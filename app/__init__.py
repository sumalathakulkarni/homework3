import os
import pkgutil
import importlib
from app.commands import CommandHandler, Command
import logging
import logging.config

#add, subtract, multiply, and divide

class App:
    def __init__(self,  input_func=input, output_func=print): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        self.command_handler = CommandHandler()
        self.input_func = input_func  # Allow input function to be passed for testability
        self.output_func = output_func

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            if plugin_name == "menu": #pass command_handler for the menu plugin
                                self.command_handler.register_command(plugin_name, item(self.command_handler))
                            else: 
                                self.command_handler.register_command(plugin_name, item())
                            logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
    def start(self):
        # Register commands here
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:
            try:
                user_input = input(">>> ").strip()
                self.command_handler.execute_command(user_input)
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                print(f"An error occurred: {e}")