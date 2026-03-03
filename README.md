# beeware.org

This is the homepage for the [BeeWare project](http://beeware.org).

It is a [MkDocs](https://mkdocs.org)-based site. The site is hosted on GitHub Pages, with PR builds being provided by ReadTheDocs.

## Getting started

To view a local build of this website, create a virtual environment, and install the development requirements:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install --group dev
```

Then from the root directory of the checkout, run:

```sh
(venv) $ tox -e docs-live
```

This will [start a web server](http://127.0.0.1:8042) that will automatically reload whenever you make a change to site content. This will only build the English version of the site; to build and test the *full* site, run:

```sh
(venv) $ tox -e docs-all,docs-serve
```

This will also [start a web server](http://127.0.0.1:8042); however the content will *not* automatically reload.

## Financial support

The BeeWare project would not be possible without the generous support of our financial members:

[![Anaconda logo](https://beeware.org/images/anaconda-dark.png)](https://anaconda.com/)

Anaconda Inc. - Advancing AI through open source.

Plus individual contributions from [users like you](https://beeware.org/community/members/). If you find Briefcase, or other BeeWare tools useful, please consider becoming a financial member.

## Community

You can talk to the community through:

- [@beeware@fosstodon.org on Mastodon](https://fosstodon.org/@beeware)
- BeeWare Discord server: [Discord](https://beeware.org/bee/chat/)
- [Tickets on the website issue tracker](https://github.com/beeware/website/issues)

### Code of Conduct

The BeeWare community has a strict [Code of Conduct](https://beeware.org/community/code-of-conduct/). All users and developers are expected to adhere to this code.

If you have any concerns about this code of conduct, or you wish to report a violation of this code, please contact the project founder [Russell Keith-Magee](mailto:russell@keith-magee.com).

### Contributing

If you find problems with this website, [log them on GitHub](https://github.com/beeware/website/issues). If you want to contribute a modification you can fork this repository and submit a pull request.

### Translations

We manage translations using [Weblate](https://weblate.org/). Updates to translated content should be submitted through Weblate, not as PRs to this repository.

<a href="https://hosted.weblate.org/projects/beeware/website/"><img src="https://hosted.weblate.org/widget/beeware/website/open-graph.png" width="300px" alt="Website translation status"></a>

<a href="https://hosted.weblate.org/engage/beeware/"><img src="https://hosted.weblate.org/widget/beeware/website/horizontal-auto.svg" alt="Translation status" /></a>

If you'd like to contribute to the translation effort, join the `#translations` channel on [Discord](https://beeware.org/bee/chat/) and introduce yourself!
