import datetime
from pathlib import Path
from textwrap import dedent
import yaml


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
    @env.macro
    def fa(*tags):
        """Generates the fontawesome HTML i element."""
        tags = " ".join(f"fa-{tag}" for tag in tags)
        return f'<i class="{tags}"></i>'

    @env.macro
    def generate_resource_post(resource):
        """Generate a resource post from resource template."""
        content = []

        if resource["type"] == "video" and resource["embeddable"]:
            video_url = dedent(f"""\
                <div class="resource-video">
                <iframe class="video" src="{resource["url"]})" frameborder="0" allowfullscreen></iframe>
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
                f"\n\nAs seen at [{resource['event_name']}]({resource['event_url']}).\n\n"
            )

        content.append("<!-- more -->")

        return "".join(content)

    @env.macro
    def generate_event_post(authors, event, involvement, team):
        """Generate an event post from event template."""
        content = []
        if event.date == event.end_date:
            event_timeframe = f"on {event.date.strftime('%B %d, %Y')}"
        elif event.date != event.end_date:
            event_timeframe = (
                f"from {event.date.strftime('%B %d')} "
                f"- {event.end_date.strftime('%B %d, %Y')}"
            )

        for inv in involvement:
            if inv["type"] == "keynote":
                content.append(dedent(f"""
                    {attendees(inv["team_members"], team)} will be keynoting {event.name}, giving a presentation entitled [{talk_title_punctuation(inv["title"])}]({inv["url"]})

                    <!-- more -->\n\n
                    """))

        inv_types = {inv["type"] for inv in involvement}

        if "organizing" in inv_types:
            content.append(
                dedent(f"""\
                    {attendees(authors, team)} will be organizing [{event.name}]({event.url}), which will happen {event_timeframe}!\n\n
                """)
            )
        elif inv_types != {"keynote"}:
            content.append(
                dedent(f"""\
                    {attendees(authors, team)} will be attending [{event.name}]({event.url}) {event_timeframe}!

                    <!-- more -->\n\n
                """)
            )

        content.append(f"{event.description}\n\n")

        _, first_pronoun, second_pronoun = pronouns(team["authors"][authors[-1]]["pronoun"])

        if inv_types != {"attending"} and inv_types != {"organizing"} and inv_types != {"keynote"}:
            if len(authors) > 1:
                content.append(f"You can find us throughout {event.name}:\n\n")
            else:
                content.append(f"You can find {second_pronoun} throughout {event.name}:\n\n")

        for inv in involvement:
            if len(authors) > 1:
                team_members = attendees(inv["team_members"], team)
            else:
                team_members = first_pronoun.capitalize()

            if inv["type"] == "talk":
                talk = dedent(f"""
                    - {team_members} will be giving a talk entitled [{talk_title_punctuation(inv["title"])}]({inv["url"]})

                    """)
                content.append(talk)

            elif inv["type"] == "tutorial":
                tutorial = dedent(f"""
                    - {team_members} will be hosting a tutorial entitled [{talk_title_punctuation(inv["title"])}]({inv["url"]})

                    """)
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
                content.append(f"He's looking forward to seeing you there!")
            elif first_pronoun == "she":
                content.append(f"She's looking forward to seeing you there!")
            elif first_pronoun == "they":
                content.append(f"They're looking forward to seeing you there!")

        return "".join(content)

    @env.macro
    def generate_team_members(team, page, current):
        """Generate the team page from the .authors.yml file metadata."""
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
                        member_image_details_mastodon = f"""<div class="team-mastodon-handle" markdown="1">{fa("mastodon", "lg", "brands")} [{member_details["mastodon"]}](https://{mastodon[2]}/@{mastodon[1]})</div>"""
                    except KeyError:
                        member_image_details_mastodon = ""

                    pronoun_logo, first_pronoun, second_pronoun = pronouns(member_details["pronoun"])

                    member_image_details = dedent(
                        f"""\
                        <div class="team-image-details" markdown="1">

                        ![{member_details["name"]}](/{member_details["avatar"]})

                        <div class="team-contact-details" markdown="1">
                        <div class="team-pronouns" markdown="1">{fa("regular", pronoun_logo)} {first_pronoun}/{second_pronoun}</div>
                        <div class="team-github-handle" markdown="1">{fa("github", "lg", "brands")} [{github_id}](https://github.com/{github_id})</div>
                        {member_image_details_mastodon}
                        <div class="team-email" markdown="1">{fa("envelope", "lg", "solid")} <{member_details["email"]}></div>
                        </div>
                        </div>
                        
                        <div class="team-bio" markdown="1">
                        """
                    )

                    member_bio = (
                        Path(page.file.src_dir) / f"about/team/{github_id}.md"
                    ).read_text()

                    team_member = member_title + member_image_details + member_bio + "</div></div>"

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

    def get_metadata(contents):
        return next(yaml.load_all(contents, Loader=yaml.SafeLoader))

    @env.macro
    def upcoming_events(files):
        """Generate upcoming events list for beeware.org homepage sidebar."""
        this_year = datetime.datetime.now().year
        next_year = this_year + 1

        events = []
        for filename, file_data in files.src_uris.items():
            if filename.startswith(
                tuple(f"news/posts/{year}/events/" for year in [this_year, next_year])
            ):
                metadata = get_metadata(file_data.content_string)

                if metadata["event"]["date"] < datetime.date.today():
                    if metadata["event"]["date"] == metadata["event"]["end_date"]:
                        event_date = metadata["event"]["date"].strftime("%B %d, %Y")
                    else:
                        event_date = (
                            f"{metadata['event']['date'].strftime('%B %d')}"
                            f"-{metadata['event']['end_date'].strftime('%d, %Y')}"
                        )

                    events.append(
                        (
                            metadata["event"]["date"],
                            (
                                f"- [{metadata['event']['name']}"
                                f": {event_date}]({file_data.src_path})",
                            ),
                        )
                    )

        if events:
            return "\n".join(item[1] for item in sorted(events)[:5])
        return "Nothing at the moment..."

    @env.macro
    def latest_news(files):
        """Generate "Latest news" latest blog post link for beeware.org homepage
        sidebar.
        """
        this_year = datetime.datetime.now().year
        last_year = this_year - 1

        latest_post = None

        for filename, file_data in files.src_uris.items():
            if filename.startswith(
                tuple(f"news/posts/{year}/buzz/" for year in [last_year, this_year])
            ):
                metadata = get_metadata(file_data.content_string)

                if latest_post is None or latest_post[0]["date"] < metadata["date"]:
                    latest_post = (metadata, file_data)

        return (
            f"{latest_post[0]['date'].strftime('%B %d')}"
            f": [{latest_post[0]['title']}]({latest_post[1].src_path})"
        )
