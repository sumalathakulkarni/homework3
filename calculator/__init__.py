
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
    def execute(first_input: Decimal, second_input: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Executes the operation"""
        calculation = Calculation.create(first_input, second_input, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(first_input: Decimal, second_input: Decimal) -> Decimal:
        """Performs addition operation"""
        return Calculator.execute(first_input, second_input, add)

    @staticmethod
    def subtract(first_input: Decimal, second_input: Decimal) -> Decimal:
        """Performs subtraction operation"""
        return Calculator.execute(first_input, second_input, subtract)

    @staticmethod
    def multiply(first_input: Decimal, second_input: Decimal) -> Decimal:
        """Performs multiplication operation"""
        return Calculator.execute(first_input, second_input, multiply)

    @staticmethod
    def divide(first_input: Decimal, second_input: Decimal) -> Decimal:
        """Performs division operation"""
        return Calculator.execute(first_input, second_input, divide)
