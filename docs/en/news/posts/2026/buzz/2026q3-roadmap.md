---
title: 2026Q3 Roadmap
date: 2026-07-22
authors:
- freakboy3742
categories:
- Buzz
---

We've made a lot of progress in Q2. However, much of that progress wasn't in areas that we were fully anticipating, and we didn't make as much progress in some areas where we were hoping to. As always, this roadmap should be read as a guide to what we aim to focus on over the coming quarter, rather than a hard commitment to features that will be made available on a specific deadline.

<!-- more -->

## Q2 progress

In Q2, we were able to make a number of key improvements to Briefcase's Windows packaging tools. We added support for Windows on ARM64; and we added a number of features to MSI installers, including improved customization options for installers, pre-install checks for .NET and minimum Windows versions, options for creating desktop shortcuts, and improved behavior for post-install and pre-uninstall scripts.

We're most of the way through a major rework of Briefcase's environment handling. This will allow us to provide options for using `uv` and `conda` for building Briefcase apps, and will provide more repeatable environments for app creation. This will form the basis of work required to support iOS on Python 3.15, and will provide a foundation for supporting lock files. We're expecting this work to be completed in the coming weeks.

We also launched our first (and second!) community call. We're hoping to maintain a monthly cadence on those calls on the second Thursday of the month. That call occurs at a time that isn't really convenient for Europe; once we've got the format established, we're hoping to add a second call to provide an opportunity for European users to participate.

Unfortunately, we didn't make much progress on the "Big Picture" widgets in Toga. There's an in-progress branch for some of the refactoring needed to support this work, but that work is very preliminary at this stage. We were also unable to make any progress on live reloading for iOS apps.

However, we have been able to make a lot of unanticipated improvements. We've made a number of key improvements to Briefcase's macOS 26 support, including some major changes to the way logs are handled, and resolving a long standing issue with the stability of the iOS testing environment on GitHub Actions. We've made some significant improvements to Briefcase's publication commands, making the process of publishing macOS apps in a CI environment much easier. We've resolved some long-standing issues with Windows event loop integration in Toga, and completed a major reorganization of Toga's Canvas API to provide better alignment with the HTML5 canvas API.

We've also been able to finally land support for both Android and iOS in NumPy - both are now Tier 3 supported platforms in NumPy. This is the culmination of work that has taken over a year, and required updates in a huge number of projects, including `cibuildwheel`, `meson`, and `meson-python`.

The discrepancy between our Q2 Roadmap goals and our Q3 goals is primarily caused by the nature of Open Source development. In a commercial environment, it's possible to have a relatively clear picture of the available resources and priorities. While unexpected events do sometimes alter plans, those events are just that - extraordinary. In an Open Source project, they're *completely* ordinary. We're constrained by the resources that are volunteered by contributors, and the areas where those contributors focus their contributions. That makes the planning process much less predictable.

## Q3 priorities

In Q3, our primary focus will be on supporting the upcoming Python 3.15 release. The inclusion of official iOS binaries in Python 3.15 requires some small changes in how Briefcase builds iOS applications; we're hoping those changes will also be accepted as part of `cibuildwheel`. On the Android side, there's updates required to add support for the Android 36 SDK. There's also updates and testing required to support Python 3.15 for macOS, Windows and Linux; plus updates to our CI configuration to support new images (like Ubuntu 26.04), and migrate off older images (like macOS 14).

We're also going to spend some time improving the security posture of BeeWare's tools. At present, Briefcase doesn't perform any validation of downloads. We're planning to add hash-based download validation, as well as configuration options that completely prevent Briefcase from initiating downloads so that security hardened environments are able to audit what is being downloaded. Although we're tackling this to provide more secure app builds, the same approach can be used to improve the experience in tutorials by providing a mechanism to "bootstrap" a Briefcase environment when download bandwidth is limited.

We will also be attending [PyCon AU](https://2026.pycon.org.au), where we'll be presenting a [workshop on building cross-platform GUI apps](https://2026.pycon.org.au/schedule/H33RW8/), plus talks on [mechanisms for distributing Python code](https://2026.pycon.org.au/schedule/AVCYHU/) and [switching your project documentation from Sphinx to Markdown](https://2026.pycon.org.au/schedule/ZYSPB3/). We'll also be there for [the Development Sprint day](https://2026.pycon.org.au/schedule/sunday/). If you're able to make it, make sure you say hello!

## Longer term goals

In Q1, we published a plan for "Big Picture" app development. Executing on that plan remains our primary long term goal. We're hoping that toward the end of this year, we'll be able to focus more on features in Toga that enable users to build interesting mobile and desktop apps. As part of that effort, we're hoping to show off more apps ourselves - both to demonstrate the capabilities of BeeWare's tools, and to provide example apps that others can use to learn how to use BeeWare's tools better.

Along the way, we're not going to ignore Briefcase. Briefcase already solves a number of key distribution problems in the Python ecosystem; but there's a lot of opportunity to further improve alignment with Python ecosystem standards, simplify the process of developing apps, and streamline publication of apps into app stores.
