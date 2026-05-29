---
title: May 2026 Status Update
date: 2026-06-01
authors:
- freakboy3742
categories:
- Buzz
---

May was dominated by [PyCon US](https://us.pycon.org/2026/), where the BeeWare team ran another successful sprint, resulting in a number of improvements - many from first time contributors.

<!-- more -->

## What we've done

- We presented 2 main track talks at PyCon US - one on [mechanisms for distributing Python code](https://us.pycon.org/2026/schedule/presentation/36/), and one on [switching your project documentation from Sphinx to Markdown](https://us.pycon.org/2026/schedule/presentation/6/). We also presented at the [Web Assembly Summit](https://us.pycon.org/2026/events/webassembly-summit/), and [Packaging Summit](https://us.pycon.org/2026/events/packaging-summit/).
- We rolled out a series of updates to our GitHub Action workflows, simplifying our use of Dependabot, and adding some improvements to help users [identify if they haven't filled out our PR template](https://github.com/beeware/.github/pull/357) or [provided a Towncrier change note](https://github.com/beeware/.github/pull/361).
- We adopted the use of our new warning banner helper [throughout the Briefcase repository](https://github.com/beeware/briefcase/pull/2842), replacing the existing banners.
- We [improved Briefcase's validation of bundle identifiers](https://github.com/beeware/briefcase/pull/2825), allowing single-dot bundle IDs while still rejecting invalid ones.
- Now that [Python.net supports Python 3.14](https://github.com/pythonnet/pythonnet/issues/2610), we have [removed the warning in the BeeWare tutorial that advised against using Python 3.14 on Windows](https://github.com/beeware/beeware-tutorial/pull/78).
- We modified [Toga's `Canvas` widget to expose drawing-context attributes (`fill_style`, `stroke_style`, `line_width`, `line_dash`) along with `save`/`restore` methods](https://github.com/beeware/toga/pull/4332), continuing the alignment with the HTML5 Canvas API, and completed a [comprehensive revamp of the documentation of the `Canvas` widget](https://github.com/beeware/toga/pull/4362).
- We implemented [dark mode detection in Toga for iOS, web, and Windows](https://github.com/beeware/toga/pull/4408).
- We addressed some [reliability problems with Toga's app-level dialogs on macOS 26](https://github.com/beeware/toga/pull/4363).
- We modified Toga's [`Window` initialization process to ensure event handlers exist before the underlying widget is constructed](https://github.com/beeware/toga/pull/4359).
- We added [keyboard toggling for nodes in the Toga's WinForms Tree widget](https://github.com/beeware/toga/pull/4360).
- We [modified the handling of static HTML content in the Android `WebView`](https://github.com/beeware/toga/pull/4410), fixing a rendering problem observed when content contained characters such as `#`.
- We [improved Toga's GTK `MapView` handling of null values](https://github.com/beeware/toga/pull/4379).
- We corrected an issue with the Toga testbed app that caused [tests to fail if the user had multiple monitors](https://github.com/beeware/toga/pull/4428).
- We [documented the limitations of `OptionContainer` on mobile platforms](https://github.com/beeware/toga/pull/4369).
- We ensured Toga's codebase [checks for default encoding warnings](https://github.com/beeware/toga/pull/4365), and corrected some examples where encoding wasn't being explicitly specified.
- We [improved the resilience of Toga's `WebView` tests under Qt](https://github.com/beeware/toga/pull/4424).
- We [migrated Briefcase's project template to include a Markdown README](https://github.com/beeware/briefcase-template/pull/258).
- We [improved the BeeWare overview page with details about the platforms that BeeWare supports](https://github.com/beeware/beeware.github.io/pull/783).
- We [corrected a configuration issue that broke compilation of Python for iOS on macOS 26](https://github.com/python/cpython/pull/150444).
- We landed [the `cibuildwheel` improvements needed for building NumPy and related packages on Android](https://github.com/pypa/cibuildwheel/pull/2695), and [added Android support to `auditwheel`](https://github.com/pypa/auditwheel/pull/643). Together, these are the foundation that will let `cibuildwheel` build a much wider range of scientific-Python wheels for Android.

Much of this work is due to the contributions of members of the BeeWare community, many of these users contributed at the PyCon US Sprints. Thanks to <nospell>Abdo ([@abdnh](https://github.com/abdnh)), Abdur-Rahmaan Janhangeer ([@Abdur-rahmaanJ](https://github.com/Abdur-rahmaanJ)), [@AJTheDataGuy](https://github.com/AJTheDataGuy), [@albertchae](https://github.com/albertchae), Aman Sachan ([@AmSach](https://github.com/AmSach)), Aqil Aziz ([@aqilaziz](https://github.com/aqilaziz)), [@atuseract](https://github.com/atuseract), Audrey Dang ([@audreydng](https://github.com/audreydng)), Campbell ([@ceggy91](https://github.com/ceggy91)), [@changquan](https://github.com/changquan), Andy P Fundinger ([@Ciemaar](https://github.com/Ciemaar)), [@drewRB](https://github.com/drewRB), Chris Patti ([@feoh](https://github.com/feoh)), Grant Wang ([@gwdio](https://github.com/gwdio)), Michael Wilson ([@hyperboloid](https://github.com/hyperboloid)), Ian Dolge ([@iandolge](https://github.com/iandolge)), Joel Peter ([@joelpeter-c](https://github.com/joelpeter-c)), John ([@johnzhou721](https://github.com/johnzhou721)), Jorge ([@jvigueras](https://github.com/jvigueras)), [@lihua-xinghun](https://github.com/lihua-xinghun), Matthew Wygal ([@matthew-wy](https://github.com/matthew-wy)), Miro ([@Mirochill](https://github.com/Mirochill)), [@mrds555](https://github.com/mrds555), Matt Van Horn ([@mvanhorn](https://github.com/mvanhorn)), [@Nando301](https://github.com/Nando301), Oliver Leigh ([@Oliver-Leigh](https://github.com/Oliver-Leigh)), Taiwo Osunrinde ([@osunrinde](https://github.com/osunrinde)), Puneet Dixit ([@puneetdixit200](https://github.com/puneetdixit200)), Robert J Spencer ([@Rjvs](https://github.com/Rjvs)), [@Rowlando13](https://github.com/Rowlando13), Shannon ([@shannonmcin](https://github.com/shannonmcin)), Darryl Wang ([@Tridwoxi](https://github.com/Tridwoxi)), [@tylerboutwell](https://github.com/tylerboutwell), Vinicius Gubiani Ferreira ([@vinigfer](https://github.com/vinigfer)), and David_C ([@YuDavidCao](https://github.com/YuDavidCao))</nospell> for their code and documentation contributions this month.

## What's next?

On the technical front, in the coming month, we'll also be looking into options for updating code in a running app; and continuing work on the "big picture" app navigation plan published earlier in the year. If time permits, we'll begin investigations into the use of Conda environments in Briefcase apps.

We're also planning to step up our efforts to build the BeeWare community. We've developed a reputation at PyCon US for running extremely effective sprints; but we need to do more of that outreach for people who can't make it to PyCon. We've already begun doing an audit of our outstanding issues in the hope of curating a more actionable list of work for contributors; and we're going to start being more active on social media, including reaching out to more social media channels. We're also going to host our first Community Call - a live video event where members of the core team and community members can share what they've been working on. [Join us on Discord on June 11 at 11PM UTC (7PM EDT, 4PM EDT, 9AM AEST)](https://discord.gg/U6RfbGDN?event=1509015071890870443) (and yes - we're planning to add calls at other times more convenient for European and Asian audiences).

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [contribution guide](https://beeware.org/contributing/guide/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
