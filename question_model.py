class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def get_question(self):
        return [{"Text": self.text, "Answer": self.answer}]
