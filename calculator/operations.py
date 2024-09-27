
"""Calculation operations"""
from decimal import Decimal
# Defining the functions with type hints for input parameters and return output
def add(firstinput: Decimal, secondinput: Decimal) -> Decimal:
    """add operation"""
    return firstinput + secondinput

def subtract(firstinput: Decimal, secondinput: Decimal) -> Decimal:
    """subtract operation"""
    return firstinput - secondinput

def multiply(firstinput: Decimal, secondinput: Decimal) -> Decimal:
    """multiply operation"""
    return firstinput * secondinput

def divide(firstinput: Decimal, secondinput: Decimal) -> Decimal:
    """divide operation"""
    if secondinput == 0:
        raise ValueError("Divide by zero error")
    return firstinput / secondinput
