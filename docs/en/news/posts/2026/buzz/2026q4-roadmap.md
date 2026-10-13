---
title: 2026Q4 Roadmap
date: 2026-10-15
authors:
- freakboy3742
categories:
- Buzz
---

Q3 was dominated by preparations for the Python 3.15 release, and by improvements to the security posture of BeeWare's tools. As always, this roadmap should be read as a guide to what we aim to focus on over the coming quarter, rather than a hard commitment to features that will be made available on a specific deadline.

<!-- more -->

## Q3 progress

Our primary focus in Q3 was supporting the Python 3.15 release - and we're happy to report that this work is complete. Python 3.15.0 has been released, and we've published new releases of Chaquopy, Briefcase and Toga to support it. Briefcase now uses the official CPython iOS binary release when building iOS apps. We've dropped support for Python 3.10 across all of BeeWare's projects and templates. `cibuildwheel` also supports building iOS wheels for Python 3.15.

To support this work, we made substantial improvements to [`xbuild`](https://github.com/beeware/xbuild), BeeWare's PEP 517 build frontend for cross-compiling wheels. Briefcase now uses `xbuild` to create cross-platform virtual environments for iOS. We've also made extensive changes to `xbuild` that are aimed at simplifying `cibuildwheel`'s cross-platform wheel-building; we hope to submit those changes upstream in the near future. The improvements to `xbuild` should also be useful for testing code outside `cibuildwheel`.

We also kept up with changes in the platforms we support. We updated Briefcase's Android template to target API level 36, keeping apps compliant with Google Play requirements; we added support for the changes in Xcode 27, including the new Device Hub; and we updated Toga's iOS backend to support the Scene-based application life cycle required by the iOS 27 SDK. We've migrated our CI configurations off macOS 14. However, Ubuntu 26.04 didn't leave beta until late September, so we haven't yet had a chance to update our CI to use those new images.

We've made significant improvements to the security of BeeWare's tools. Briefcase now performs hash verification of all tool and template downloads, and of the contents of its asset cache. We've also continued hardening our GitHub Actions workflows across BeeWare's repositories. We decided against implementing a "no downloads" mode for security hardening purposes, but we *did* develop a manual process for bootstrapping a Briefcase environment for tutorial purposes. We used this process for our workshop at PyCon AU, and it proved successful. We may revisit this in future; but for now, the manual process works well enough to meet our tutorial needs.

We also completed the rework of Briefcase's environment handling that we started in Q2. Briefcase can now use `uv` or Conda to manage app environments, and each app is built in an isolated virtual environment.

We made some progress on Toga as well. We added a new WinForms event loop implementation that dramatically improves the performance of Windows apps, and fixed a cluster of DPI scaling problems. We've also started implementing Toga's new Scaffold layer - the first piece of the "Big Picture" app navigation design that we published earlier this year.

We attended [PyCon AU](https://2026.pycon.org.au), where we presented a workshop and two talks; and we welcomed Oliver Leigh to the BeeWare core team, in recognition of his ongoing contributions to Toga's WinForms backend.

## Q4 priorities

Q4 will be a short quarter, as the BeeWare team will be taking leave over the end-of-year holidays. However, we still have a lot planned.

Firstly, we'll be working on adding Android support to [Pillow](https://github.com/python-pillow/Pillow). Pillow already supports iOS; adding Android will make Pillow available on both major mobile platforms. As one of the most widely used libraries in the Python ecosystem, this will be a significant step forward for the Python mobile experience.

Secondly, we'll be working with the NumPy team to finalize Tier 2 support for Android and iOS. Earlier this year, both platforms were accepted as Tier 3 supported platforms in NumPy. Moving to Tier 2 *should* be mostly procedural; but it may require some additional work, and navigating the process will take some effort.

Lastly, we'll be returning to Toga as an area of focus. In particular, we'll be resuming work on the "Big Picture" app navigation design that we published earlier this year, building on the initial work on the Scaffold layer that we started in Q3.

## Longer term goals

Much of the work we've done over the last 2 years has been an essential part of establishing a strong foundation for mobile app development - but that work hasn't been very "flashy". Over the coming quarters, we're hoping to reverse that trend, and show off features that are more obviously impressive and useful. We're hoping to engage in more demo-driven development - writing new features for Toga, and then demonstrating those features with apps that use them. Those new features will be accompanied by blog posts and other supporting documentation so that it's obvious how BeeWare can be used to build complex, useful applications.
