class MenuCommand:
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        commands = self.command_handler.get_registered_commands()
        return f"Available commands: {', '.join(commands)}"
