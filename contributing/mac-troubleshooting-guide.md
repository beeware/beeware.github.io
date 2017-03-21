Mac Troubleshooting Guide for Python Development Environments

Homebrew troubleshooting
>brew list
  There should be NO Python versions installed directly with HomeBrew
  There should be NO Python tools like pip installed with HomeBrew

For the purposes of this troubleshoot guide, if you have any issues and you have Pythons and Python tools installed with Homebrew, please stop and remove them. We will be installing these under pyenv and pyenv-virtualenv as the python development environment helper and manager.

After removing any Python versions and other HomeBrew installed packages that are python development dependencies ( Things that one of more projects need to build their software. )

Remove packages
>>brew uninstall python3

Update homebrew
>>brew upgrade

Now update the remaining packages and remove old versions 
>>brew update
>>brew cleanup
>>brew prune

And now check that homebrew believes it is health and managing the packages that are in Userspace. /usr/local/
>>brew doctor

If brew gives a warning, this MAY NOT be an actual issue but if you are here, that you probably have a problem and it is probably related to Python.... ( you are here after all ), SOOOOO ... if a warning is about Python related things then read them carefully and trying to follow the recommendations. These warning are generally correct in the sense that they point to a strong possiblity that you or some installer has added some packages to what ideally should now be HomeBrews area of management. Mostly warnings mean that you may need to carefully craft your unix PATH but YMMV.