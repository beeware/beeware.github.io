---
title: February 2026 Status Update
date: 2026-03-02
authors:
- freakboy3742
categories:
- Buzz
---

February has seen a collection of improvements across the BeeWare ecosystem - including a couple of big milestones!

<!-- more -->

## What we've done

- We've launched a new version of our [website](https://beeware.org)! This primarily an infrastructure change - we've moved off Lektor, and onto a MkDocs-based site, matching the tooling that we're now using for the rest of BeeWare's documentation. This gives us much faster builds, better translation tooling, search... and dark mode! A huge shout out to [Kattni](/about/team.md#kattni) for all her work getting this done.
- We welcomed a new member of the BeeWare core team - [Corran Webster](/about/team.md#corranwebster). Over the last few months, Corran has taken Toga’s Qt backend from a bare stub to a widget-complete implementation. He’s also done some major internal design work around Toga's Table and Tree implementations, and added the long-requested ability to add bitmap images to a Canvas. That's a lot of work for a couple of months - we're excited to see what comes next!
- We published new [support packages for iOS and macOS](https://github.com/beeware/Python-Apple-support/releases), backporting some recent changes in CPython to our patches for Python 3.10-3.12.
- We made significant progress on adding [FastAPI and PyScript backends for Positron](https://github.com/beeware/toga/pull/4156). The PyScript part of this backend has revealed some issues with the feature set of Android and iOS `WebView` widgets; we're working with the PyScript team to find a workaround for these problems.
- We [fixed several issues with the testbed application that is used to test Python on Android](https://github.com/python/cpython/pull/142912).
- We [added a plugin interface to Briefcase to allow for the definition of publication channels](https://github.com/beeware/briefcase/pull/2701). We're working with the [PythonAnywhere](https://pythonanywhere.com) team to build a [plugin that will allow for the publication of web apps](https://github.com/pythonanywhere/pythonanywhere-briefcase-plugin).
- We optimized the [work that Briefcase does when inspecting app configurations on startup](https://github.com/beeware/briefcase/pull/2659).
- We added the ability to [revoke permissions when running an app on Android](https://github.com/beeware/briefcase/pull/2664).
- We [corrected an issue handling macOS wheels that have multiple platform tags](https://github.com/beeware/briefcase/pull/2692).
- We [fixed some issues with Briefcase's version parsing logic](https://github.com/beeware/briefcase/pull/2694).
- We modified how Briefcase handles dependencies on Linux to ensure that [package extras are preserved on packages that are specified as local dependencies](https://github.com/beeware/briefcase/pull/2702).
- We corrected an issue with the [naming of DEB packages produced by Briefcase](https://github.com/beeware/briefcase/pull/2703).
- We [improved the documentation for packaging apps that weren't created with Briefcase](https://github.com/beeware/briefcase/pull/2677).
- We finished porting all widgets for the Qt backend, adding a [`DetailedList`](https://github.com/beeware/toga/pull/4165) and [`Tree`](https://github.com/beeware/toga/pull/4112) widgets.
- We corrected some issues with how [Toga's canvas widget handles transforms in the middle of a path](https://github.com/beeware/toga/pull/4106).
- We added support for [rounded rectangles on `Canvas`](https://github.com/beeware/toga/pull/4161).
- We corrected some [edge cases in the handling of join mitering on Toga's `Canvas` widget](https://github.com/beeware/toga/pull/4162).
- We ensured that Toga's `WebView` widget can always handle HTML content provided as a string [no matter how large that content is](https://github.com/beeware/toga/pull/4062).
- We modified Toga's codebase to make [better use of abstract base classes (ABCs)](https://github.com/beeware/toga/pull/4142).
- We added the ability for [WinForms `Table` widgets to have an icon in *every* column, not just the first column](https://github.com/beeware/toga/pull/4164).
- We corrected some [memory leaks in Toga's Windows backend](https://github.com/beeware/toga/pull/4167).
- We [improved how corrupted icons are handled in Toga](https://github.com/beeware/toga/pull/4191), providing a fallback path instead of a crash.
- We [fixed an intermittent issue with the testbed when testing Toga on Android](https://github.com/beeware/toga/pull/4208).
- We made some [changes to our bug reporting template](https://github.com/beeware/.github/pull/303), and [added a new template for reporting documentation issues](https://github.com/beeware/.github/pull/306).

## What's next?

In March, we're hoping to wrap up our work on the FastAPI and PyScript plugins for Positron. The plugin is mostly done, but we're looking into some additional optimizations and improvements that will improve the experience when using the plugin.

However, most of our focus will be on design work around capabilities that are currently missing from Toga. This month saw some initial discussions on these topics. We're hoping that by the end of the month, we'll be able to resolve those discussions with some concrete designs that we can start to implement.

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).
