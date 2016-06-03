These recommendations and it's mini-tutorial is an alternative setup for Mac OS X environment that uses Homebrew + pyenv + pyenv-virtualenv.
This is an alternative to the management of python environments and project virtual environment with the Anaconda packaged installs of python(s). See this link for the Anaconda ways.... http://bit.ly/sprint-setup

## Python Versions in a Mac development environment

Developing with multiple versions of Python can be easy but can be hard be to get started if one starts down one path of recommendations for your environment ( your computer ) and then get stuck or try a different set of recommendations. For a typical Mac User, even a developer this can a work in progress.

One base fact is that all Mac OS X system come with a version of python - an old version of python - that you should forget about and almost never use for development unless you are writing scripts to do some for your mac environment and only your mac environment .... In general, this mean for administering your computer or a local one time tool for you alone. Perhaps you will find that opinion harsh but experience tells us this. What this means to you the developer setting up your computer for python development is that you need to leave the system python alone and make sure you use a "User Space" Python. It is also useful to understand which the system Python(s) live so you can make sure you are using the Python versions you intend.

Here is one example of the system level Pythons on a Mac OS X 10.10.5 ( Yosemite ) machine

>>ls -lsa /usr/bin/python*
32 -rwxr-xr-x  2 root  wheel  58416 Jul 14  2015 /usr/bin/python
 0 -rwxr-xr-x  5 root  wheel    925 Sep  9  2014 /usr/bin/python-config
 8 lrwxr-xr-x  1 root  wheel     75 Dec  5 16:53 /usr/bin/python2.6 -> ../../System/Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6
 8 lrwxr-xr-x  1 root  wheel     82 Dec  5 16:53 /usr/bin/python2.6-config -> ../../System/Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6-config
 8 lrwxr-xr-x  1 root  wheel     75 Dec  5 16:53 /usr/bin/python2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7
 8 lrwxr-xr-x  1 root  wheel     82 Dec  5 16:53 /usr/bin/python2.7-config -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7-config
32 -rwxr-xr-x  2 root  wheel  58416 Jul 14  2015 /usr/bin/pythonw
 8 lrwxr-xr-x  1 root  wheel     76 Dec  5 16:53 /usr/bin/pythonw2.6 -> ../../System/Library/Frameworks/Python.framework/Versions/2.6/bin/pythonw2.6
 8 lrwxr-xr-x  1 root  wheel     76 Dec  5 16:53 /usr/bin/pythonw2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/pythonw2.7

Notice that the system versions of Python are "seen" in Userspace at /usr/bin/python but are syslinked to System Space. Another thing to notice about this is the owner of these Pythons is root/wheel. This is another clue that you really don't want to use these Pythons because changing them requires root permissions and or sudo to get there and this is a trap. Checking the actual version that one would get if they used the system Python this Mac OS X Yosemite system we see

>>/usr/bin/python -V
Python 2.7.10

Now that our opinion about NOT using the system Python is clear and we know where it lives, we a ready to examine where to install Python(s) and how.

Here is an example of some Pythons and "virtual environments" installed using a command line tool called pyenv. URL HERE

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

The Python versions include the "system Python", plus versions 2.7.11, 3.4.4, pypy-5.0.0, and stackless-3.4.1. The Python virtual environments include each of those versions above and several named virtual environments - badguys, py_requests, tdd-workshop, tls-workshop.

In contrast to the Mac OS X "system Pythons" these pyenv Pythons are installed in "User Space" and with NO root or sudo permission - this is important. The system is owned by the Apple installer and updaters and to be used for development would required more that Userspace permissions. Our goal is to never use "System Space", root or sudo for this guide and to never have Apple mess with our development space. Thus we need to create a development environment to use other Pythons and to keep them safe from each other, the system versions, and your sanity as a dependency tracker/hacker.

## How to get started

We are going to add one more opinion. If you are on a Mac, the preferred package management system for terminal applications is called Homebrew. It is your friend and it is Homebrew that will both get into trouble and stay out of trouble if you follow the recommends of Homebrew developers and those here.

OK. From the beginning. Assuming you are a beginner. Go to your Finder. Navigate to the Terminal.app in your Application's Utilities folder. Launch it.

At the terminal prompt we first HomeBrew. To check for it type

>>brew

To install HomeBrew is normally easy. [HomeBrew Website](http://brew.sh)

If you are lucky enough to have a new system without homebrew here is the terminal command to install homebrew. Follow the HomeBrew getting started tutoral here. 

>>/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

LINK to Screenshot of homebrew install
Yes, you will need to give Homebrew root permission to install itself but Homebrew is "safe" - ( but of course - we cannot guarentee nothing will ever go wrong because time marches on... )

If you already have Homebrew installed, then you MAY have to uninstall some of the python related things you have already installed to have a clean and straightforward development environment. But that is an aside that we will leave to the [troubleshooting guide.](./mac-troubleshooting-guide.mdown)

It is the preferred and most trouble free method to use two homebrew installed terminal tools to manage your python versions and your python virtual environments - pyenv and pyenv-virtualenv.

Once homebrew is in place. The install is easy.

>>brew install pyenv 
<INSERT LINK TO SCREENSHOT>
Most of the install comments can be ignored safely
Note these comments though and act on them...
Ignore first "Caveats" because we have an opinion and we are not going to go this.....
We will act on the second "Caveat" after you run the next brew install

==> Caveats
To use Homebrew's directories rather than ~/.pyenv add to your profile:
  export PYENV_ROOT=/usr/local/var/pyenv

To enable shims and autocompletion add to your profile:
  if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi

Now install pyenv-virtualenv

>>brew install pyenv-virtualenv
...
==> Caveats
To enable auto-activation add to your profile:
  if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
...

You will notice that when you run these two commands above that you will recieve instructions to add a line of code "to your profile" - This is your "dot files". Sorry this requires a little discussion.... Depending on the way you use your terminal environment, these commands will be added to your .bash_profile, .profile or another "dot file" in your home directory. For completeness. These dot files are invisible if you use the Finder to look for them.... so don't do that.... better to use the terminal...

Where are your "Dot Files" and which ones you ask....
On a Mac Dot Files are hidden by default. To list them at the terminal, use the ls command with flags to expose them. This shows a collection of dot files.

Insert about Dot Files

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

Over time you will accumulate lots of "dot files".

The ones that are Python related for this tutorial are:
.bashrc
.bash_profile
.profile

and the directories 
.ssh
.pyenv

.python_version

For the purposes of these directories was need to focus on the ones that effect the "environment" of your development. And in particular you need to "tune" for PATH to search and use the version of python that is right for the project.

Typing env ( pronounced "Environment" ) at the terminal prompt will show you all the hidden "environment variables" in your system .... here is one example of what these look like.

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
END OF INSERT ABOUT DOT FILES

OK. insert the two line into your dot file as appropriate for you and run a test to see if we have successfully setup our development environment for python.
Test
INSERT BLOCK OF TERMINAL 

>> pyenv versions
* system (set by /Users/myusername/.pyenv/version)
>> pyenv install 3.4.4
Downloading Python-3.4.4.tgz...
-> https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tgz
Installing Python-3.4.4...
Installed Python-3.4.4 to /Users/myusername/.pyenv/versions/3.4.4

>> pyenv versions
* system (set by /Users/myusername/.pyenv/version)
  3.4.4

>> env | grep PATH
PATH=/Users/myusername/.pyenv/shims:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/Server.app/Contents/ServerRoot/usr/bin:/Applications/Server.app/Contents/ServerRoot/usr/sbin

Create a .python_version file that determine that we want to use python 3.4.4
>> pyenv local 3.4.4
>> ls -lsa .python-version 
8 -rw-r--r--  1 myusername  staff  6 Jun  3 11:24 .python-version
>> cat .python-version 
3.4.4
>> 

>> python -V
Python 2.7.10
Hummmm..... What's wrong?
>> pyenv rehash
>> python -V
Python 3.4.4
So, we are good...
Where is this happening...

So, when you run >>python what is happening is that pyenv has added a "shim" in your path that tells your shell to look for python in a particular place 

>> which python
/Users/myusername/.pyenv/shims/python

And because this is first in your shell PATH variable thus whatever this shim is linked to will be the python.... that you get.... You can look at the contents of the file called "python" in the shims directory.... it is a little shell script that does the magic.








[Testing URL to pybee's github account](http://pybee.github.io)


When you are all setup in the Homebrew, pyenv, pyenv-virtualenv way, this how to work with the it....

to download a a begin using a number version of Python
>>pyenv install --list 
This gives a very long list of possible Pythons
  2.1.3
...
  2.7.10
  2.7.11
  3.0.1
...
  3.4.4
  3.5.0
  3.5-dev
  3.5.1
  3.6-dev
  anaconda-1.4.0
...
  anaconda3-2.5.0
  anaconda3-4.0.0
  ironpython-dev
...
  ironpython-2.7.5
  jython-dev
  jython-2.5.0
...
  jython-2.7.0
  jython-2.7.1b1
  jython-2.7.1b2
  jython-2.7.1b3
  miniconda-latest
  miniconda-2.2.2
...
  miniconda3-3.19.0
  miniconda3-4.0.5
...
  pypy-portable-5.1
  pypy-portable-5.1.1
  pypy-1.5-src
  pypy-1.5
...
  pypy-5.1.1-src
  pypy-5.1.1
...
  pypy3-2.4.0-src
  pypy3-2.4.0
  stackless-dev
  stackless-2.7-dev
 ...
  stackless-3.4.1
The "..." mean there are many more inbetween... 
Select the python version of interest....
>> source activate my-virtualenv-name
pyenv-virtualenv: deactivate 
pyenv-virtualenv: activate my-virtualenv-name
pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.
(my-virtualenv-name) >> which python
/Users/myusername/.pyenv/shims/python
(my-virtualenv-name) >> python -V
Python 3.4.4
(my-virtualenv-name) >> pyenv install 3.5.1
Downloading Python-3.5.1.tgz...
-> https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
Installing Python-3.5.1...
Installed Python-3.5.1 to /Users/myusername/.pyenv/versions/3.5.1

(my-virtualenv-name) >> pyenv versions
  system
  3.4.4
  3.4.4/envs/my-virtualenv-name
  3.5.1
* my-virtualenv-name (set by PYENV_VERSION environment variable)
(my-virtualenv-name) >> pyenv virtualenv 3.5.1 my-bleeding-edge-virtualenv
Ignoring indexes: https://pypi.python.org/simple
Requirement already satisfied (use --upgrade to upgrade): setuptools in /Users/myusername/.pyenv/versions/3.5.1/envs/my-bleeding-edge-virtualenv/lib/python3.5/site-packages
Requirement already satisfied (use --upgrade to upgrade): pip in /Users/myusername/.pyenv/versions/3.5.1/envs/my-bleeding-edge-virtualenv/lib/python3.5/site-packages
(my-virtualenv-name) >> . activate my-bleeding-edge-virtualenv
pyenv-virtualenv: deactivate 3.4.4/envs/my-virtualenv-name
pyenv-virtualenv: activate my-bleeding-edge-virtualenv
pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.
(my-bleeding-edge-virtualenv) >> which python
/Users/myusername/.pyenv/shims/python
(my-bleeding-edge-virtualenv) >> python -V
Python 3.5.1
(my-bleeding-edge-virtualenv) >> python
Python 3.5.1 (default, Jun  3 2016, 11:59:30) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(my-bleeding-edge-virtualenv) >> 

^^^^^^
Edited stuff above here
^^^^^^
Copied stuff below here is from other approach for comparison only.... using the methods and directions below may ( will likely ) give you problems. Don't try to mix and match different ways of managing your development environment.

See troubleshoot tip and ask for additional assistance in the FAQs.

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
