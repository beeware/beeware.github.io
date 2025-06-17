# -*- coding: utf-8 -*-
"""This is a custom local plugin to add extra functionality to the BeeWare site."""

from datetime import date

from lektor.pluginsystem import Plugin
from jinja2 import pass_context, Template
from markupsafe import Markup


@pass_context
def translate(context, string, bag_name="translate"):
    # Make sure that any macros which need to call this are imported with context.
    alt = context["this"].alt
    bag = context["bag"]
    result = ""
    if trans := bag(f"{bag_name}.{alt}.{string}"):
        result = trans

    if not result and (en := bag(f"{bag_name}.en.{string}")):
        result = en

    template = Template(result)
    
    # Wrapping it in Markup() marks it as safe, so it won't be escaped.
    return Markup(template.render(context))


def link_to(address):
    def link_maker(text):
        return f'<a href="{address}">{text}</a>'

    return link_maker


class BeeWarePlugin(Plugin):
    name = "BeeWare Custom Lektor Plugin"
    description = "This is a custom local plugin to add extra functionality."

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals["today"] = date.today()
        self.env.jinja_env.globals["link_to"] = link_to
        self.env.jinja_env.filters["trans"] = translate
