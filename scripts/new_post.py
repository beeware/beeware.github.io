import datetime
import re
from pathlib import Path
from textwrap import dedent
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import yaml


def validate_url(url: str) -> bool:
    """Validates a URL.

    NOTE: CHECK YOUR ENTRY. This does a simple HEAD request check but only if
    you are connected to the internet. If that fails, it will parse the URL
    string to validate that it has the expected elements of a URL. There are
    edge cases where this will pass with an invalid entry.
    """
    try:
        urlopen(Request(url, method="HEAD"))
        return True
    except (URLError, HTTPError, ValueError):
        # If the URL fails to open, fall back to parsing the URL string. This
        # enables verification when an internet connection is unavailable.
        parsing_url = urlparse(url)
        if parsing_url.scheme in ["http", "https"] and parsing_url.netloc != "":
            print(
                "URL is the correct format, however it has not been validated. "
                "Verify it on post creation."
            )
            return True
        else:
            print("Invalid URL.")
            return False


def input_url(prompt: str, default: str | None = None) -> str:
    """Provides a prompt for a URL, returns a validated URL.

    :param prompt: The prompt string.
    :param default: Optional URL string, to be used as default value if no URL
        is provided.
    """
    while True:
        url = input(prompt)
        if not url and default:
            url = default
        if validate_url(url):
            return url


def input_date(prompt: str, default: datetime.date | None = None) -> datetime.date:
    """Provides a prompt for a date, returns a validated datetime object.

    :param prompt: The prompt string.
    :param default: Optional datetime object to be used as the default value
        if no date is provided.
    """
    while True:
        date = input(prompt)
        if not date and default:
            return default
        try:
            return (
                datetime.datetime.strptime(date, "%Y-%m-%d")
                .replace(tzinfo=datetime.UTC)
                .date()
            )
        except ValueError:
            print("Invalid date format. Must be YYYY-DD-MM format.")


def input_choice(prompt: str, choices: list[str]) -> str:
    """Provides a prompt for a choice from a list of choices, returns a choice string.

    :param str prompt: The prompt string. Will be followed by 'Choose a number: '.
    :param list choices: The list of choices, which will be presented with an
        associated number from which to choose.
    """
    print(prompt)
    for number, choice in enumerate(choices, start=1):
        print(f"{number}: {choice}")
    while True:
        try:
            response = int(input("Choose a number: "))
            if response <= 0:
                raise ValueError()
            return choices[response - 1].lower()
        except (ValueError, IndexError):
            print("Invalid; you must choose a number from the list.")


def request_blog_metadata():
    """Gathers metadata for a blog post."""
    blog_title = input("Blog post title: ")
    blog_authors = input(
        "Blog post author's GitHub user ID; separate multiple authors with a comma: "
    )

    return {
        "title": blog_title,
        "date": datetime.date.today(),
        "authors": [blog_author.strip() for blog_author in blog_authors.split(",")],
        "categories": ["Buzz"],
    }


def request_event_metadata():
    """Gathers metadata for an event post."""
    event_name = input("Event name: ")
    event_url = input_url("Event URL: ")
    event_start_date = input_date("Event start date (e.g. 2026-01-01): ")
    event_end_date = input_date(
        "Event end date (e.g. 2026-01-01; leave blank if same as event start date): ",
        event_start_date,
    )

    involvements = []
    authors = set()
    more = True
    while more:
        involvement_metadata = {}

        involvement_type = input_choice(
            "How is the team involved?",
            [
                "Attending",
                "Keynote",
                "Talk",
                "Tutorial",
                "Workshop",
                "Sprint",
                "Booth",
                "Organizing",
                "Track",
            ],
        )
        involvement_metadata["type"] = involvement_type

        team_members = input(
            "Enter GitHub user ID for all team members involved, separated by comma: "
        )
        team_member_list = sorted(
            [team_member.strip() for team_member in team_members.split(",")]
        )
        involvement_metadata["team_members"] = team_member_list
        authors.update(team_member_list)

        if involvement_type in ["keynote", "talk", "tutorial", "workshop", "track"]:
            presentation_title = input("Presentation title: ")
            involvement_metadata["title"] = presentation_title

        if involvement_type in [
            "keynote",
            "talk",
            "tutorial",
            "workshop",
            "sprint",
            "booth",
            "track",
        ]:
            involvement_metadata["url"] = input_url(
                f"{involvement_type} URL (leave blank if unavailable): ", event_url
            )

        involvement_metadata["date"] = input_date(
            (
                f"Start date of {involvement_type} at {event_name} "
                f"(e.g. 2026-01-01, leave blank if same as {event_name} start date): "
            ),
            event_start_date,
        )
        involvement_metadata["end_date"] = input_date(
            (
                f"End date of {involvement_type} (e.g. 2026-01-01; "
                f"leave blank if same as {involvement_type} start date): "
            ),
            involvement_metadata["date"],
        )

        if involvement_type in [
            "keynote",
            "talk",
            "tutorial",
            "workshop",
            "sprint",
            "booth",
            "track",
        ]:
            # if statement duplicated for the purposes of
            # preserving desired metadata order
            involvement_metadata["description"] = dedent(
                f"""\
                TODO: Remove this content and update with {involvement_type} description.

                Description should begin on the line below 'description: |-' with that line left intact.
                """  # noqa: E501
            )

        involvements.append(involvement_metadata)

        further_involvement = input("Is the team involved in another way? (y/N): ")
        more = further_involvement[:1].upper() == "Y"

    return {
        "title": f"We'll be at {event_name}!",
        "date": datetime.date.today(),
        "authors": sorted(authors),
        "categories": ["Events"],
        "event": {
            "name": event_name,
            "url": event_url,
            "date": event_start_date,
            "end_date": event_end_date,
            "description": dedent(
                """\
                TODO: Remove this content and update with event description.

                Description should begin on the line below 'description: |-' with that line left intact.
                """  # noqa: E501
            ),
        },
        "involvement": involvements,
    }


def request_resource_metadata():
    """Gather metadata for a resource post."""
    resource_metadata = {}

    resource_type = input_choice(
        "What type of resource are you adding?", ["Video", "Article", "Podcast"]
    )
    resource_metadata["type"] = resource_type.lower()

    resource_metadata["title"] = input("Resource title: ")
    resource_metadata["publication_date"] = input_date(
        "Resource publication date (e.g. 2026-01-01): "
    )
    resource_metadata["url"] = input_url("Resource URL: ")

    if resource_type == "video":
        resource_metadata["embeddable"] = True
        resource_metadata["event_name"] = input("Event name: ")
        resource_metadata["event_url"] = input_url("Event URL: ")

    resource_metadata["description"] = dedent(
        """\
        TODO: Remove this content and update with resource description.

        Description should begin on the line below 'description: |-' with that line left intact.
        """  # noqa: E501
    )

    authors = set()
    resource_authors = input(
        "Enter the GitHub user ID for everyone involved, separated by comma: "
    )
    resource_authors_list = sorted(
        [resource_author.strip() for resource_author in resource_authors.split(",")]
    )
    authors.update(resource_authors_list)

    content = {
        "title": resource_metadata["title"],
        "date": datetime.date.today(),
        "authors": [
            resource_author.strip() for resource_author in resource_authors.split(",")
        ],
        "categories": ["Resources"],
        "resource": resource_metadata,
    }

    return content


class NoAliasDumper(yaml.SafeDumper):
    """This is provided for two reasons:

    - Disables aliases (YAML's behavior of factoring out any repeated values as
      constants that are referenced.)
    - Ensures multiline strings are output with `|` syntax.
    """

    def ignore_aliases(self, data):
        return True

    def represent_str(self, data):
        if "\n" in data:
            return self.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        return super().represent_str(data)


yaml.add_representer(str, NoAliasDumper.represent_str, Dumper=NoAliasDumper)


def generate_entry(metadata, payload):
    """Generate a Markdown content file for a single entry."""
    if metadata["categories"] == ["Events"]:
        name = metadata["event"]["name"]
    else:
        name = metadata["title"]

    file_path = (
        Path(__file__).parent.parent
        / "docs/en/news/posts"
        / str(metadata["date"].year)
        / metadata["categories"][0].lower()
        / f"{re.sub(r'[^\w ]', '', name).lower().replace(' ', '-')}.md"
    )

    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.is_file():
        print("Post already exists.")
    else:
        # sort_keys stops it from sorting the already deliberately sorted metadata.
        # width stops it from wrapping strings at 80 characters.
        content = yaml.dump(metadata, Dumper=NoAliasDumper, sort_keys=False, width=9999)
        file_path.write_text(f"---\n{content}---\n{payload}")
    print(f"File created: {file_path}")


if __name__ == "__main__":
    post_type = input_choice(
        "What type of post are you adding?", ["Blog", "Event", "Resource"]
    )
    if post_type == "blog":
        metadata = request_blog_metadata()
        payload = dedent(
            """\

            Add blog post introduction here. Leave newline between frontmatter and content.

            <!-- more -->

            Add blog post content here.
            """  # noqa: E501
        )
    elif post_type == "event":
        metadata = request_event_metadata()
        payload = "\n{{ generate_event_post(authors, event, involvement, team) }}"
    elif post_type == "resource":
        metadata = request_resource_metadata()
        payload = "\n{{ generate_resource_post(resource) }}"

    generate_entry(metadata, payload)

    if post_type == "event":
        print()
        print("**********************************************************")
        print("* Don't forget to fill in long descriptions in the post! *")
        print("**********************************************************")
