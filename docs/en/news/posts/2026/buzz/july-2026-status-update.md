---
title: July 2026 Status Update
date: 2026-08-03
authors:
- freakboy3742
categories:
- Buzz
---

In July, we added `uv` support to Briefcase, landed some patches for mobile support in some major Python projects, and welcomed a new member to the BeeWare core team.

<!-- more -->

## What we've done

- We welcomed [Oliver Leigh to the core team](https://github.com/beeware/beeware.github.io/pull/813), in recognition of his ongoing contributions to Toga's WinForms backend.
- We attended EuroPython, where [Malcolm Smith spoke about supporting Android and iOS in Python packages](https://ep2026.europython.eu/session/supporting-android-and-ios-in-your-python-package).
- We continued the rework of Briefcase's environment management, adding [isolated virtual environments for each app](https://github.com/beeware/briefcase/pull/2967),and [support for using `uv` to manage app environments](https://github.com/beeware/briefcase/pull/2970). Support for [using Conda to manage app environments](https://github.com/beeware/briefcase/pull/2972) is in the final stages of review.
- We finalized [Android](https://github.com/numpy/numpy/pull/32032) and [iOS](https://github.com/numpy/numpy/pull/28759) support in NumPy. Android and iOS have now been accepted as [Tier 3 supported platforms in NumPy](https://github.com/numpy/numpy/pull/32032).
- We contributed iOS support for [`contourpy`](https://github.com/contourpy/contourpy/pull/556) and [`kiwisolver`](https://github.com/nucleic/kiwi/pull/238).
- We [resolved a long-standing issue with the stability of the iOS simulator on GitHub Actions](https://github.com/python/cpython/pull/153632).
- We [exposed macOS app lifecycle notifications as hooks](https://github.com/beeware/toga/pull/4599), giving app authors a way to respond to native lifecycle events such as activation, hiding, and termination.
- We [finalized Toga's switch to `libgirepository` 2.0](https://github.com/beeware/toga/pull/4556), formally deprecating support for Debian 12 and Ubuntu 22.04.
- We added [a new WinForms event loop implementation that dramatically improves the performance of Windows apps](https://github.com/beeware/toga/pull/4459).
- We fixed a cluster of WinForms DPI scaling problems, including [issues with `Canvas` scaling](https://github.com/beeware/toga/pull/4584), [some DPI scaling bugs](https://github.com/beeware/toga/pull/4577), and [incorrect divider positioning](https://github.com/beeware/toga/pull/4566).
- We extracted the Microsoft `WebView2` binary components out of `toga-winforms` [into their own package](https://github.com/beeware/toga/pull/4582).
- We added [`system-pyside6` integration for Toga's Qt backend](https://github.com/beeware/toga/pull/4534), allowing Toga to follow the operating system's theme on Qt-based Linux desktops.
- We fixed [keyboard dismissal on input widgets on iOS](https://github.com/beeware/toga/pull/4452).
- We added [a testbed probe for the Textual backend](https://github.com/beeware/toga/pull/4527), allowing automated testing of that backend.
- We started [implementing Toga's new Scaffold layer](https://github.com/beeware/toga/pull/4382). This is the start of the "Big Picture app navigation" design that we published earlier this year.
- We corrected an issue with [shut down event handling in Rubicon ObjC](https://github.com/beeware/rubicon-objc/pull/785).
- We [removed a vestigial logging handler](https://github.com/beeware/briefcase-iOS-Xcode-template/pull/74) left over from the `NSLog` to `os_log` migration in the iOS Xcode template.
- We added [support for creating a desktop shortcut for Windows apps](https://github.com/beeware/briefcase-windows-app-template/pull/100).
- We fixed an MSI packaging bug where [shortcut descriptions longer than 256 characters would break the installer](https://github.com/beeware/briefcase-windows-app-template/pull/103).
- We added [a fix for the "Mark of the Web" problem with Windows apps distributed as ZIP files](https://github.com/beeware/briefcase/pull/2959).
- We replaced `flake8` and `isort` with Ruff in [Briefcase's project template](https://github.com/beeware/briefcase-template/pull/272).
- We started hardening our GitHub Actions workflows, adding [`zizmor` security scanning across many of our repositories](https://github.com/beeware/briefcase/pull/2939), [consolidating our Dependabot configuration with cool down periods](https://github.com/beeware/beeware.github.io/pull/807) and [adding multi-ecosystem grouping](https://github.com/beeware/briefcase-windows-app-template/pull/110).
- We added [Ukrainian translations of the BeeWare website](https://github.com/beeware/beeware.github.io/pull/812).
- We [reworked the success stories page](https://github.com/beeware/beeware.github.io/pull/809) on the BeeWare website, and added [a new success story from Juno](https://github.com/beeware/rubicon-objc/pull/800).

Much of this work is due to the contributions of members of the BeeWare community. Thanks to <nospell>Rahul Patel ([@100jinwoo001](https://github.com/100jinwoo001)), Abdo ([@abdnh](https://github.com/abdnh)), Oluwatoyosi Peter Abolaji ([@abj360](https://github.com/abj360)), [@alex-indi](https://github.com/alex-indi), Michaela Dušková ([@amfibio](https://github.com/amfibio)), [@armorbreak001](https://github.com/armorbreak001), Andrew Barnes ([@Bortlesboat](https://github.com/Bortlesboat)), [@ColumbusLabs](https://github.com/ColumbusLabs), Daniel Del Rio ([@ddelrio1986](https://github.com/ddelrio1986)), Dresden ([@DresdenGman](https://github.com/DresdenGman)), [@emerardd](https://github.com/emerardd), Jan Koprowski ([@jankoprowski](https://github.com/jankoprowski)), [@jlonsdalen](https://github.com/jlonsdalen), John ([@johnzhou721](https://github.com/johnzhou721)), Kevin Turcios ([@KRRT7](https://github.com/KRRT7)), Aleš Laník ([@Krumca97](https://github.com/Krumca97)), Robin ([@lrandersson](https://github.com/lrandersson)), Jonathan ([@mgalore](https://github.com/mgalore)), Mgs. Tabrani ([@mgstabrani](https://github.com/mgstabrani)), Matt Van Horn ([@mvanhorn](https://github.com/mvanhorn)), Rohit Madhavan ([@ROHITCRAFTSYT](https://github.com/ROHITCRAFTSYT)), Shaurya Srivastava ([@Shaurya2k06](https://github.com/Shaurya2k06)), [@Solaris-star](https://github.com/Solaris-star), Sneha ([@suscripty](https://github.com/suscripty)), Likhitha J ([@TensorDevLJ](https://github.com/TensorDevLJ)), Thomas Nguyen ([@thomxsnguyen](https://github.com/thomxsnguyen)), and xintao ([@xintao0312](https://github.com/xintao0312))</nospell> for their code and documentation contributions this month.

## What's next?

In the coming month, we'll be looking at Briefcase's handling of downloads. The main improvement will be adding support for hash verification of downloads; but we're also hoping to develop a better workflow for bootstrapping a Briefcase installation, especially in tutorial situations.

We will also be performing some updates to Toga's Android backend. Android SDK 36 introduced some changes to the visual layout of apps. Until recently, we've been able to work around these issues; but by the end of August, Google will require all apps to be fully compliant with SDK 36 to be submitted to the App Store.

At the end of the month, we will be attending [PyCon AU](https://2026.pycon.org.au), where we'll be presenting a [workshop on building cross-platform GUI apps](https://2026.pycon.org.au/schedule/H33RW8/), plus talks on [mechanisms for distributing Python code](https://2026.pycon.org.au/schedule/AVCYHU/) and [switching your project documentation from Sphinx to Markdown](https://2026.pycon.org.au/schedule/ZYSPB3/). We'll also be there for [the Development Sprint day](https://2026.pycon.org.au/schedule/sunday/). If you're able to make it, make sure you say hello!

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
