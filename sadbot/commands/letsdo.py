"""Letsdo bot command"""

from typing import Optional

from sadbot.commands.interface import CommandsInterface
from sadbot.message import Message


class LetsdoBotCommand(CommandsInterface):
    """This is the letsdo bot command class"""

    @property
    def command_regex(self) -> str:
        """Returns the regex for matching letsdo commands"""
        return r"((!|\.)([Ll][Ee][Tt][Ss][Dd][Oo]\s+\w+))"

    @property
    def parsemode(self) -> Optional[str]:
        """Returns the command parsemode"""
        return None

    def get_reply(self, message: Optional[Message] = None) -> Optional[str]:
        """Returns letsdo"""
        this = message.text[8:]
        return (
            f"let's do {this}! {this} {this} toe "
            f"{this} banana fanna foe f{this[1:]} "
            f"me my moe m{this[1:]}, {this}"
        )
