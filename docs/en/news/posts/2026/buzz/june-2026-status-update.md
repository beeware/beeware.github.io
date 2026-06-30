---
title: June 2026 Status Update
date: 2026-07-01
authors:
- freakboy3742
categories:
- Buzz
---

June saw a major push on logging support for macOS 26, a continuing overhaul of Toga's Canvas API, as well as many other improvements.

<!-- more -->

## What we've done

- We hosted our first ["The Buzz: Live" community call](https://www.youtube.com/watch?v=b3kYCAnM88w)!
- We migrated Apple platform logging from `NSLog` to `os_log`, as [macOS 26 now marks `NSLog` content as private](https://github.com/beeware/std-nslog/pull/96). This required [Briefcase to adopt the `os_log`-based logger](https://github.com/beeware/briefcase/pull/2877), updates to the [macOS Xcode template](https://github.com/beeware/briefcase-macOS-Xcode-template/pull/122), the [Python support testbed](https://github.com/beeware/Python-support-testbed/pull/187), and [upstream in CPython](https://github.com/python/cpython/pull/150645).
- We [refined the encoding of ASCII `NUL` characters in `std-nslog`](https://github.com/beeware/std-nslog/pull/99).
- We [refactored Briefcase's handling of virtual environments](https://github.com/beeware/briefcase/pull/2885), providing a cleaner interface for creating Python environments. This is the start of a larger piece of work adding support for [using alternative environment managers - such as `uv`, Conda, or Pixi in Briefcase projects](https://github.com/beeware/briefcase/pull/2917).
- We added support for [automatically resuming an interrupted macOS notarization](https://github.com/beeware/briefcase/pull/2886), including the ability to [avoid waiting for the macOS notarization response](https://github.com/beeware/briefcase/pull/2890). These changes make it much easier to notarize a macOS app in a CI environment.
- We added support for [post-install scripts in macOS PKG installers](https://github.com/beeware/briefcase/pull/2903).
- We added [support for enforcing a minimum OS version](https://github.com/beeware/briefcase/pull/2855).
- We made MSI installers [more resilient when uninstalling an application that is currently running](https://github.com/beeware/briefcase-windows-VisualStudio-template/pull/99).
- We [improved the validation of Briefcase application names](https://github.com/beeware/briefcase/pull/2840).
- We [added warnings to guard against project paths that are known to cause problems](https://github.com/beeware/briefcase/pull/2870).
- We [added a warning when an app description exceeds the recommended length](https://github.com/beeware/briefcase/pull/2869).
- We added the ability for [Linux applications to provide a custom man page](https://github.com/beeware/briefcase/pull/2901).
- We added validation that [the requested Flatpak base is installed](https://github.com/beeware/briefcase/pull/2905) before building an app.
- We modified how Briefcase asks questions so that [if there's a single option, that response is provided as a default answer](https://github.com/beeware/briefcase/pull/2863).
- We [documented how to generate a self-signed Windows code signing certificate](https://github.com/beeware/briefcase/pull/2900).
- We [finished rolling out the use of Briefcase's warning banner helper](https://github.com/beeware/briefcase/pull/2915), ensuring that warnings in Briefcase are consistently formatted.
- We continued aligning Toga's `Canvas` widget with the HTML5 Canvas API, [deprecating `write_text` in favor of `fill_text` and `stroke_text`](https://github.com/beeware/toga/pull/4432), [turning the transform methods into states](https://github.com/beeware/toga/pull/4477), [adding keyword parameters to `Canvas.state()`](https://github.com/beeware/toga/pull/4485), and [more clearly delineating between the Canvas API levels in the documentation](https://github.com/beeware/toga/pull/4507).
- We corrected a number of issues with Toga's `Canvas` implementation, including [fixing an issue with `reset_transform` on Cocoa and iOS](https://github.com/beeware/toga/pull/4045), issues with [`DrawingAction` color aliasing logic](https://github.com/beeware/toga/pull/4472), an [inconsistency in the default Canvas stroke width](https://github.com/beeware/toga/pull/4473), and the [handling of line dashes on Qt Canvas objects](https://github.com/beeware/toga/pull/4475).
- We [updated `toga-chart` to use the revised Canvas API](https://github.com/beeware/toga-chart/pull/319).
- We corrected the colors used on [`Button` widgets](https://github.com/beeware/toga/pull/4431), [`DetailedList` widgets](https://github.com/beeware/toga/pull/4456) and [`WebView` widgets](https://github.com/beeware/toga/pull/4434) on Windows.
- We migrated the documentation for [Podium](https://github.com/beeware/podium/pull/91) and [Toga Chart](https://github.com/beeware/toga-chart/pull/332) to Markdown and MkDocs.
- We corrected some issues with how project-specific additions to our contribution guide are rendered in the documentation of [Briefcase](https://github.com/beeware/briefcase/pull/2872), [Toga](https://github.com/beeware/toga/pull/4449) and [`rubicon-objc`](https://github.com/beeware/rubicon-objc/pull/769).
- We [fixed the `ds_store` CLI](https://github.com/dmgbuild/ds_store/pull/218), and [improved the rendering of `.plist` blob values in the `ds_store` CLI output](https://github.com/dmgbuild/ds_store/pull/220).
- We [landed a round of Android fixes in `cibuildwheel`](https://github.com/pypa/cibuildwheel/pull/2933), updating to current Python versions and removing a testbed patch.
- We [added an "Available for hire" page](https://github.com/beeware/beeware.github.io/pull/798) to the BeeWare website.
- We [added Vietnamese](https://github.com/beeware/beeware.github.io/pull/772) and [Tamil](https://github.com/beeware/beeware.github.io/pull/797) translations of the website.

Much of this work is due to the contributions of members of the BeeWare community. Thanks to <nospell>Abdo ([@abdnh](https://github.com/abdnh)), Aniruddha Nalawade ([@aniruddhanalawade24-beep](https://github.com/aniruddhanalawade24-beep)), Christian Clauss ([@cclauss](https://github.com/cclauss)), [@haikesan](https://github.com/haikesan), Haya Asif ([@haya-asif](https://github.com/haya-asif)), John ([@johnzhou721](https://github.com/johnzhou721)), Kevin Turcios ([@KRRT7](https://github.com/KRRT7)), Labib Bin Salam ([@Labib-Bin-Salam](https://github.com/Labib-Bin-Salam)), Luis Gómez Gutiérrez ([@lucuma13](https://github.com/lucuma13)), Luis Palacios ([@moondial-pal](https://github.com/moondial-pal)), Oliver Leigh ([@Oliver-Leigh](https://github.com/Oliver-Leigh)), Sai Asish Y ([@SAY-5](https://github.com/SAY-5)), Shannon ([@shannonmcin](https://github.com/shannonmcin)), sky ([@skyswordw](https://github.com/skyswordw)), Darryl Wang ([@Tridwoxi](https://github.com/Tridwoxi)), Yousuf Khan ([@Yousuf24100286](https://github.com/Yousuf24100286)), and KBS ([@youdie006](https://github.com/youdie006))</nospell> for their code and documentation contributions this month.

## What's next?

We're currently doing our planning for Q3; we'll be publishing those plans in the coming weeks. However, it's safe to assume that a lot of our time will be consumed with preparations for the Python 3.15 release in October. The availability of official iOS installers will require some changes to Briefcase; the annual cycle of Android Studio releases will also require testing and verification. There are also some lingering issues with GitHub Actions macOS testing and macOS 26 support that we need to address. Lastly, we're hoping to spend some time focusing on security, adding download checksum validation to Briefcase, and possibly adding SBOM support for CPython's iOS and Android releases.

We'll be at EuroPython in July, where [Malcolm Smith is presenting on supporting iOS and Android in Python packages](https://ep2026.europython.eu/session/supporting-android-and-ios-in-your-python-package); we'll also be at PyCon AU, where [Russell Keith-Magee will be speaking about packaging Python code for distribution](https://2026.pycon.org.au/schedule/AVCYHU/), and [Kattni will be speaking about switching from Sphinx to Markdown](https://2026.pycon.org.au/schedule/ZYSPB3/). You can also [Join us on Discord on July 9 at 11PM UTC (7PM EDT, 4PM PDT, 9AM AEST)](https://discord.gg/aH92JFNX3?event=1509015071890870443).

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
