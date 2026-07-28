---
title: We'll be at EuroPython 2026!
date: 2026-07-01
authors:
- mhsmith
categories:
- Events
event:
  name: EuroPython 2026
  url: https://ep2026.europython.eu
  date: 2026-07-13
  end_date: 2026-07-19
  description: |-
    EuroPython is a week of talks, tutorials, sprints, and community. Join 1,500+ Pythonistas in July, in Kraków, Poland 🇵🇱.
involvement:
- type: talk
  team_members:
  - mhsmith
  title: Supporting Android and iOS in your Python package
  url: https://ep2026.europython.eu/session/supporting-android-and-ios-in-your-python-package
  date: 2026-07-17
  end_date: 2026-07-17
  description: |
    One of the most exciting recent developments in Python is the addition of Android and iOS as officially-supported platforms. This allows us to reach far more users on the devices where they spend the most time.

    What does this mean for you as a Python package maintainer? If your package is pure-Python, then it'll probably just work. But if it uses C, Cython, Rust, or any other native-compiled language, then you'll have to take some steps to make it available to these new platforms.

    The mobile support status of the most popular packages on PyPI can be seen at beeware.org/mobile-wheels. Let's help push those numbers up! Come to this talk to learn about:

    * Why mobile platforms are important for the future of Python
    * How to build your package for Android and iOS using cibuildwheel
    * How to test your mobile builds – even if you don't have Android or iOS hardware
    * How to distribute mobile packages to your users
    * How to automate all of these things in your CI system
- type: sprint
  team_members:
  - mhsmith
  url: https://ep2026.europython.eu/sprints/
  date: 2026-07-18
  end_date: 2026-07-18
  description: |
    Join us for two days of open-source hacking, learning, and collaboration! As is tradition, the sprints will happen the weekend after EuroPython.
---

{{ generate_event_post(authors, event, involvement, team) }}
