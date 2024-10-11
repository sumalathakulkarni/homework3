
import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        print("Exiting...")  # Ensure the message is printed
        sys.exit(0)  # Exit after printing the message