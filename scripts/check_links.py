# -*- coding: utf-8 -*-
"""
Check status of links from anchors and images on the generated site.

mailto: links are currently ignored
"""

# Standard library imports
from __future__ import print_function
import datetime
import os
import shutil
import subprocess
import sys
import tempfile

# Third party imports
from bs4 import BeautifulSoup
import requests


try:
    import urlparse as parse
except ImportError:
    import urllib.parse as parse


HERE = os.path.abspath(os.path.dirname(__file__))
REPO = os.path.dirname(HERE)
TIMEOUT = 10  # Seconds
TIMEOUT_RETRIES = 3  # Amount of retries on link check when ReadTimeOut error
WHITELIST = [
    'https://github.com/beeware/beeware.github.io/edit/lektor/content/',
    'https://github.com/beeware/beeware.github.io/new/lektor/content/',
    'https://github.com/issues?q=user%3Abeeware+label%3Afirst-timers-only+is%3Aopen&type=Issues',
    'https://github.com/issues?q=user%3Abeeware+label%3Aup-for-grabs+is%3Aopen&type=Issues',
]


def normalize_url(url, root_url):
    """Normalize a url based on a site root url"""
    if url.startswith(('http')):
        norm_link = url
    elif url.startswith('mailto'):
        norm_link = None
    else:
        norm_link = parse.urljoin(root_url, url)
    return norm_link


def get_files(root_path, extensions=('.html',)):
    """Return all files located in root_path that match extensions."""
    all_paths = []
    for dirname, subdirlist, filelist in os.walk(root_path):
        for fname in filelist:
            if fname.endswith(extensions):
                print('.', end='')
                fpath = os.path.join(dirname, fname)
                all_paths.append(fpath)

    all_paths = list(sorted(all_paths))

    return all_paths


def parse_urls(fpath, root_url):
    """Parse html file using BS4 and find links for anchors and images."""
    urls = set()
    if os.path.isfile(fpath):
        with open(fpath, 'r') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # Find anchors
        for tag in soup.find_all('a', href=True):
            url = tag['href']
            norm_url = normalize_url(url, root_url)
            if norm_url:
                urls.add(norm_url)

        # Find images
        for tag in soup.find_all('img', src=True):
            url = tag['src']
            norm_url = normalize_url(url, root_url)
            if norm_url:
                urls.add(norm_url)

    return urls


def check_link(url, root_url, root_path):
    """"""
    error = None
    status = 0
    content = ''
    headers = headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/39.0.2171.95 Safari/537.36')}

    try:
        if url.startswith(root_url):
            # Check if actual file path exists, otherwise try to use requests
            sep = os.sep*2 if os.name == 'nt' else os.sep
            url_path = url.replace(root_url[:-1], root_path).replace('/', sep)
            # print(url_path, os.path.isdir(url_path))
            if os.path.isdir(url_path) or os.path.isfile(url_path):
                status = 200
            else:
                r = requests.get(url, headers=headers, timeout=TIMEOUT)
                content = r.content
                status = r.status_code
        else:
            r = requests.head(url, headers=headers, timeout=TIMEOUT)
            status = r.status_code
    except Exception as e:
        error = True
        status = type(e).__name__

    if ("Brutus can't find what you're looking for" in content and
            not url.endswith('404.html')):
        res = 404
    elif status not in [200, 301, 302] or error:
        res = status or error
    else:
        res = None

    if res:
        res = str(res)

    return res


def execute(cmd):
    """Execute cmd with popen and yield the output form stdout."""
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, universal_newlines=True)

    for stdout_line in iter(popen.stdout.readline, ""):
        # Yield process and stdout output, that way the process can be killed
        yield popen, stdout_line

    popen.stdout.close()
    return_code = popen.wait()

    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def run_link_checks(root_path, root_url):
    """Run checks on links found for anchors and images."""
    print('\nFinding built files:\n')
    file_paths = get_files(root_path)
    file_links = {}

    print('\n\nParsing built files for links:\n')
    for i, fpath in enumerate(file_paths):
        # print('\n')
        # print(i, fpath)
        print('.', end='')
        file_links[fpath] = set()
        links = parse_urls(fpath, root_url)
        for link in links:
            # print('.', end='')
            file_links[fpath].add(link)

    link_files = {}
    for fpath, links in file_links.items():
        for link in links:
            if link not in link_files:
                link_files[link] = set()
            link_files[link].add(fpath)

    issues = len(link_files)
    plural = 's' if issues != 1 else ''
    print('\n\nFound {0} unique link{1}!\n'.format(issues, plural))
    print('\nChecking links\n'.format(issues, plural))
    counter = 0
    for i, link in enumerate(sorted(link_files)):
        # Ignore `edit content on github` links as they would take too long
        if any(link.startswith(i) for i in WHITELIST):
            continue

        # sys.stdout.write("{0}\r".format(i))
        # sys.stdout.flush()
        fpaths = link_files[link]

        for j in range(TIMEOUT_RETRIES):
            check = check_link(link, root_url, root_path)
            if check:
                if 'ReadTimeout' in check:
                    print('\nRetrying...\n')
                else:
                    break
            else:
                break

        if check:
            print('\n\nError number: {0}'.format(counter))
            print('Status code or error type: {0}'.format(check))
            print('{0}'.format(link))
            print('-'*len(link))
            for fpath in sorted(fpaths):
                clean_fpath = fpath.replace(root_path, '')
                clean_url = root_url[:-1] + os.path.dirname(clean_fpath)
                print('\t' + clean_url)
            counter += 1
            print('\n')
        else:
            print('.', end='')

    return counter


def main():
    """Run main script."""
    start_time = datetime.datetime.now()
    temp_build_path = tempfile.mkdtemp()
    port = '5000'
    root_url = 'http://127.0.0.1:{0}/'.format(port)

    # Remove build folder if it exists
    if os.path.isdir(temp_build_path):
        shutil.rmtree(temp_build_path, ignore_errors=True)

    cmd = ['lektor', 'server', '--no-prune', '--port', port, '--output-path',
           temp_build_path]

    print('\nRunning Lektor Server:')
    print('\t$ ' + ' '.join(cmd) + '\n')

    count = 0
    finished_build = False
    print('\nBuilding static site:\n')
    for p, stdout in execute(cmd):
        if stdout and not finished_build:
            print('.', end='')

        if 'Finished build' in stdout:
            finished_build = True
            print('\n\nFinished building site!\n\n')
            count = run_link_checks(temp_build_path, root_url)

            # Kill the server
            p.kill()
            break

    # Remove build folder
    if os.path.isdir(temp_build_path):
        shutil.rmtree(temp_build_path, ignore_errors=True)

    total_seconds = (datetime.datetime.now() - start_time).total_seconds()

    # Fail if problems found, otherwise do a normal exit
    if count:
        if count != 1:
            print('\n\n{} links are broken!'.format(count))
        else:
            print('\n\n{} link is broken!'.format(count))
        exit_code = 1
    else:
        print('\n\nAll links found are working fine!')
        exit_code = 0

    print('\nProcess took {} seconds\n'.format(total_seconds))
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
