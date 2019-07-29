class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        total = 0
        length = len(self.scores)
        for i in self.scores:
            total += i
        avg_score = total/length

        if 90 <= avg_score <= 100:
            return "O"
        elif 80 <= avg_score < 90:
            return "E"
        elif 70 <= avg_score < 80:
            return "A"
        elif 55 <= avg_score < 70:
            return "P"
        elif 40 <= avg_score < 55:
            return "D"
        elif 40 > avg_score:
            return "T"
