"""Calculation class to take two input parameters and an operation name to perform the calculation"""
from decimal import Decimal
from typing import Callable

class Calculation:
    """Calculation class will take two input parameters and an operation name to perform the calculation"""
    def __init__(self, firstinput: Decimal, secondinput: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Constructor method with type hints for parameters and the return type"""
        # Initialize parameters
        self.firstinput = firstinput
        self.secondinput = secondinput
        self.operation = operation

    @staticmethod
    def create(firstinput: Decimal, secondinput: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Alternative constructor"""
        return Calculation(firstinput, secondinput, operation)

    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        return self.operation(self.firstinput, self.secondinput)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.firstinput}, {self.secondinput}, {self.operation.__name__})"
           