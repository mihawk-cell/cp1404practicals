"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_10.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format phrase as a sentence with capital and period.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('hELLo WoRLd')
    'Hello world.'
    """
    phrase = phrase.strip()
    phrase = phrase[0].upper() + phrase[1:].lower()
    if not phrase.endswith("."):
        phrase += "."
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail if repeat_string is wrong
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test if Car sets the fuel correctly (given value)
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when value provided"

    # Test default fuel
    car = Car()
    assert car.fuel == 0, "Car does not set default fuel correctly"


run_tests()

# Enable doctests
doctest.testmod()

