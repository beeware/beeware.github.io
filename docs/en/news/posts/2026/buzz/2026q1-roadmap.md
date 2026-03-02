---
title: 2026Q1 Roadmap
date: 2026-01-16
authors:
- freakboy3742
categories:
- Buzz
---

In Q4, BeeWare saw wide-ranging improvements across almost all the tools we maintain, as well as the conclusion of some long-running efforts in wheel packaging. As always, this roadmap should be read as a guide to what we aim to focus on over the coming quarter, rather than a hard commitment to features that will be made available on a specific deadline.

<!-- more -->

## Q4 progress

We have now concluded our work on iOS packaging. We contributed support for iOS to Maturin and `PyO3`, and have been able to successfully publish wheels for Cryptography to BeeWare's iOS wheel repository. We need to wait for a formal release of `PyO3` and `cffi` before we can contribute patches to Cryptography, but we know the work that needs to be done.

We have added iOS to CPython's CI processes; however we haven't been able to add iOS to CPython's release artefacts. This is due to some ongoing discussions about the need to centralize the processes of producing binary dependencies, and providing SBOMs for that work. We hope to revisit this work before the 3.15 release. Work was also slowed by a large number of issues with GitHub's macOS runners. During Q4, we saw a disturbingly large number of regressions and performance issues caused by changes made by GitHub; responding to those issues consumed a lot of our time. These issues are not yet fully resolved; but we have workarounds in place that will work until later this year. We hope that GitHub will have resolved the underlying problems before those workarounds stop working.

Work on Android wheels has not proceeded as quickly as we had hoped due to the need to address some compatibility issues with the most recent Android SDK release; but we have made some progress. We hope to wrap up Android wheels work in this coming quarter.

Toga saw the addition of a completely new Qt backend - and a large proportion of the widgets on that backend have been implemented. We also published a new `system-pyside6` package that allows the use of system-provided Qt bindings in an isolated Python virtual environment - this ensures that packaged Qt apps don't need to include a complete copy of Qt in order to run. We also added support for a number of GTK4 widgets, and added initial support for Adwaita (a common Gnome desktop theme) in Toga's GTK4 backend. We've also seen a large number of fixes to Toga required by the roll out of Apple's "Liquid Glass" appearance changes in macOS 26 and iOS 26. We are continuing to find and response to these edge cases as we find them.

Briefcase saw a number of significant improvements. We were able to leverage the work done by our Curtin University capstone students to significantly improve the experience of development mode for Briefcase projects. We added support for customizing the install directory, and configuring uninstall options to Windows installers. We also added a framework for integrated debugging support for packaged apps, including plugins for PDB and Visual Studio Code.

Lastly, we completed our documentation switch to Markdown, launching a new documentation landing page on the BeeWare website, converting Briefcase and Rubicon's documentation to Markdown format, adding improved machine translation workflows, and rolling out a major refresh of our contribution guides.

## Q1 priorities

In Q1, we have three main priorities.

Firstly, we hope to wrap up work on binary packaging of wheels on Android. We hope that we'll be able to wrap up work on Android wheel packaging this quarter.

Secondly, we've had some interest from the PyScript team on using Toga's Positron layer as a mechanism for deploying PyScript apps. As a result, we'll be spending some time to improve the integration of Positron with PyScript.

Our last goal is to return our focus to Toga's native GUI capabilities, especially for mobile platforms. Over the course of this quarter, we're hoping to see progress on Table and Tree widgets (which have long been gaps on iOS and Android), as well as the start of work on notifications and high-level navigation in iOS applications. These are all completely new capability additions for Toga, so the design process will likely take some time.

## Longer term goals

We've spent the last 2 years establishing a firm technical foundation. We've formalized iOS and Android support in CPython itself, and we've ensured that Python binary packages can be fully supported on mobile platforms. We can now turn our attention to the things we want to build on this foundation.

Our focus for the rest of this year will be to improve Toga so that it can be used for "real world" applications. We're hoping to fill out the Toga API gaps that have historically existed, and have prevented people from building useful applications. This means more widgets, more mobile-specific capabilities - and more time spent documenting and promoting what can be done with Toga.

Part of the motivation for spending time on promotion is to encourage the development of a vibrant and growing community around Toga, and BeeWare as a whole. We want to spread the excitement that we feel about BeeWare to others, welcoming new people into our community, while ensuring that when they arrive, we have a buzzing hive of BeeWare contributors ready to provide support for newcomers, share expertise with those building complex projects, fix bugs, and add yet more features as time progresses. To that end, we hope to spend more time engaging with folks in the Python ecosystem to show how they can begin their BeeWare journey.
