<a href="https://beeware.org"><img src="http://beeware.org/static/images/brutus-270.png" width="72px" alt="Brutus the Bee"></a>

# beeware.github.io

---

This is the homepage for the [BeeWare project](http://beeware.org).

It is a [Lektor](https://getlektor.com)-based site.

If you want to contribute a modification, you can fork this repository
and submit a pull request. However, **do not fork the main branch** -
fork the [lektor branch](https://github.com/beeware/beeware.github.io/tree/lektor) and make changes there instead.

If you want to test out a change before you submit it, create a virtual
environment, and install [Lektor](https://getlektor.com):

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install lektor
```

Then from the root directory of the checkout, run:

```
(venv) $ lektor server
```

This will [start a webserver](http://127.0.0.1:5000) that will
autoreload whenever you make a change to site content.

## Community

---

You can talk to the community through:

- [@beeware@fosstodon.org on Mastodon](https://fosstodon.org/@beeware)
- BeeWare Discord server: [Discord](https://beeware.org/bee/chat/)
- [Tickets on the beeware.github.io issue tracker](https://github.com/beeware/beeware.github.io/issues)

## Contributing

---

If you find problems with this website, [log them on GitHub](https://github.com/beeware/beeware.github.io/issues). If you want to contribute, please [fork the code](https://github.com/beeware/beeware.github.io/tree/lektor) and [submit a pull request](https://github.com/beeware/beeware.github.io/pulls).

Before submitting a pull request, please make sure your forked branch is
up-to-date with the original branch. To do this:

- Set your upstream remote:

```
$ git remote add upstream https://github.com/beeware/beeware.github.io.git
```

- Make sure you have the latest changes from upstream:

```
$ git fetch upstream
```

- Rebase your `lektor` branch to `upstream` before pushing to git
  and submitting a pull request:

```
$ git rebase upstream/lektor
```

## Translations

<a href="https://hosted.weblate.org/projects/beeware/website/"><img src="https://hosted.weblate.org/widget/beeware/website/open-graph.png" width="300px" alt="Website translation status"></a>

We manage translations using [Weblate](https://weblate.org/).

<a href="https://hosted.weblate.org/engage/beeware/"><img src="https://hosted.weblate.org/widget/beeware/website/horizontal-auto.svg" alt="Translation status" /></a>

If you'd like to contribute to the translation effort, join the `#translations`
channel on [Discord](https://beeware.org/bee/chat/) and introduce yourself!
