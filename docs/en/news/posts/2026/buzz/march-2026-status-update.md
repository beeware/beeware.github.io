---
title: March 2026 Status Update
date: 2026-03-31
authors:
- freakboy3742
categories:
- Buzz
---

March has seen some big improvements in Briefcase, as well as some major discussions of design and policy issues in the rest of the project.

<!-- more -->

## What we've done

- We released [Briefcase 0.4.0](https://pypi.org/project/briefcase/0.4.0/)! This release makes a major change to how development mode operates for apps, isolating the dependencies of the app being developed from the environment that is running Briefcase.
- We upgraded Briefcase to use [PEP639 license format](https://github.com/beeware/briefcase/pull/2732).
- We added support for [dynamic PEP 621 project metadata](https://github.com/beeware/briefcase/pull/2772). This allows apps to have their version number configured by version control tags.
- We addressed [CVE-2026-33430](https://github.com/beeware/briefcase/security/advisories/GHSA-r3r2-35v9-v238), a security issue which allowed for potential privilege escalation in Windows MSI installers.
- We added the ability to [configure the Android ABIs](https://github.com/beeware/briefcase/pull/2723) that are targeted as part of a Briefcase build.
- We made [a retry mechanism to make project cleanup mechanisms more robust on Windows](https://github.com/beeware/briefcase/pull/2725).
- We started experimenting with the use of `ty` to enforce type compliance in the Briefcase codebase.
- We added validation of [MIME type definitions on document types](https://github.com/beeware/briefcase/pull/2738).
- We modified MSI installers to [allow install scripts to inherit elevated privileges of the installing user](https://github.com/beeware/briefcase/pull/2755).
- In order to address some emerging issues and questions about the use of AI tools in contributions to BeeWare, we [discussed the possible adoption of an AI contribution policy](https://github.com/beeware/beeware/discussions/621), and then [published a draft policy](https://github.com/beeware/.github/pull/328) and [drafted a set of agent guides for Briefcase](https://github.com/beeware/briefcase/pull/2733).
- We published a design plan for the next collection of Toga widgets, governing ["Big Picture" app navigation](https://github.com/beeware/toga/discussions/4271).
- We added a [FastAPI bootstrap for Toga's Positron plugin](https://github.com/beeware/toga/pull/4156).
- We experimented with a [PyScript bootstrap for Positron](https://github.com/beeware/toga/pull/4296). This work is still dependent on some experimental tools, but we hope we'll be able to release this in the near future.
- We added [support for column resizing in Qt tables](https://github.com/beeware/toga/pull/4189).
- We modified the API for `Table` and `Tree` to [allow explicit definition of columns](https://github.com/beeware/toga/pull/4199). This provides a much more flexible mechanism for configuring the display of `Table` and `Tree` widgets.
- We added a mechanism for [lazy loading and dynamic registration of widgets](https://github.com/beeware/toga/pull/4205). In addition to reducing app startup time, this allows third party libraries to provide widget implementations that Toga doesn't provide, and to register entirely new widget types.
- We added a [Switch widget for Toga's Textual backend](https://github.com/beeware/toga/pull/4228).
- We added a [Tree widget to the WinForms backend](https://github.com/beeware/toga/pull/4235). This has one of the more notable missing widgets from Toga's API.
- We modified how notifications from data sources are handled so that [a `ListSource` can be a listener on other sources](https://github.com/beeware/toga/pull/4237).
- We corrected a bug in Toga's handling of presentation mode that would [prevent more than one window from being put into presentation mode.](https://github.com/beeware/toga/pull/4259)
- We [migrated Rubicon ObjC's test suite to pytest](https://github.com/beeware/rubicon-objc/pull/722), and performed a [large refactor of the tests](https://github.com/beeware/rubicon-objc/pull/730) to break up some large test files.
- We contributed a [migration of CPython's iOS build code to the new "Platforms" directory](https://github.com/python/cpython/pull/146497), and reviewed a [comparable change for Emscripten](https://github.com/python/cpython/pull/146198). CPython has grown a number of new platforms in recent releases; this refactor is an organizational change that allows all platform-specific build tooling to be in a single subdirectory, rather than having lots of top-level directories. A similar set of patches for Android are in development.
- We made some improvements to the CPython [iOS build script](https://github.com/python/cpython/pull/146447) and [Android build script](https://github.com/python/cpython/pull/146451) for consistency with other platform tools.
* We submitted Android support to [auditwheel](https://github.com/pypa/auditwheel/pull/643) and [meson-python](https://github.com/mesonbuild/meson-python/pull/824), and enabled automated Android testing of [pybind11](https://github.com/pybind/pybind11/pull/6001).
- After the launch of the updated BeeWare website at the end of last month, we've addressed a number of small cosmetic, linking and translation issues that were reported, including [improvements to the layout of upcoming events](https://github.com/beeware/beeware.github.io/pull/761), [improvements in mobile rendering](https://github.com/beeware/beeware.github.io/pull/760), and [ensuring as much content as possible can be translated](https://github.com/beeware/beeware.github.io/pull/759).
- We added sections to the contribution guide on [retrieving repository tags](https://github.com/beeware/beeware-docs-tools/pull/190), and [using the `gh` tool to open issues](https://github.com/beeware/beeware-docs-tools/pull/196).
- We [resolved an issue with the preservation of spaces in code blocks](https://github.com/beeware/beeware-docs-tools/pull/192) when copying sample code content.
- We optimized the build of the tutorial to [build all languages in a single pass](https://github.com/beeware/beeware-tutorial/pull/58).
- We [replaced the use of a JSON API with an internal link under our control](https://github.com/beeware/beeware-tutorial/pull/65).

Much of this work is due to the contributions of members of the BeeWare community. Thanks to <nospell>[Mattijs Ugen (@akaIDIOT)](https://github.com/akaIDIOT), [Aleksei Pirogov (@astynax)](https://github.com/astynax), [Filip Łajszczak (@filiplajszczak)](https://github.com/filiplajszczak), [Johanan Oppong Amoateng (@JohananOppongAmoateng)](https://github.com/JohananOppongAmoateng), [John (@johnzhou721)](https://github.com/johnzhou721), [Robin (@lrandersson)](https://github.com/lrandersson), [lif (@majiayu000)](https://github.com/majiayu000), [@Oliver-Leigh](https://github.com/Oliver-Leigh), [@Pulga8](https://github.com/Pulga8), [Scott Halgrim (@shalgrim)](https://github.com/shalgrim), [Tom Arn (@t-arn)](https://github.com/t-arn), [Eyal Tabib (@tabibeyal)](https://github.com/tabibeyal), and [Zyad Haddad (@Trighap52)](https://github.com/Trighap52)</nospell> for their code and documentation contributions this month.

## What's next?

We'll be publishing our Q2 roadmap in a couple of weeks. In addition to some progress in Toga that is aligned with the design plans we laid out this quarter, we're hoping that Q2 will see some experimentation with how Briefcase can be used to improve the process of developing and deploying apps. The hope is by making some relatively small changes to how Briefcase starts mobile applications, we will be able to speed up the app development process, and enable some interesting use cases for deploying applications to mobile platforms.

We'll also be preparing for our attendance at [PyCon US](https://us.pycon.org/2026/schedule/presentation/36/). We're presenting talks on [mechanisms for distributing Python code](https://us.pycon.org/2026/schedule/presentation/36/) and [switching your project documentation from Sphinx to Markdown](https://us.pycon.org/2026/schedule/presentation/6/). We'll be there for [both days of the sprints](https://us.pycon.org/2026/events/dev-sprints/), as well as participating in a number of other events and generally lurking around the hallways.

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
