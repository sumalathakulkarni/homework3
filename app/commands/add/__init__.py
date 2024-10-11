 
import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import add, subtract
from decimal import Decimal

class AddCommand:
    def execute(self, *args):
        if len(args) != 2:
            return "Add Command requires two arguments."
        try:
            a, b = Decimal(args[0]), Decimal(args[1])
            calc = Calculation(a, b,add)
            return f"Add Command result for inputs {a}, {b} is {calc.perform()}"

        except ValueError:
            return "Invalid numbers provided."
