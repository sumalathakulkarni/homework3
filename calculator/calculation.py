"""Calculation class to take two input parameters and an operation name to perform the calculation"""
from decimal import Decimal
from typing import Callable

class Calculation:
    """Calculation class will take two input parameters and an operation name to perform the calculation"""
    def __init__(self, first_input: Decimal, second_input: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Constructor method with type hints for parameters and the return type"""
        # Initialize parameters
        self.first_input = first_input
        self.second_input = second_input
        self.operation = operation

    @staticmethod
    def create(first_input: Decimal, second_input: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Alternative constructor"""
        return Calculation(first_input, second_input, operation)

    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        return self.operation(self.first_input, self.second_input)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.first_input}, {self.second_input}, {self.operation.__name__})"
           