---
title: August 2026 Status Update
date: 2026-09-01
authors:
- freakboy3742
categories:
- Buzz
---

In August, we made some major improvements hardening the security of BeeWare's tools, and attended PyCon AU 2026.

<!-- more -->

## What we've done

- We attended [PyCon AU 2026](https://2026.pycon.org.au), where we presented two talks and a workshop. Videos of the talks should be [available on YouTube](https://www.youtube.com/pyconau) in the very near future.
- We added [support for using Conda as an environment manager](https://github.com/beeware/briefcase/pull/2972) to Briefcase.
- We added [hash verification for all of Briefcase's tool downloads](https://github.com/beeware/briefcase/pull/2982) and [template downloads](https://github.com/beeware/briefcase/pull/2985).
- We added [support for signing Linux system packages with GPG identities](https://github.com/beeware/briefcase/pull/2973).
- We [ensured that Briefcase generates valid SPDX license identifiers for Proprietary and Other license options](https://github.com/beeware/briefcase/pull/3021).
- We [improved the error messages shown when an Android app fails to install](https://github.com/beeware/briefcase/pull/2949).
- We [updated the Android Gradle template to target API level 36](https://github.com/beeware/briefcase-android-gradle-template/pull/127), keeping apps compliant with the Google Play requirements that come into force at the end of August.
- We [added signal handler initialization to the iOS, Linux, macOS and Windows templates](https://github.com/beeware/briefcase-iOS-Xcode-template/pull/79).
- We [corrected macOS toolbar handling in Toga](https://github.com/beeware/toga/pull/4635).
- We added [user-space path anchors (desktop, documents, downloads and pictures) to Toga's path API](https://github.com/beeware/toga/pull/4645).
- We [made Toga respect local environment configuration when determining app file storage on Linux and Windows](https://github.com/beeware/toga/pull/4606).
- We [improved the documentation of widget style properties](https://github.com/beeware/toga/pull/4573).
- We [fixed variable substitution in `python3.pc` for Android in CPython](https://github.com/python/cpython/pull/155111).
- We [updated the Android Python versions and improved Meson tests in `cibuildwheel`](https://github.com/pypa/cibuildwheel/pull/2962).
- We [modified the way SQLite is compiled for Android to better match CPython's requirements](https://github.com/beeware/cpython-android-source-deps/pull/10).
- We [fixed the display of 404 page assets on Read the Docs](https://github.com/beeware/beeware-docs-tools/pull/267).
- We [corrected an issue with switching languages in BeeWare documentation content](https://github.com/beeware/beeware-docs-tools/pull/268).
- We continued hardening our GitHub Actions workflows, adding [`zizmor` security scanning across many of our repositories](https://github.com/beeware/beeware/pull/634), and [consolidating our Dependabot configuration with cool down periods and multi-ecosystem grouping](https://github.com/beeware/Python-Apple-support/pull/362).
- We [added verbose Briefcase logging to debug-mode CI reruns](https://github.com/beeware/.github/pull/392).
- We [refreshed the project configuration for Colosseum](https://github.com/beeware/colosseum/pull/219),
- We [did some spring-cleaning of Cricket](https://github.com/beeware/cricket/pull/104), getting the project running on a recent version of Toga.

Much of this work is due to the contributions of members of the BeeWare community. Thanks to <nospell>Rahul Patel ([@100jinwoo001](https://github.com/100jinwoo001)), Alex V ([@AlexVerrico](https://github.com/AlexVerrico)), Aruna Selvam ([@Aruna-Mani](https://github.com/Aruna-Mani)), Aronnax ([@aronnaxlin](https://github.com/aronnaxlin)), Ashton Lane ([@Ashton321](https://github.com/Ashton321)), Dipendra Paudel ([@BabuDip](https://github.com/BabuDip)), [@bilgituncay](https://github.com/bilgituncay), DawnWang ([@dawnwang3692](https://github.com/dawnwang3692)), Jainam h.maru ([@Dev9269](https://github.com/Dev9269)), [@Georgefifth](https://github.com/Georgefifth), Ivan Shamoon ([@IvanShamoon](https://github.com/IvanShamoon)), Jenish Gajera ([@jenish0908](https://github.com/jenish0908)), John ([@johnzhou721](https://github.com/johnzhou721)), Jasmeen Kaur ([@KAUR1984](https://github.com/KAUR1984)), Loi Nguyen ([@lntutor](https://github.com/lntutor)), Mgs. Tabrani ([@mgstabrani](https://github.com/mgstabrani)), Luis Palacios ([@moondial-pal](https://github.com/moondial-pal)), Phyo Pyae Sone ([@phyodev](https://github.com/phyodev)), Nishchaya Sharma ([@shinzoxD](https://github.com/shinzoxD)), Siddhant Bayas ([@siddhant-bayas](https://github.com/siddhant-bayas)), Stan Ulbrych ([@StanFromIreland](https://github.com/StanFromIreland)), and Harsh Kumar ([@thisisharsh7](https://github.com/thisisharsh7))</nospell> for their code and documentation contributions this month.

## What's next?

In September, our focus will be on the upcoming Python 3.15 release. In addition to the basic housekeeping of updating CI configurations, we need to make some updates to support the latest Android SDKs, and get the `xbuild` tool to a point where it can be used to manage cross-platform builds. We're also hoping to contribute SBOM configurations for CPython on iOS and Android, as part of the wider ecosystem trend to clearly documenting upstream dependencies.

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
