student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    grade = ''
    
    if student_scores[key] > 90:
        grade = "Outstanding"
        
    elif student_scores[key] > 80:
        grade = "Exceeds Expectations"
        
    elif student_scores[key] > 70:
        grade = "Acceptable"
        
    else:
        grade = "Fail"
    
    student_grades[key] = grade

for key in student_scores:
    print(key, " - ", student_scores[key], " - ", student_grades[key])
