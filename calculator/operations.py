
"""Calculation operations"""
from decimal import Decimal
# Defining the functions with type hints for input parameters and return output
def add(first_input: Decimal, second_input: Decimal) -> Decimal:
    """add operation"""
    return first_input + second_input

def subtract(first_input: Decimal, second_input: Decimal) -> Decimal:
    """subtract operation"""
    return first_input - second_input

def multiply(first_input: Decimal, second_input: Decimal) -> Decimal:
    """multiply operation"""
    return first_input * second_input

def divide(first_input: Decimal, second_input: Decimal) -> Decimal:
    """divide operation"""
    if second_input == 0:
        raise ValueError("Cannot divide by zero")
    return first_input / second_input
