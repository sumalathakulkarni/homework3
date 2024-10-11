from decimal import Decimal
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, input_str):
        # Extract the command and its arguments from the input
        tokens = input_str.split()
        if not tokens:
            print("No command entered.")
            return
        
        command_name = tokens[0]
        args = tokens[1:]

        # Check if command is registered
        if command_name in self.commands:
            try:
                # Execute the command with any arguments
                result = self.commands[command_name].execute(*args)
                if result is not None:
                    print(result)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"Unknown command: {command_name}")
    
    def get_registered_commands(self):
        # Return the list of registered command names
        return list(self.commands.keys())
    
    