class StudentGrading:

  def __init__(self):


    self.grade = []
  def add_grade(self, grade):

    if 0 <= grade <= 100:

      self.grades.append(grade)

    else:

      print(f"{grade} is ignored (invalid)")



  def average_grade(self):

    if not self.grade:

      return 0

    return sum(self.grade) / len(self.grade)



  def point_grade(self):

    avg = self.average_grade()

    return ((100 - avg) + 10) / 10



  def remarks(self):

    avg = self.average_grade()

    if avg < 50:

      return "Dropped"

    elif avg < 75:

      return "Failed"

    elif 75 <= avg <= 79:

      return "Passed – Satisfactory"

    elif 80 <= avg <= 84:

      return "Passed – Good"

    elif 85 <= avg <= 89:

      return "Passed – Average"

    elif 90 <= avg <= 99:

      return "Passed – Very Good"

    elif avg == 100:

      return "Passed – Excellent"

    else:

      return "Invalid"



  def display_results(self):

    print("\nGrades Entered:", ", ".join(str(int(g)) if g.is_integer() else str(g) for g in self.grade))

    avg = self.average_grade()

    pt = self.point_grade()

    remark = self.remarks()

    print("Average =", round(avg, 2))

    print("Point Grade =", round(pt, 2))

    print("Remarks =", remark)


student = StudentGrading()
while True:

  try:

    grade = float(input("Enter grade: ( 1 - 60 ): "))

    if grade == -1:

      break

    student.add_grade(grade)

  except ValueError:

    print("Invalid input, please enter a number.")



  student.display_results()