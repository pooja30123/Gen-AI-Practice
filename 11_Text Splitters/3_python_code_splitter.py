from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # Dictionary of subject: marks

    def calculate_average(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        average = total_marks / num_subjects
        return average

    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "F"

    def show_report(self):
        print(f"\nStudent: {self.name}")
        print("Marks:", self.marks)
        print("Average:", round(self.calculate_average(), 2))
        print("Grade:", self.get_grade())


# ✅ Example usage:
student1 = Student("Pooja", {"Math": 88, "Science": 92, "English": 85})
student2 = Student("Rahul", {"Math": 45, "Science": 40, "English": 39})

student1.show_report()
student2.show_report()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(chunks)
print(chunks[1 ])