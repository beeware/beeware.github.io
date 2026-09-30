---
title: September 2026 Status Update
date: 2026-10-01
authors:
- freakboy3742
categories:
- Buzz
---

In September, we've been focused on preparing for the impending release of Python 3.15, as well as adapting to updates in Xcode and Android Studio.

<!-- more -->

## What we've done

- We dropped support for Python 3.10 across BeeWare's projects and templates, adding support for Python 3.15 in its place.
- We [prepared for a new Chaquopy release](https://github.com/chaquo/chaquopy/milestone/7). The actual release is dependent on the release of CPython 3.15.0, and will also include support for the latest Android Studio and Android SDK releases.
- We substantially improved [`xbuild`](https://github.com/beeware/xbuild), BeeWare's PEP 517 build frontend for cross-compiling wheels. The updates add [the ability to automatically fetch a Python install for a target platform](https://github.com/beeware/xbuild/pull/81), [a full test suite](https://github.com/beeware/xbuild/pull/82), and [an `xpython` command for running arbitrary code in a cross-platform environment](https://github.com/beeware/xbuild/pull/90).
- We [switched Briefcase's iOS support to use `xbuild` when creating cross-platform virtual environments](https://github.com/beeware/briefcase/pull/3071). This also allowed switching to using the official CPython iOS binary release.
- We [modified Briefcase to support changes in Xcode 27, including the new Device Hub](https://github.com/beeware/briefcase/pull/3059).
- We [added hash verification for Briefcase's asset cache](https://github.com/beeware/briefcase/pull/3045), protecting against cache poisoning if a build machine is compromised.
- We [added support for limiting Windows MSI installer options to a specific install scope](https://github.com/beeware/briefcase/pull/3022).
- We [added automatic device selection for iOS](https://github.com/beeware/briefcase/pull/3032) and [Android](https://github.com/beeware/briefcase/pull/3033), so `briefcase run` can select (and create, if needed) an appropriate default device without user intervention.
- We [migrated Briefcase's use of `httpx` to `httpx2`](https://github.com/beeware/briefcase/pull/3056), following the shift in maintenance focus in the HTTP client ecosystem.
- We [dropped Briefcase's built-in support for Pygame](https://github.com/beeware/briefcase/pull/3030), in favor of the actively maintained Pygame-CE, which ships its own Briefcase plugin.
- We [updated Toga iOS's backend to support the Scene-based application life cycle](https://github.com/beeware/toga/pull/4696) required by the iOS 27 SDK.
- We [migrated Toga's GTK, Cocoa, WinForms and Textual backends to use `platformdirs` for app-specific paths](https://github.com/beeware/toga/pull/4682), improving support for unusual user-space platform configurations.
- We continued hardening our GitHub Actions workflows, adopting `zizmor` and adding Dependabot cool-off delays on several repositories.
- We [fixed a bug where `encoding_for_ctype()` raised an undocumented `AttributeError` instead of `ValueError` for unknown C types](https://github.com/beeware/rubicon-objc/pull/827).
- We [ensured Briefcase doesn't derive an invalid Python keyword as an app's class name](https://github.com/beeware/briefcase/pull/3057), [rejected bundle identifiers containing a trailing newline](https://github.com/beeware/briefcase/pull/3054), and [logged captured output when a non-streamed subprocess call fails](https://github.com/beeware/briefcase/pull/3036).
- We [switched the Windows Visual Studio template to be compatible with Visual Studio 2026](https://github.com/beeware/briefcase-windows-VisualStudio-template/pull/124).
- We [refreshed Toga's iOS testbed](https://github.com/beeware/toga/pull/4720), expanding the range of test devices and configurations where the testbed suite will pass.
- We [added a documentation guide covering the expired system certificate issue affecting macOS code signing](https://github.com/beeware/briefcase/pull/3060).
- We [highlighted the existence of project-specific contribution guides at the top of BeeWare's general contribution guide](https://github.com/beeware/beeware.github.io/pull/828).

Much of this work is due to the contributions of members of the BeeWare community. Thanks to <nospell>Abdo ([@abdnh](https://github.com/abdnh)), Deepak Thorat ([@deepak25000000](https://github.com/deepak25000000)), Felipe Medici ([@femedici](https://github.com/femedici)), Hyuri ([@hyuri](https://github.com/hyuri)), Jenish Gajera ([@jenish0908](https://github.com/jenish0908)), Joshua King ([@jkingok](https://github.com/jkingok)), Mgs. Tabrani ([@mgstabrani](https://github.com/mgstabrani)), Roshan Ramani ([@rawsun007](https://github.com/rawsun007)), [@Rayan-and-beyond](https://github.com/Rayan-and-beyond), Revar Desmera ([@revarbat](https://github.com/revarbat)), Tanya Schlusser ([@tanyaschlusser](https://github.com/tanyaschlusser)), [@TianHengZhuang](https://github.com/TianHengZhuang), and Xiaowen ([@Xiaowen-Yang](https://github.com/Xiaowen-Yang))</nospell> for their code and documentation contributions this month.

## What's next?

The final release of 3.15.0 is days away; once that release is out, we'll be able to make a Chaquopy, Briefcase and Toga release. We also want to explore whether `cibuildwheel` can make use of `xbuild`.

Once that work is completed, we're expecting to turn our focus back to Toga. We've made *some* progress against the "big picture app navigation" plan that we published at the start of the year; with the 3.15 release behind us, we can now focus on delivering that plan, and adding other exciting features to Toga.

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
