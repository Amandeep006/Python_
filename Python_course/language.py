# from survey import AnonymousSurvey
# # Define a question, and make a survey.
# questions="What language did you first learn to speak ?"
# language_survey=AnonymousSurvey(questions)

# """Show the question, and store responses to the question."""
# language_survey.show_questions()
# print("Enter 'q' at any time to quit.\n")

# while True:
#     response=input("Language :")
#     if response =="q":
#         break

#     language_survey.store_responses(response)


# # Show the survey results.
# print("\n Thank you to everyone who partiipated in the survey !")
# language_survey.show_result()

"""TESTING THE ANONYMOUSSURVEY CLASS"""

# from survey import AnonymousSurvey

# def test_store_single_responses():
#     # Test that a single response is stored properly.
#     questions="What language did you first learn to speak ?"
#     language_survey=AnonymousSurvey(questions)
#     language_survey.store_responses("English")
#     assert "English" in language_survey.responses


# def test_store_three_responses():
#     # Test that three individual responses are stored properly.
#     questions="What language did you first learn to speak ?"
#     language_survey=AnonymousSurvey(questions)
#     responses=["English","Spanish","Mandarin"]
#     for response in responses:
#         language_survey.store_responses(response)

#     for response in responses:
#         assert response in language_survey.responses



"""Using Fixtures : A fixture is a function that sets up a certain state or condition for the tests to run. It can be used to create objects, set up databases, or perform any other necessary setup before the tests are run. In pytest, you can use the @pytest.fixture decorator to define a fixture function, and then use it in your test functions by including it as an argument. This allows you to reuse the same setup code across multiple tests, making your tests more efficient and easier to maintain."""

import pytest
from survey import AnonymousSurvey
@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    questions="WHat language did you first learn to speak ?"
    language_survey=AnonymousSurvey(questions)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
     language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses