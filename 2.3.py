def calculate_final_grade(student, submission_rate):
    if submission_rate.get(student['name'], 0) >= 4:
        assignment_avg = sum(student['assignment']) / len(student['assignment']) if student['assignment'] else 0
        lab_avg = sum(student['lab']) / len(student['lab']) if student['lab'] else 0
        test_avg = sum(student['test']) / len(student['test']) if student['test'] else 0

        final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
    else:
        final_grade = 0

    student['final_grade'] = final_grade
    return student

student1 = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
submission_rate = {'Adam': 6}
print(calculate_final_grade(student1, submission_rate))

student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2]}
submission_rate = {'Adam': 6, 'Kevin': 3}
print(calculate_final_grade(student2, submission_rate))