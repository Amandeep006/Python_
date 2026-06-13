class AnonymousSurvey:
    """Collect anonymous answers to a surveys questions."""

    def __init__(self, questions):
        """Store a question, and prepare to store responses """
        self.questions = questions
        self.responses=[]

    def show_questions(self):
        """Show the  survey questions."""
        print(self.questions)

    def store_responses(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_result(self):
        """Show all the responses that have been given."""
        print("Survey results :")
        for response in self.responses :
            print(f"- {response}")