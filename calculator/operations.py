
"""Calculation operations"""
from decimal import Decimal
import logging
# Defining the functions with type hints for input parameters and return output
def add(first_input: Decimal, second_input: Decimal) -> Decimal:
    """add operation"""
    logging.info(f"Performing add operation for ({first_input},{second_input})")
    return first_input + second_input

def subtract(first_input: Decimal, second_input: Decimal) -> Decimal:
    """subtract operation"""
    logging.info(f"Performing subtract operation for ({first_input},{second_input})")
    return first_input - second_input

def multiply(first_input: Decimal, second_input: Decimal) -> Decimal:
    """multiply operation"""
    logging.info(f"Performing multiply operation for ({first_input},{second_input})")
    return first_input * second_input

def divide(first_input: Decimal, second_input: Decimal) -> Decimal:
    """divide operation"""
    if second_input == 0:
        logging.info("Cannot divide by zero")
        raise ValueError("Cannot divide by zero")
    logging.info(f"Performing divide operation for ({first_input},{second_input})")
    return first_input / second_input
