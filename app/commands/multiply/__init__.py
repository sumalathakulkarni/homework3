
import sys
from app.commands import Command


class MultiplyCommand(Command):
    def execute(self):
        print(f'I WIll send something to Multiply')


import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import multiply
from decimal import Decimal

class MultiplyCommand:
    def execute(self, *args):
        if len(args) != 2:
            return "Multiply Command requires two arguments."
        try:
            a, b = Decimal(args[0]), Decimal(args[1])
            calc = Calculation(a, b, multiply)
            return f"Multiply Command Operation result for inputs {a}, {b} is {calc.perform()}"

        except ValueError:
            return "Invalid numbers provided."
