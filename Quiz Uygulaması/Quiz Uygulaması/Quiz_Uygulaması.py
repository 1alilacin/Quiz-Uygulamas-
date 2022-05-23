class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionsIndex=0
    def getQuestion(self):
        return self.quiz.questions[self.questionsIndex]
    def displayQuestion(self):
        quesiton=self.getQuestion()
        print(f"soru {self.questionIndex +1}:{question.text}")

        for q in question.choices:
            print("-",q)

        answer =input("cevap:")
        self.guess(answer)
    def guess(self,answer):
        question=self.getQuestion()
        if quesiton.checkAnswer(answer):
            self.score+=1
        self.questionsIndex +=1
        self.displayQuestion()
q1=Question("En iyi proglamlama dili hangisidir ?",["C#","Python","Javascript","java"],"Python")
q2=Question("En popüler proglamlama dili hangisidir ?",["C#","Python","Javascript","java"],"Python")
q3=Question("En çok kazandıran proglamlama dili hangisidir ?",["C#","Python","Javascript","java"],"Python")
questions=[q1,q2,q3]

quiz=Quiz(questions)
quesiton=quiz.getQuestion