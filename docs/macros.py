import datetime
from pathlib import Path
from textwrap import dedent

import yaml


def as_date(value):
    """Return a date, whether YAML parsed the value as a date or a string."""
    if isinstance(value, datetime.date):
        return value
    return datetime.date.fromisoformat(str(value))


def merge_team_details(team, team_details):
    """Merge the blog author details with the team details for each author.

    The blog only accepts a limited set of fields for each author, so the
    remaining team details are stored separately, keyed by the same GitHub ID.
    """
    return {
        "authors": {
            github_id: {**author_details, **team_details.get(github_id, {})}
            for github_id, author_details in team["authors"].items()
        }
    }


def get_metadata(contents):
    return next(yaml.load_all(contents, Loader=yaml.SafeLoader))


def attendees(authors, team):
    """Generates string identifying attendees of an event, based on whether there is
    one, or more.
    """
    if len(authors) == 1:
        return team["authors"][authors[-1]]["short_name"]
    else:
        return (
            ", ".join(team["authors"][author]["short_name"] for author in authors[:-1])
            + " and "
            + team["authors"][authors[-1]]["short_name"]
        )


def pronouns(pronoun):
    expanded_pronouns = {
        "she": ("venus", "she", "her"),
        "he": ("mars", "he", "him"),
        "they": ("non-binary", "they", "them"),
    }
    return expanded_pronouns[pronoun]


def talk_title_punctuation(talk_title):
    """Preserves talk title punctuation when talk is provided at the end of a
    sentence.
    """
    if talk_title.endswith(("!", "?")):
        return talk_title
    else:
        return f"{talk_title}."


def define_env(env):
    # The docs directory being built; for translations, this is the directory
    # containing the translated content.
    docs_dir = Path(env.project_dir) / env.conf["docs_dir"]

    def full_team(team):
        """Merge the team details into the blog author details."""
        team_details = yaml.load(
            (docs_dir / "news/.team.yml").read_text(encoding="utf-8"),
            Loader=yaml.SafeLoader,
        )
        return merge_team_details(team, team_details)

    @env.macro
    def fa(style, name):
        """Generates an inline Font Awesome icon, using the icon shortcodes
        provided by the emoji extension, rather than depending on the Font
        Awesome kit/CDN.
        """
        return f'<span class="fa-icon">:fontawesome-{style}-{name}:</span>'

    @env.macro
    def generate_resource_post(resource):
        """Generate a resource post from resource template."""
        content = []

        if resource["type"] == "video" and resource["embeddable"]:
            video_url = dedent(f"""\
                <div class="resource-video">
                    <iframe class="video" src="{resource["url"]})"
                            frameborder="0" allowfullscreen>
                    </iframe>
                </div>
            """)
            content.append(video_url)

        content.append(f"""{resource["description"]}\n""")

        if resource["type"] in ["article"]:
            article_url = dedent(f"""\

                [Read the full article here.]({resource["url"]})

            """)
            content.append(article_url)

        elif resource["type"] == "podcast":
            podcast_url = dedent(f"""\

                [Click here to listen.]({resource["url"]})

            """)
            content.append(podcast_url)

        elif resource["type"] == "video" and not resource["embeddable"]:
            video_url = dedent(f"""\

                As seen at [{resource["event_name"]}]({resource["event_url"]}).

                [View the video here.]({resource["url"]})

            """)
            content.append(video_url)

        elif resource["type"] == "video" and resource["embeddable"]:
            content.append(
                f"\n\nAs seen at [{resource['event_name']}]({resource['event_url']}).\n\n"  # noqa: E501
            )

        content.append("<!-- more -->")

        return "".join(content)

    @env.macro
    def generate_event_post(authors, event, involvement, team):
        """Generate an event post from event template."""
        team = full_team(team)
        content = []
        start_date = as_date(event["date"])
        end_date = as_date(event["end_date"])
        if start_date == end_date:
            event_timeframe = f"on {start_date.strftime('%B %d, %Y')}"
        else:
            event_timeframe = (
                f"from {start_date.strftime('%B %d')} "
                f"- {end_date.strftime('%B %d, %Y')}"
            )

        highlight_authors = set()
        show_participation = False
        for inv in involvement:
            if inv["type"] == "organizing":
                highlight_authors.update(set(inv["team_members"]))
                content.append(
                    dedent(f"""\
                        {attendees(inv["team_members"], team)} will be organizing [{event["name"]}]({event["url"]}), which will happen {event_timeframe}!\n\n
                    """)  # noqa: E501
                )
            elif inv["type"] == "keynote":
                highlight_authors.update(set(inv["team_members"]))
                content.append(
                    dedent(f"""
                    {attendees(inv["team_members"], team)} will be keynoting {event["name"]}, giving a presentation entitled [{talk_title_punctuation(inv["title"])}]({inv["url"]})

                    <!-- more -->\n\n
                    """)  # noqa: E501
                )
            elif inv["type"] != "attending":
                show_participation = True

        inv_types = {inv["type"] for inv in involvement}

        if "keynote" in inv_types or "organizing" in inv_types:
            other_authors = [
                author for author in authors if author not in highlight_authors
            ]
            if other_authors:
                content.append(
                    dedent(f"""\
                        {attendees(other_authors, team)} will also be attending.

                        <!-- more -->\n\n
                    """)
                )
        else:
            content.append(
                dedent(f"""\
                    {attendees(authors, team)} will be attending [{event["name"]}]({event["url"]}) {event_timeframe}!

                    <!-- more -->\n\n
                """)  # noqa: E501
            )

        content.append(f"{event['description']}\n\n")

        _, first_pronoun, second_pronoun = pronouns(
            team["authors"][authors[-1]]["pronoun"]
        )

        if show_participation:
            if len(authors) > 1:
                content.append("You can find us throughout the event:\n\n")
            else:
                content.append(
                    f"You can find {second_pronoun} throughout the event:\n\n"
                )

        for inv in involvement:
            if len(authors) > 1:
                team_members = attendees(inv["team_members"], team)
            else:
                team_members = first_pronoun.capitalize()

            if inv["type"] == "talk":
                talk = dedent(
                    f"""
                    - {team_members} will be giving a talk entitled [{talk_title_punctuation(inv["title"])}]({inv["url"]})

                    """  # noqa: E501
                )
                content.append(talk)

            elif inv["type"] == "tutorial":
                tutorial = dedent(f"""
                    - {team_members} will be hosting a tutorial entitled [{talk_title_punctuation(inv["title"])}]({inv["url"]})

                    """)  # noqa: E501
                content.append(tutorial)

            elif inv["type"] == "workshop":
                tutorial = dedent(f"""
                    - {team_members} will be hosting a workshop entitled [{talk_title_punctuation(inv["title"])}]({inv["url"]})

                    """)  # noqa: E501
                content.append(tutorial)

            elif inv["type"] == "sprint":
                sprint = dedent(f"""
                    - {team_members} will be hosting a [sprint]({inv["url"]}).

                    """)
                content.append(sprint)

            elif inv["type"] == "booth":
                booth = dedent(f"""
                    - {team_members} will be hosting a [booth]({inv["url"]}).

                    """)
                content.append(booth)

            elif inv["type"] == "track":
                tutorial = dedent(f"""
                    - {team_members} will be hosting the [{talk_title_punctuation(inv["title"])}]({inv["url"]})

                    """)  # noqa: E501
                content.append(tutorial)

        if len(authors) > 1:
            content.append(
                "Please come say hello, we'd love to meet you. "
                "We're looking forward to seeing you there!"
            )
        else:
            content.append(
                f"Please come say hello, {first_pronoun}'d love to meet you. "
            )
            if first_pronoun == "he":
                content.append("He's looking forward to seeing you there!")
            elif first_pronoun == "she":
                content.append("She's looking forward to seeing you there!")
            elif first_pronoun == "they":
                content.append("They're looking forward to seeing you there!")

        return "".join(content)

    @env.macro
    def generate_team_members(team, current):
        """Generate the team page from the .authors.yml and .team.yml file
        metadata.
        """
        team = full_team(team)
        team_member_content = []

        for github_id, member_details in team["authors"].items():
            try:
                if member_details["join_date"]:
                    member_title = dedent(f"""\
                        <div class="team-member" markdown="1">

                        ### {member_details["name"]} {{ #{github_id} }}
                    """)

                    try:
                        mastodon = member_details["mastodon"].split("@")
                        member_image_details_mastodon = f"""<div class="team-mastodon-handle" markdown="1">{fa("brands", "mastodon")} [{member_details["mastodon"]}](https://{mastodon[2]}/@{mastodon[1]})</div>"""  # noqa: E501
                    except KeyError:
                        member_image_details_mastodon = ""

                    pronoun_logo, first_pronoun, second_pronoun = pronouns(
                        member_details["pronoun"]
                    )

                    try:
                        member_email_details = f"""<div class="team-email" markdown="1">{fa("solid", "envelope")} <{member_details["email"]}></div>"""  # noqa: E501
                    except KeyError:
                        member_email_details = ""

                    member_image_details = dedent(
                        f"""\
                        <div class="team-image-details" markdown="1">

                        ![{member_details["name"]}](/{member_details["avatar"]})

                        <div class="team-contact-details" markdown="1">
                        <div class="team-pronouns" markdown="1">{fa("solid", pronoun_logo)} {first_pronoun}/{second_pronoun}</div>
                        <div class="team-github-handle" markdown="1">{fa("brands", "github")} [{github_id}](https://github.com/{github_id})</div>
                        {member_image_details_mastodon}
                        {member_email_details}
                        </div>
                        </div>

                        <div class="team-bio" markdown="1">
                        """  # noqa: E501
                    )

                    member_bio = (docs_dir / f"about/team/{github_id}.md").read_text(
                        encoding="utf-8"
                    )

                    team_member = (
                        member_title
                        + member_image_details
                        + member_bio
                        + "</div></div>"
                    )

                    if not current and "emeritus_date" in member_details:
                        team_member_content.append(
                            (member_details["emeritus_date"], team_member)
                        )
                    elif current and "emeritus_date" not in member_details:
                        team_member_content.append(
                            (member_details["join_date"], team_member)
                        )
            except KeyError:
                pass

        return "".join(tmc[1] for tmc in sorted(team_member_content))

    def posts(*paths):
        """Yield the docs-relative path and metadata of every post in the given
        docs-relative directories.
        """
        for path in paths:
            for post in sorted((docs_dir / path).glob("*.md")):
                yield (
                    post.relative_to(docs_dir).as_posix(),
                    get_metadata(post.read_text(encoding="utf-8")),
                )

    @env.macro
    def upcoming_events():
        """Generate upcoming events list for beeware.org homepage sidebar."""
        this_year = datetime.datetime.now().year
        next_year = this_year + 1

        events = []
        for src_path, metadata in posts(
            *(f"news/posts/{year}/events" for year in [this_year, next_year])
        ):
            start_date = as_date(metadata["event"]["date"])
            end_date = as_date(metadata["event"]["end_date"])

            if start_date > datetime.date.today():
                if start_date == end_date:
                    event_date = start_date.strftime("%B %d, %Y")
                else:
                    event_date = (
                        f"{start_date.strftime('%B %d')}-{end_date.strftime('%d, %Y')}"
                    )

                events.append(
                    (
                        start_date,
                        f"- [{metadata['event']['name']}: {event_date}]({src_path})",
                    )
                )

        if events:
            return "\n".join(item[1] for item in sorted(events)[:5])
        return None

    @env.macro
    def latest_news():
        """Generate "Latest news" latest blog post link for beeware.org homepage
        sidebar.
        """
        this_year = datetime.datetime.now().year
        last_year = this_year - 1

        latest_post = None

        for src_path, metadata in posts(
            *(f"news/posts/{year}/buzz" for year in [last_year, this_year])
        ):
            post_date = as_date(metadata["date"])
            if latest_post is None or latest_post[0] < post_date:
                latest_post = (post_date, metadata["title"], src_path)

        post_date, title, src_path = latest_post
        return f"{post_date.strftime('%B %d')}: [{title}]({src_path})"
