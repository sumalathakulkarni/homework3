"""Creates the calculations class to maintain the history"""
from typing import List

from calculator.calculation import Calculation

class Calculations:
    """Calculations class to maintain the history of previous operations"""
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
    