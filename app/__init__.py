from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand
from app.commands.menu import MenuCommand

#add, subtract, multiply, and divide

class App:
    def __init__(self,  input_func=input, output_func=print): # Constructor
        self.command_handler = CommandHandler()
        self.input_func = input_func  # Allow input function to be passed for testability
        self.output_func = output_func


    def start(self):
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command('exit', ExitCommand())

        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

        print(self.command_handler.commands["menu"].execute())

        print("Type 'exit' to exit.")
        while True:
            try:
                user_input = input(">>> ").strip()
                if user_input == 'exit':
                    print("Exiting...")
                    break
                self.command_handler.execute_command(user_input)
            except Exception as e:
                print(f"An error occurred: {e}")