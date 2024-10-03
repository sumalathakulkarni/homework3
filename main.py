'''main functionality'''
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def calculate_and_print(first_input, second_input, operation_name):
    '''Perform calculation and print the result'''
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        first_input, second_input = map(Decimal, [first_input, second_input])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {first_input} {operation_name} {second_input} is equal to {result(first_input, second_input)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {first_input} or {second_input} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():

    print(len(sys.argv))
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, first_input, second_input, operation = sys.argv
    calculate_and_print(first_input, second_input, operation)

if __name__ == '__main__':
    main()
