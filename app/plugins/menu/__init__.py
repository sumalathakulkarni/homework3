
import sys
from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        commands = self.command_handler.get_registered_commands()
        return f"Available commands: {', '.join(commands)}"
