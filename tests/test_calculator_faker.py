'''Faker - Calculator Test'''
from decimal import Decimal
from faker import Faker
from calculator import Calculator

fake = Faker()
firstnumber = Decimal(fake.random_number(digits=2))
secondnumber = Decimal(fake.random_number(digits=2))
sumofnumbers = firstnumber + secondnumber
differenceofnumbers = firstnumber - secondnumber

def test_addition_faker():
    '''Faker Test that addition function works ''' 
    print (f'Faker Test Calculator.add({firstnumber},{secondnumber})')
    assert Calculator.add(firstnumber,secondnumber) == sumofnumbers

def test_subtraction_faker():
    '''Faker Test that subtraction function works '''
    print (f'Faker Test Calculator.subtract({firstnumber},{secondnumber})')
    assert Calculator.subtract(firstnumber,secondnumber) == differenceofnumbers
