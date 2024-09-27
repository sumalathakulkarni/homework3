
"""Calculator class to perform a calculation and return the result."""
# Addressed all the coding standard errors raised by pylint in this class.

from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    """Calculator class creates and performs a calculation operation passed as a parameter and returns the result."""
    @staticmethod
    def execute(firstinput: Decimal, secondinput: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Executes the operation"""
        calculation = Calculation.create(firstinput, secondinput, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(firstinput: Decimal, secondinput: Decimal) -> Decimal:
        """Performs addition operation"""
        return Calculator.execute(firstinput, secondinput, add)

    @staticmethod
    def subtract(firstinput: Decimal, secondinput: Decimal) -> Decimal:
        """Performs subtraction operation"""
        return Calculator.execute(firstinput, secondinput, subtract)

    @staticmethod
    def multiply(firstinput: Decimal, secondinput: Decimal) -> Decimal:
        """Performs multiplication operation"""
        return Calculator.execute(firstinput, secondinput, multiply)

    @staticmethod
    def divide(firstinput: Decimal, secondinput: Decimal) -> Decimal:
        """Performs division operation"""
        return Calculator.execute(firstinput, secondinput, divide)
