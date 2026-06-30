---
name: draft-monthly-status-update
description: Generate a draft blog post that describes the notable project updates from the past month.
---

# Generate monthly status update

Produce a blog post draft in a file named `docs/en/news/posts/<year>/buzz/<month>-<year>-status-update.md`, substituting the year and month as appropriate. If this skill is run after the 20th day of the month it will be a summary of the current month. At any other time, it will be a summary of the previous month.

## Steps

1. Generate a stub `docs/en/news/posts/<year>/buzz/<month>-<year>-status-update.md` that follows the following template:

```markdown
---
title: { month } { year }  Status Update
date: { first day of the next month, in YYYY-MM-DD format }
authors:
- { username }
categories:
- Buzz
---

{ summary }

<!-- more -->

## What we've done

- { work item }
- { work item }

Much of this work is due to the contributions of members of the BeeWare community. Thanks to <nospell> { contributors } </nospell> for their code and documentation contributions this month.

## What's next?

A summary of coming activity.

## Want to get involved?

Want to get involved? We curate issues that should be approachable for first-time contributors to BeeWare. They're all relatively minor changes, but would provide a big improvement to the lives of BeeWare users:

- If you're interested in the tooling for deploying applications to various platforms, take a look at [Briefcase](https://github.com/beeware/briefcase/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).
- Or, if you're interested in GUI widgets, take a look at [Toga](https://github.com/beeware/toga/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22).

These lists can also be filtered by platform - so you can find issues that are specific to your preferred operating system. Pick one of these tickets, drop a comment on the ticket to let others know you're looking at it, and try your hand at a PR! We have a [guide on setting up a Briefcase development environment](https://briefcase.beeware.org/en/latest/how-to/contribute/how/dev-environment/); but if you need any additional assistance or guidance, you can ask on the ticket, or join us on the [BeeWare Discord server](https://beeware.org/bee/chat/).

```

2. Fill out the document Markdown preamble with appropriate values. Ask the user for their Github username.
3. Build a list of all GitHub pull requests that have been merged into a repository in the `beeware` or `dmgbuild` project, except for those whose primary author is `dependabot` or `brutusthebee`.
4. Add to that list any pull request merged into a project owned by the `python`, `pypa`, or `PyO3` organziations where the author is `freakboy3742` or `mhsmith`:
5. Replace the bullet points in the "What we've done" section of the template document with the pull requests that have been found. Each bullet point should be a 1 sentence summary of the pull request, including a Markdown hyperlink to the pull request that spans the key part of the description (i.e., don't link preamble at the start of the sentence as part of the Markdown link)
6. Build a list of authors who contributed to the full list of pull requests found. Exclude any user who is a member of the BeeWare core team.
7. Replace the `{contributors}` block of the Markdown template with a list of authors that was found, sorted alphabetically by GitHub username. If the user has a full name listed in their Github profile, include their name as `[John Smith ([@johnsmith](https://github.com/johnsmith))]`; if they don't have a full name in their profile, use `[@johnsmith](https://github.com/johnsmith)`. The full list should be comma separated, with `, and` for the last entry in the list.

## Content guidelines

* The initial summary should be as short as possible.
* The bullet points created in step 5 should generally be one issue per bullet point. Multiple PRs should not be merged into a single bullet point unless they are near identical in content across multiple repositories, or are *extremely* closely related changes in the same repository.
* The summaries should be functional summaries describing what has changed from the perspective of the user, not how the feature was implemented.
* Do not attempt to draft the "What's next" section. Leave this for human authors.

## Validation

The final document should be a valid Markdown document with no spelling errors, as validated by running `tox -m pre-commit,docs-lint`.

If any words are identified as spelling errors by the `docs-lint` step, the user should be prompted to approve those words for addition in the `docs/spelling_wordlist` file. If a word is approved, it should be added to the file in alphabetical order.

## Examples

Any existing post in the `docs/en/news/posts/<year>/buzz` folder with a `-status-update.md` suffix can be used as an example. Newer examples should be considered better than older ones.
