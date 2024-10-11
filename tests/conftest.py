'''Generate test data'''
from decimal import Decimal
from faker import Faker

from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    ''' Define operation mappings for both Calculator and Calculation tests '''
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        first_input = Decimal(fake.random_number(digits=2))
        second_input = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        try:
            if operation_func.__name__ == 'divide' and second_input == Decimal('0'):
                expected = "Cannot divide by zero"
            else:
                expected = operation_func(first_input, second_input)
        except ZeroDivisionError:
            expected = "Cannot divide by zero"

        yield first_input, second_input, operation_name, operation_func, expected

def pytest_addoption(parser):
    ''' addoption method '''
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    ''' Check if the test is expecting any of the dynamically generated fixtures '''
    if {"first_input", "second_input", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(first_input, second_input, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for first_input, second_input, op_name, op_func, expected in parameters]
        metafunc.parametrize("first_input,second_input,operation,expected", modified_parameters)
