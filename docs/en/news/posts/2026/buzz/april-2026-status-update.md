---
title: April 2026 Status Update
date: 2026-05-01
authors:
- freakboy3742
categories:
- Buzz
---

April saw some extremely important improvements to BeeWare's Windows support, and some important new policy decisions.

<!-- more -->

## What we've done

- We formally adopted [an AI and Autonomous code contribution policy](https://github.com/beeware/.github/pull/328). This policy is neutral on whether AI tools can be used for contribution, but clearly places the responsibility on a human contributor to take full responsibility for the output of any tool they use, and to declare if AI tooling *has* been used.
- As part of adopting a format AI usage policy, we've added an `AGENTS.md` file, and a [Spec Kit constitution](https://github.github.com/spec-kit/) to [Briefcase](https://github.com/beeware/briefcase/pull/2733), [Toga](https://github.com/beeware/toga/pull/4344), and [Rubicon ObjC](https://github.com/beeware/rubicon-objc/pull/751). We expect we'll be tweaking and tuning those configurations over time as we discover what does (and doesn't) work. If you've got experience in developing these foundational AI configuration files, we'd appreciate any suggestions or feedback you may have.
- You can now build [native ARM64 Windows binaries and installers with Briefcase](https://github.com/beeware/briefcase/pull/2797).
- We added support for [detecting if .NET is installed as part of a Windows MSI installer](https://github.com/beeware/briefcase-windows-VisualStudio-template/pull/90).
- We added the ability to [customize the banner and background images in an MSI installer](https://github.com/beeware/briefcase-windows-VisualStudio-template/pull/91).
- We added a utility method for formatting the [banner-style warning messages that Briefcase generates](https://github.com/beeware/briefcase/pull/2563). We haven't rolled out the usage of this banner across all parts of the Briefcase codebase, but it will allow us to improve consistency in the display of warning output.
- We modified the new project wizard to [improve the visibility of known third-party bootstraps](https://github.com/beeware/briefcase/pull/2640).
- We added a runtime checks for [using an x86-64 Python interpreter on an Apple Silicon Mac](https://github.com/beeware/briefcase/pull/2760). This configuration can cause issues when trying to run an iOS simulator.
- We [added the ability to create a "skinless" Android emulator](https://github.com/beeware/briefcase/pull/2788). This is mostly useful for CI configurations, where the extra visual detail doesn't help, but downloading the skin will sometimes fail due to rate limits imposed by Google's servers.
- We [improved the verification of installed Android SDK images](https://github.com/beeware/briefcase/pull/2796).
- We [added support for the use of .NET Core 10 in Toga](https://github.com/beeware/toga/pull/4331). This was primarily required to support WinForms on ARM64, but it also means features like dark mode are now possible on WinForms.
- We performed a [major refactor of the internals of the Canvas widget](https://github.com/beeware/toga/pull/4328), and modified the Canvas API to [align better with JavaScript's HTML5 Canvas API](https://github.com/beeware/toga/pull/4330).
- We migrated Toga's Web backend to use [WebAwesome, rather than Shoelace](https://github.com/beeware/toga/pull/4262). WebAwesome is effectively "Shoelace 3", after the Shoelace project was adopted by the FontAwesome team.
- We added a [full implementation of `DetailedList` on WinForms](https://github.com/beeware/toga/pull/4319). This was the last widget in Beta status on WinForms - WinForms is now widget complete!
- We corrected some crashes that could occur [on macOS when clicking on empty rows of a table, or the table header row](https://github.com/beeware/toga/pull/4265).
- We corrected an unusual bounce when [calling `scroll_to_bottom()` on a WinForms `MultilineText` widget](https://github.com/beeware/toga/pull/4276).
- We [made the definition of accessors optional when defining sources](https://github.com/beeware/toga/pull/4277).
- We added support for [fonts that have been system-registered on iOS and macOS](https://github.com/beeware/toga/pull/4314).
- We [normalized the feature set of the CPython Android build script with other platform build scripts](https://github.com/python/cpython/pull/146451).
- We completed the migration of [CPython Android build tooling to the Platforms folder](https://github.com/python/cpython/pull/148282).
- We [increased the RAM available to the Python Android testbed](https://github.com/python/cpython/pull/148054) to accommodate more demanding test suites.
- We submitted [updates to cibuildwheel](https://github.com/pypa/cibuildwheel/pull/2695) to support Android packages that use Fortran, NumPy's C API, and external libraries bundled with auditwheel.

Much of this work is due to the contributions of members of the BeeWare community. Thanks to <nospell>Abdo ([@abdnh](https://github.com/abdnh)), Keyang Zheng ([@albuszheng](https://github.com/albuszheng)), Filip Łajszczak ([@filiplajszczak](https://github.com/filiplajszczak)), John ([@johnzhou721](https://github.com/johnzhou721)), Luis Palacios ([@moondial-pal](https://github.com/moondial-pal)), Matt Van Horn ([@mvanhorn](https://github.com/mvanhorn)), [@Oliver-Leigh](https://github.com/Oliver-Leigh), [@otekraden](https://github.com/otekraden), Robert Kirkman ([@robertkirkman](https://github.com/robertkirkman)), Matt Cooper ([@vtbassmatt](https://github.com/vtbassmatt))</nospell> for their code and documentation contributions this month.

Special thanks go to <nospell>Scott Halgrim ([@shalgrim](https://github.com/shalgrim)), Juan ([@Pulga8](https://github.com/Pulga8)), and Vui Nguyen ([@vuinguyen](https://github.com/vuinguyen))</nospell> who were contributing to BeeWare as part of Session 6 of the [Djangonaut Space program](https://djangonaut.space). Go Team Mercury!

## What's next?

A lot of May will be spent preparing for and attending [PyCon US](https://us.pycon.org/2026/schedule/presentation/36/). We're presenting talks on [mechanisms for distributing Python code](https://us.pycon.org/2026/schedule/presentation/36/) and [switching your project documentation from Sphinx to Markdown](https://us.pycon.org/2026/schedule/presentation/6/). We'll be there for [both days of the sprints](https://us.pycon.org/2026/events/dev-sprints/), hosting some open spaces (watch the boards at the venue for details), attending the community showcase, as well as participating in a other events and generally lurking around the hallways. Tickets are still available - if you're around, come say hi! We're actively looking for stories of how you're using BeeWare, or how you'd like to use BeeWare.

In what time that remains in the month, we'll be focused primarily on Briefcase, adding more customizations for MSI installers, and starting to experiment with mechanisms for improving the development experience for mobile apps.

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
