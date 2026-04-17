---
title: 2026Q2 Roadmap
date: 2026-04-20
authors:
- freakboy3742
categories:
- Buzz
---

Q1 has seen some significant improvements to Toga, Android packages, and a milestone for official iOS support. As always, this roadmap should be read as a guide to what we aim to focus on over the coming quarter, rather than a hard commitment to features that will be made available on a specific deadline.

<!-- more -->

## Q1 progress

The bulk of our activity in Q1 has focused on Toga. We completed work on Toga's new Qt backend, achieving full widget coverage. We made some significant improvements to the API for managing columns in Tree and Table widgets. On Windows, we've added an implementation of a Tree widget for the first time, and signficantly improved the Table widget. We made a major change to how widgets are imported, improving load times for Toga apps, and allowing third-party libraries to register their own widgets and their own implementations of existing widgets. We also performed a major refactor of the Canvas widget API, improving consistency between Toga's Python API and the HTML5 Canvas API that we use as a reference implementation.

We also made improvements to Toga's Positron plugin. Positron is Toga's answer to Electron - a way to build cross-platform apps where the user interface is provided by a web page. However, Positron allows you to use Python web servers rather than Javascript - and unlike Electron, allows for the development of hybrid applications and mobile application. This quarter, we added the ability to deploy a FastAPI website; improved the tooling for building an app from an existing website; and we've prototyped a new PyScript backend that allows client-side browser code to access server-side capabilities.

However, the biggest Toga news for the quarter is that we laid out a design plan for the next phase of Toga's development, addressing issues of "Big Picture" app design. The set of widgets offered by Toga is reasonably complete for most platforms. At this point, the issue facing application developers - especially on mobile platforms - is how to represent navigation between content in a large app. After some public discussions, we've laid out a plan for a range of improvements that should enable users to write reasonably complex applications in Toga, while retaining cross-platform, single source base compatibility. This plan will form the basis of Toga development for the coming months.

Work on Android wheels has progressed. We have published updated internal Android wheels for a number of key data science packages, including NumPy, Pandas, SciPy, scikit-learn and xgboost. Developing these patches involved developing updates to a variety of tools that are used to build wheels, including `cibuildwheel`, `auditwheel`, Meson, and Python's own Android testbed. The patches resulting from this work take time to get upstream; that work will proceed in the background over the coming months.

We have completed the work adding iOS to CPython's release artefacts. As a result, Python 3.15.0b1 should include an official CPython iOS XCframework that can be incorporated into an iOS project. As part of this work, we've also assisted with a large cleanup of the CPython repository, moving all the platform-specific build tooling for iOS, Android and Emscripten into a single "Platforms" directory. Along the way, we've addressed some minor inconsistencies and usage issues with these build scripts.

We released Briefcase 0.4.0, which includes a major improvement to the operation of development mode operates for apps, isolating the dependencies of the app being developed from the environment that is running Briefcase. It also includes support for PEP 639 license specifications - part of an ongoing effort to align Briefcase metadata with PEP 621. We've also started experimenting with the use of `ty` to enforce type annotations in Briefcase's code.

After some discussion by the team, we've made the decision to adopt an AI Contribution policy. This policy adopts a neutral stance on the use of AI tooling; however, it requires formal declaration of AI tool usage, and makes it clear that the humans driving autonomous tools are ultimately responsible for the output of those tools. The policy is currently in the final stages of getting approval from the team; we expect to roll out the policy in the next couple of weeks.

Lastly, we released our new project website. The content of this website isn't signficantly different to before - but it now uses the same MkDocs tooling that we use for all our other documentation, giving us much faster builds, better translation tooling, search... and dark mode! It also includes translations to some new languages, including Japanese and Russian.

## Q2 priorities

In Q2, we have two main priorities.

Firstly, we'll be focusing on some key improvements to Briefcase. We intend to continue improving Windows MSI installers, adding some additional customization options, and adding support for Windows on ARM64. We plan to start investigating the use of Conda environments for building Briefcase apps. Lastly, we will explore mechanisms for updating the content of an existing app without having to go through an App Store review cycle. This may also open options for "live reload" of app development.

Secondly, we plan to start executing on the "Big Picture" plan that was laid out in this quarter. That plan describes a lot of changes, so we don't anticipate completing that plan for some time. However, we're hoping to see some progress on the foundational pieces of that work, which we will build on over the course of the year.

We will also be attending [PyCon US](https://us.pycon.org/2026/schedule/presentation/36/). We're presenting talks on [mechanisms for distributing Python code](https://us.pycon.org/2026/schedule/presentation/36/) and [switching your project documentation from Sphinx to Markdown](https://us.pycon.org/2026/schedule/presentation/6/). We'll be there for [both days of the sprints](https://us.pycon.org/2026/events/dev-sprints/), as well as participating in a number of other events and generally lurking around the hallways. If you're able to make it, make sure you say hello!

## Longer term goals

Now that we've published a plan for "Big Picture" app development, our primary long term goal is to deliver on that plan.

Along the way, we're not going to ignore Briefcase. Briefcase already solves a number of key distribution problems in the Python ecosystem; but there's a lot of opportunity to further improve alignment with Python ecosystem standards, simplify the process of developing apps, and streamline publication of apps into app stores.

However, there's only so much the core team can do by ourselves. The ultimate long term goal is to build the community of BeeWare users and developers so that the core team isn't the only source of new features and support. Part of the reason we spent time publishing a plan for Toga's future development rather than just doing the work ourselves is to enable community contribution. We hope to do more of this community enablement work over the coming months.
