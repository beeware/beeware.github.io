These recommendations and it's mini-tutorial is an alternative setup for Mac OS X environment.
This is an alternative to the management of python environments and project virtual environment with the Anaconda packaged installs of python(s). See this link for the Anaconda ways.... http://bit.ly/sprint-setup

## Python Versions in a Mac development environment

Using different versions of python can be easy and can be hard....
All Mac OS X system come with a version of python - an old version of python - that you should forget about and never use unless you are not doing environment.... This means in general, there are some system administration and tools

Here is one example of the system level pythons on a Mac OS X 10.10.5 ( Yosemite ) machine

>>ll /usr/bin/python*
32 -rwxr-xr-x  2 root  wheel  58416 Jul 14  2015 /usr/bin/python
 0 -rwxr-xr-x  5 root  wheel    925 Sep  9  2014 /usr/bin/python-config
 8 lrwxr-xr-x  1 root  wheel     75 Dec  5 16:53 /usr/bin/python2.6 -> ../../System/Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6
 8 lrwxr-xr-x  1 root  wheel     82 Dec  5 16:53 /usr/bin/python2.6-config -> ../../System/Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6-config
 8 lrwxr-xr-x  1 root  wheel     75 Dec  5 16:53 /usr/bin/python2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7
 8 lrwxr-xr-x  1 root  wheel     82 Dec  5 16:53 /usr/bin/python2.7-config -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7-config
32 -rwxr-xr-x  2 root  wheel  58416 Jul 14  2015 /usr/bin/pythonw
 8 lrwxr-xr-x  1 root  wheel     76 Dec  5 16:53 /usr/bin/pythonw2.6 -> ../../System/Library/Frameworks/Python.framework/Versions/2.6/bin/pythonw2.6
 8 lrwxr-xr-x  1 root  wheel     76 Dec  5 16:53 /usr/bin/pythonw2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/pythonw2.7

Notice that the system version of python is located in /usr/bin/python and checking the version for this Mac OS X Yosemite system we see

>>/usr/bin/python -V
Python 2.7.10

 In contrast, here are some additional the python versions that are used and managed by a command line tool pyenv

>>pyenv versions
  system
  2.7.11
* 3.4.4 (set by /Volumes/Development/python/pycon2016/beeware_projects/pybee.github.io/contributing/.python-version)
  3.4.4/envs/badguys
  3.4.4/envs/py_requests
  3.4.4/envs/tdd-workshop
  3.4.4/envs/tls-workshop
  badguys
  py_requests
  pypy-5.0.0
  stackless-3.4.1
  tdd-workshop
  tls-workshop


Thus we need to create a development environment to use other pythons and to keep them save from each other, the system version and your sanity as a dependency tracker/hacker.

## How to get started

If you are on a Mac, the preferred package management system for terminal applications is Homebrew.

To install homebrew can be easy
It is the preferred and most trouble free method to use two homebrew installed terminal tools to manage your python versions and your python virtual environments - pyenv and pyenv-virtualenv.

The install is easy.

>>brew install pyenv
>>brew install pyenv-virtualenv

You will notice that when you run these two commands that you will recieve instructions to add a line of code to your "dot files". Depending on the way you use your terminal environment, these commands will be added to your .bash_profile, .profile or another "dot file" in your home directory. For completeness. These dot files are invisible if you use the Finder to look for them.... so don't do that.... better to use the terminal...

>>ls -ad .*
.       .boot2docker      .gvimrc       .rnd
..        .cache        .hgignore_global    .rstudio-desktop
.CFUserTextEncoding   .chef       .ipynb_checkpoints    .splunk
.DS_Store     .chefdk       .irb_history      .sqlite_history
.Rapp.history     .config       .jenkins      .ssh
.Rhistory     .continuum      .le       .ssh.zip
.Trash        .cups       .lesshst      .subversion
.Xauthority     .denominatorconfig    .loggly       .swt
.ZendStudio     .distlib      .lpass        .thucydides
.android      .docker       .m2       .vagrant.d
.ansible      .dropbox      .npm        .vim
.atom       .dynupdater     .oracle_jre_usage   .viminfo
.aws        .erlang.cookie      .ovftool.ssldb      .vimrc
.bash-profile     .fontconfig     .plexht       .zend
.bash_history     .gem        .profile      .zlogin
.bash_profile     .gitconfig      .pyenv        .zprofile
.bash_profile-anaconda.bak  .gitignore_global   .python_history     .zs
.bash_profile.pysave    .gitkraken      .qicon        .zshrc
.bashrc       .gnupg        .qnicon
.berkshelf      .gradle       .rediscli_history

Over time you will accumulate lots of "dot files"

For the purposes of these directories was need to focus on the ones that effect the "environment" of your development. And in particular you need to "tune" for PATH to search and use the version of python that is right for the project.

Typing env at the terminal prompt will show you all the hidden environment variables in your system .... here is one example of what these look like.

```
>>env

TERM_PROGRAM=Apple_Terminal
PYENV_ROOT=/usr/local/opt/pyenv
SHELL=/usr/local/bin/bash
TERM=xterm-256color
TMPDIR=/var/folders/gg/bk91_2dd7f350l2js_kdvyzh0000gn/T/
Apple_PubSub_Socket_Render=/private/tmp/com.apple.launchd.QNz6Jr57BG/Render
TERM_PROGRAM_VERSION=343.7
TERM_SESSION_ID=230E7584-2AAB-4EE8-A9E6-6CA9C8C17DC3
USER=yourusernamehere
SSH_AUTH_SOCK=/private/tmp/com.apple.launchd.sQQViqA1W8/Listeners
__CF_USER_TEXT_ENCODING=0x1F5:0x0:0x0
PYENV_VIRTUALENV_INIT=1
PATH=/opt/chefdk/bin:/Users/YOURUSERNAMEHERE/.chefdk/gem/ruby/2.1.0/bin:/opt/chefdk/embedded/bin:/usr/local/Cellar/pyenv-virtualenv/20160315/shims:/usr/local/opt/pyenv/shims:/usr/local/opt/pyenv/bin:/usr/local/bin:/Users/YOURUSERNAMEHERE/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/usr/local/MacGPG2/bin:/Users/YOURUSERNAMEHERE/opt/wireshark/bin:/bin:/bin:/usr/local/packer
PWD=/Volumes/Development/python/pycon2016/beeware_projects/pybee.github.io/contributing
LANG=en_US.UTF-8
PYTHONSTARTUP=/Users/YOURUSERNAMEHERE/.pystartup
MY_PUBLIC_SSH_KEY_PATH=/Users/YOURUSERNAMEHERE/.ssh/id_rsa.pub
XPC_FLAGS=0x0
PS1=\d \t \u@\h:\w >>
HISTCONTROL=ignoreboth
XPC_SERVICE_NAME=0
PYENV_SHELL=bash
SHLVL=1
HOME=/Users/YOURUSERNAMEHERE
LOGNAME=YOURUSERNAMEHERE
SECURITYSESSIONID=186a6
OLDPWD=/Volumes/Development/python/pycon2016/beeware_projects/pybee.github.io
_=/usr/bin/env

```

[Testing URL to pybee's github account](http://pybee.github.io)


^^^^^^
Edited stuff above here
^^^^^^
Copied stuff below here
\/ \/ \/ \/

## Modules

See http://python-packaging-user-guide.readthedocs.io/en/develop/installing/

A lot of python works like this:
```
 from coolproject import life_saving_code
```

But where do these modules come from, and how do we get them?

## Installing Modules from Source
Well, we could install them from source. This is often something like:

```
git checkout python_package
cd python_package
python setup.py install # or python setup.py install --user
```

Of course, you should ask yourself _Where does this install to?_

Another way would be to do a

```
python setup.py build
export PYTHONPATH=`pwd`:$PYTHONPATH
```

This is fine for the occasional module, but it quickly becomes tiresome.

How do we install a python module without "compiling" something?

### Installing Modules from PyPI: pip
Originally, the answer was `easy_install`. This was a packaging tools that had the virtue of being shipped with python, and installed modules stored in a file format called _egg_. I say this just to be historically accurate. There is [no reason to use easy_install anymore](http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install).

The new hotness is a tool called pip. Pip also lets you install packages packaged in the new <code>wheel</code> format described in [PEP 427](https://www.python.org/dev/peps/pep-0427 PEP 427). If you really want to know, you can look here for the differences between [wheel and egg](http://python-packaging-user-guide.readthedocs.io/en/latest/wheel_egg/ wheel and egg).

### Installing Modules from Anaconda
There's a new kid on the block. It's called `conda`, and in a lot of cases, it is a vast improvement over both of these. Conda is aimed at scientific computing and data science, and is absolutely essential if your code has non-python depencies, but it's a fantastic packaging tool in its own right, and we think you should give it a try.

```
 conda install packagename
```

The only real drawback of `conda` is that it may not have all the packages you need. But that's okay, because  *you can easily mix pip and conda*. Why would you do that? You'll see shortly, after we talk about Virtual Environments.

## Virtual Environments
There's an issue with modules. After a while, your installed modules become difficult to maintain. What's worse, you may need different versions of modules for different applications. The biggest example of this is python2 vs 3.

Wouldn't it be nice if you could create a clean, fresh python install for every different way that you use it?

Enter Virtual Environments.

virtualenv is a tool to create isolated Python environments. To install it, do a

```
 pip install virtualenv
```

To create a new environment
```
 cd path_to_workdir
 virtualenv my_env
```

or you can be explicit about your python interpreter:
```
 virtualenv -p /usr/bin/python2.7 my_env27
```

See what is installed:
```
 source my_env27/bin/activate
 which python
 pip list
 # ... do work
 deactivate
 which python
```
### Saving and Recreating your Environment
Letting others recreate your environment is very useful.

You can record the current set of dependencies with:

```
 pip freeze > requirements.txt
```

This file will contain a list of all the packages in your environment, and their associated version numbers. if you, or someone else needs to later re-create the environment, you can do a:

```
 pip install -r requirements.txt
```

### Conda virtual environments

Of course, anaconda has these too.
```
 conda create -n data3 python=3.5
 source activate data3
 conda install jupyter matplotlib seaborn numpy
 # ...  do work
 source deactivate
```
We could have combined the installation and creation lines as such:

```
 conda create -n data3 python=3.5 jupyter matplotlib seaborn numpy
```

What's more, you **can mix pip and conda in a conda virtualenv**. So you really don't have to choose between pip and conda. You can (and likely should) do both.
