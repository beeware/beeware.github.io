---
title: October 2026 Status Update
date: 2026-11-02
authors:
- freakboy3742
categories:
- Buzz
---

October has been a busy month of releases and security updates - but we also found time to add some notable improvements to BeeWare.

<!-- more -->

## What we've done

- We published [Briefcase 0.4.7](https://github.com/beeware/briefcase/releases/tag/v0.4.7) - this is a security update addressing the [<nospell>eMudhra</nospell> Intermediate CA exploit](https://emudhra.we-have-a-problem.com), and a [Windows path traversal issue](https://github.com/beeware/briefcase/security/advisories/GHSA-j2qc-j92x-qqhj) that was reported independently. These are both high severity security issues; we strongly advice all users to upgrade if they haven't already. This also required the release of [Chaquopy 17.2.0](https://github.com/chaquo/chaquopy/releases/tag/17.2.0).
- We published [Chaquopy 17.1.0](https://github.com/chaquo/chaquopy/releases/tag/17.1.0) and [Briefcase 0.4.6](https://github.com/beeware/briefcase/releases/tag/v0.4.6). These releases were primarily to add Python 3.15 support for Android, but also included a number of other improvements.
- We published [Toga 0.5.7](https://github.com/beeware/toga/releases/tag/v0.5.7), containing all the features from the last three months of Toga development.
- We attended the CPython Core Team summit in San Francisco. This gave us the opportunity to discuss goals and make plans for the Python 3.16 release, as well as making plans for formalizing some of the ad-hoc practices that have emerged in the Python ecosystem around cross-platform builds.
- We [contributed support for tvOS, visionOS and watchOS to CPython](https://github.com/python/cpython/pull/159944), upstreaming patches that BeeWare has maintained independently for some time.
- We [added support for free-threaded and debug builds of CPython on iOS](https://github.com/python/cpython/pull/159386).
- We contributed a fix to CPython that [disables `PIP_REQUIRE_VIRTUALENV` when updating certificates](https://github.com/python/cpython/pull/159214). Previously if you had a shell configuration that enabled this option, it was not possible to use the certificate update script that ships with the macOS Python installer.
- We optimized the CPython iOS testbed by [disabling the collection of test diagnostics](https://github.com/python/cpython/pull/159212). These test diagnostics are rarely useful in diagnosing Python issues, but can slow down the completion of a failing test suite by several minutes.
- We [added the ability for `ctypes` callbacks to return `struct` and `union` types](https://github.com/python/cpython/pull/157974), resolving a CPython issue that had been open since 2009. This will allow us to deprecate a monkey-patch that we've carried in Rubicon ObjC.
- We [contributed a patch for Android support in Pillow](https://github.com/python-pillow/Pillow/pull/10233).
- We published [`xbuild` 0.4.1](https://github.com/beeware/xbuild/releases/tag/v0.4.1). This is the first "ready for prime-time" release of `xbuild`, our suite of tools for managing cross-platform virtual environments. It includes a number of new features, including the ability to [automatically configure the environment for cross-platform builds](https://github.com/beeware/xbuild/pull/96), and [allowing the use of `xbuild` from inside an existing cross-platform environment](https://github.com/beeware/xbuild/pull/97).
- We modified `xbuild` to [allow the re-use of existing work directories](https://github.com/beeware/xbuild/pull/107),
- We added support for [`xbuild` to create virtual environments with `uv` or `virtualenv`](https://github.com/beeware/xbuild/pull/105),
- We [added Emscripten (Pyodide) support to `xbuild` and `xvenv`](https://github.com/beeware/xbuild/pull/111).
- We [added Android support for Python 3.11 and 3.12 to `xbuild`](https://github.com/beeware/xbuild/pull/108).
- We [added support for subprocesses](https://github.com/beeware/briefcase/pull/3077) to Briefcase apps on macOS, Windows, and Linux.
- We [added the ability to customize the completion screen of Windows MSI installers and uninstallers](https://github.com/beeware/briefcase/pull/3086).
- We [corrected the handling of MSI installers creating desktop shortcuts during silent installs](https://github.com/beeware/briefcase-windows-app-template/pull/126).
- We [modified Briefcase to use PEP 621 project names](https://github.com/beeware/briefcase/pull/3076), rather than requiring a separate `tool.briefcase.project_name` setting.
- We [added an actionable error message when Docker isn't available in WSL 2](https://github.com/beeware/briefcase/pull/3108).
- We [improved error handling when a Windows machine has the bootstrap binary for Visual Studio, but hasn't installed the Visual Studio IDE](https://github.com/beeware/briefcase/pull/3090).
- We added new [`toga-code-editor`](https://github.com/beeware/toga-code-editor) and [`toga-console`](https://github.com/beeware/toga-console) widgets. These widgets allow building apps that display code, or need to display console output.
- We modified Toga to [recognize official external widgets by their package metadata](https://github.com/beeware/toga/pull/4766).
- We [ensured that canvas resize events are only triggered once](https://github.com/beeware/toga/pull/4843), avoiding potential infinite recursion on macOS, iOS, Android and Qt.
- We [fixed a memory leak when loading images on GTK](https://github.com/beeware/toga/pull/4814).
- We [fixed a hang in GTK's `MultilineTextInput`](https://github.com/beeware/toga/pull/4743).
- We [made Pack layouts honor `display=none`, and corrected the handling of the `hidden` style argument on GTK3](https://github.com/beeware/toga/pull/4768).
- We [continued work on Toga's "Big Picture" app refactor](https://github.com/beeware/toga/pull/4605). The base refactor needed to add app scaffolds for macOS and iOS are nearing completion.
- We [prevented errors when clicking on non-data rows in macOS `Tree` widgets](https://github.com/beeware/toga/pull/4765).
- We [fixed Android `OptionContainer` content being hidden behind the tab bar](https://github.com/beeware/toga/pull/4738).
- We continued to [improve test coverage for Rubicon ObjC](https://github.com/beeware/rubicon-objc/pull/836).
- We [changed `dmgbuild` to create images without a partition map by default](https://github.com/dmgbuild/dmgbuild/pull/296), fixing builds that silently produced DMGs with missing files.
- We [improved `dmgbuild`'s handling of subprocess failures](https://github.com/dmgbuild/dmgbuild/pull/299).
- We [aligned the CLI detach retry default with the Python API](https://github.com/dmgbuild/dmgbuild/pull/294).
- We [added privacy-respecting analytics to BeeWare's websites](https://github.com/beeware/beeware-docs-tools/pull/278).
- We improved the reliability of our translation workflows, including [better handling of Weblate locking failures](https://github.com/beeware/beeware-docs-tools/pull/283) and [retries on server errors](https://github.com/beeware/beeware.github.io/pull/837).
- We continued hardening our GitHub Actions workflows, adding `zizmor` checks and Dependabot cool-off delays to several repositories.

Much of this work is due to the contributions of members of the BeeWare community. Thanks to <nospell>Rahul Patel ([@100jinwoo001](https://github.com/100jinwoo001)), [@aaravgauba](https://github.com/aaravgauba), Abdo ([@abdnh](https://github.com/abdnh)), [@cgkoutzigiannis](https://github.com/cgkoutzigiannis), Filip Łajszczak ([@filiplajszczak](https://github.com/filiplajszczak)), Julien ([@fjjjuv](https://github.com/fjjjuv)), [@fukalous](https://github.com/fukalous), Garvit Sharma ([@garvitshrma](https://github.com/garvitshrma)), [@Gise23](https://github.com/Gise23), Hiroshiba ([@Hiroshiba](https://github.com/Hiroshiba)), Hood Chatham ([@hoodmane](https://github.com/hoodmane)), Henrik ([@HT-573](https://github.com/HT-573)), John ([@johnzhou721](https://github.com/johnzhou721)), Mgs. Tabrani ([@mgstabrani](https://github.com/mgstabrani)), Rohan Singhvi ([@rsinghvi-maxon](https://github.com/rsinghvi-maxon)), Alex Shuvalov ([@skritosss](https://github.com/skritosss)), Skytuhua ([@Skytuhua](https://github.com/Skytuhua)), Volkan Gezer ([@vgezer](https://github.com/vgezer)), and Yanis ([@ynaamane](https://github.com/ynaamane))</nospell> for their code and documentation contributions this month.

## What's next?

With the 3.15 release finalized, we can turn our attention to other parts of the BeeWare ecosystem. We're expecting two major areas of focus.

The first is Toga. We have a backlog of PRs adding new widgets, including GTK4 support for a lot of widgets, and a bar code scanner widget for iOS. We're also hoping to be able to make significant progress on the scaffolding work that part of the "Big Picture" app refactor.

The second is the finalization of some packaging work that has been ongoing for the last 18 months. We want to get iOS and Android to Tier 2 support in NumPy; this would enable the upcoming NumPy 2.6 release will be able to include iOS and Android wheels for the first time. We'll also be working with the Pillow team to finalize the patch adding Android support.

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
