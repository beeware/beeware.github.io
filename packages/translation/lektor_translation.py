# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from jinja2 import pass_context


@pass_context
def translate(context, string, bag_name="translate"):
    this = context["this"]
    bag = context["bag"]
    if trans := bag(f"{bag_name}.{this.alt}.{string}"):
        return trans

    return bag(f"{bag_name}.en.{string}")


class TranslationPlugin(Plugin):
    name = "Translation"
    description = "Add your description here."

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters["trans"] = translate
