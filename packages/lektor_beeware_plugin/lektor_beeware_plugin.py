# -*- coding: utf-8 -*-
"""This is a custom local plugin to add extra functionality to the BeeWare site."""

from datetime import date

from lektor.pluginsystem import Plugin
from jinja2 import pass_context
import markdown
import requests


@pass_context
def translate(context, string, bag_name="translate"):
    # Make sure that any macros which need to call this are imported with context.
    alt = context["this"].alt
    bag = context["bag"]
    if trans := bag(f"{bag_name}.{alt}.{string}"):
        return trans

    if en := bag(f"{bag_name}.en.{string}"):
        return en

    return ""


@pass_context
def raw_github(context, path, repo, include_title=True):
    """
    Pull Markdown content from a raw-content GitHub link, convert it to HTML for
    inclusion in a Lektor template, using `raw_github` in the template.

    :param context: Lektor context.
    :param path: The path to the markdown file relative to the root of the GitHub repo.
    :param repo: The GitHub repo name.
    """
    raw_url = f"https://raw.githubusercontent.com/beeware/{repo}/refs/heads/main/{path}"
    content = requests.get(raw_url).text
    if not include_title:
        _, content = content.split("\n", 1)
    return markdown.markdown(content)


class BeeWarePlugin(Plugin):
    name = "BeeWare Custom Lektor Plugin"
    description = "This is a custom local plugin to add extra functionality."

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals["today"] = date.today()
        self.env.jinja_env.filters["trans"] = translate
        self.env.jinja_env.filters["raw_github"] = raw_github
