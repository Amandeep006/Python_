"""TESTING A FUNCTION"""

from test_code import get_formatted_name

# print("ENter 'q' at any time to quit.")

# while True:
#     first=input("\nPlease give me a first name :")
#     if first =="q":
#         break

#     last=input("Please give me a last name :")
#     if last=="q":
#         break

#     formatted_name=get_formatted_name(first, last)
#     print(f"\t Neatly formatted name :{formatted_name}")



"""Unit Tests : It verifies that onw specific aspect of a function's behaviour is correct.
Test cases: It is a collection of units tests that together prove that a function behaves as it's supposedto, within the full renage of situations you expect it to handle.
"""

""" PASSING TEST """
# def test_first_last_name():
#     """Do names like 'Janis Joplin' work ? """
#     formatted_name=get_formatted_name("Janis","Joplin")
#     assert formatted_name=="Janis Joplin"

# Running Test : It is a good idea to run the test every time you make a change to the function, to make sure that the change doesn't break the function. You can run the test by calling the test function directly, or by using a testing framework like unittest or pytest.
# Failing Test : If the test fails, it will raise an AssertionError, and you will see a message that indicates which test failed and what the expected and actual values were. You can use this information to debug your code and fix the problem.

# def test_first_last_middle_name():
#     """Do names like 'Wolfgang AMadeus Mozart' work ?"""
#     formatted_name=get_formatted_name("Wolfgang","Mozart","Amadeus")
#     assert formatted_name=="Wolfgang Amadeus Mozart"