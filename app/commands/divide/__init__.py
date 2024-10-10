import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import divide
from decimal import Decimal

class DivideCommand:
    def execute(self, *args):
        if len(args) != 2:
            return "Divide Command requires two arguments."
        try:
            a, b = Decimal(args[0]), Decimal(args[1])
            calc = Calculation(a, b, divide)
            return f"Divide Command Operation result for inputs {a}, {b} is {calc.perform()}"

        except ValueError:
            return "Invalid numbers provided."
