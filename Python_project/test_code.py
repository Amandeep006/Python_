def get_formatted_name(first,last,middle=""):
    """generate a neatly formatted full name."""
    if middle:
       full_name=f"{first} {middle} {last}"
    
    else:
        full_name=f"{first} {last}"

    return full_name.title()

# the dots(.) indicates that the function is defined in a separate file called test_code.py, and we are importing it into the current file (Test_name.py) so that we can use it to test its functionality.
"""sert a == b :Assert that two values are equal.
assert a != b :Assert that two values are not equal.
assert a :Assert that a evaluates to True.
assert not a :Assert that a evaluates to False.
assert element in list :Assert that an element is in a list.
assert element not in list :Assert that an element is not in a list"""
