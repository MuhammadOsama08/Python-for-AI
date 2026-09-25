class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        if not self.marks:
            return 0
        mean_marks = sum(self.marks) / len(self.marks)
        return mean_marks 

    def grade(self):
        avg = self.average()  # Grade average marks par nikaly ga
        
        if avg >= 80 and avg <= 100:
            print(f"{self.name}, your grade is A")

        elif avg < 80 and avg >= 70:
            print(f"{self.name}, your grade is B")

        elif avg < 70 and avg >= 60:
            print(f"{self.name}, your grade is C")

        else:
            print(f"{self.name}, You Are Fail. Are you from Sidra University?")


# Sahi tarika object bananay ka (Name string mein aur marks list mein)
fatima = Students("Fatima", [85, 92, 78])

print(f"Student Name: {fatima.name}")
print(f"Average Marks: {fatima.average()}")
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def average(self):
        if not self.marks:
            return 0
        mean_marks = sum(self.marks) / len(self.marks)
        return mean_marks 

    def grade(self):
        avg = self.average()  # Grade average marks par nikaly ga
        
        if avg >= 80 and avg <= 100:
            print(f"{self.name}, your grade is A")

        elif avg < 80 and avg >= 70:
            print(f"{self.name}, your grade is B")

        elif avg < 70 and avg >= 60:
            print(f"{self.name}, your grade is C")

        else:
            print(f"{self.name}, You Are Fail. Are you from Sidra University?")


# Sahi tarika object bananay ka (Name string mein aur marks list mein)
fatima = Students("Fatima", [85, 92, 78])

print(f"Student Name: {fatima.name}")
print(f"Average Marks: {fatima.average()}")
fatima.grade()

