student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for thing in student_scores:
    if student_scores[thing] >= 91 and student_scores[thing] <= 100:
        student_scores[thing]="Outstanding"
        student_grades[thing]=student_scores[thing]
    elif student_scores[thing] >= 81 and student_scores[thing] <= 90:
        student_scores[thing]="Exceeds Expectations"
        student_grades[thing]=student_scores[thing]
    elif student_scores[thing] >= 71 and student_scores[thing] <= 80:
        student_scores[thing]="Acceptable"
        student_grades[thing]=student_scores[thing]
    elif student_scores[thing] <= 70:
        student_scores[thing]="Fail"
        student_grades[thing]=student_scores[thing]
# 🚨 Don't change the code below 👇
print(student_grades) 