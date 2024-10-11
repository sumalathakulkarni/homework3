import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import add, subtract
from decimal import Decimal

class SubtractCommand:
    def execute(self, *args):
        if len(args) != 2:
            return "Add requires two arguments."
        try:
            a, b = Decimal(args[0]), Decimal(args[1])
            calc = Calculation(a, b,subtract)
            return f"Subtract Operation result for inputs {a}, {b} is {calc.perform()}"

        except ValueError:
            return "Invalid numbers provided."
        

         
import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import subtract
from decimal import Decimal

class SubtractCommand:
    def execute(self, *args):
        if len(args) != 2:
            return "Subtract Command requires two arguments."
        try:
            a, b = Decimal(args[0]), Decimal(args[1])
            calc = Calculation(a, b, subtract)
            return f"Subtract Command result for inputs {a}, {b} is {calc.perform()}"

        except ValueError:
            return "Invalid numbers provided."