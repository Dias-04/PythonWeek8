student1 = {
    'name': 'Adam',
    'assignment': [82, 56, 44, 30],
    'test': [78, 77],
    'lab': [78.2, 77.2],
    'final_grade': 70.25
}

student2 = {
    'name': 'Kevin',
    'assignment': [82, 30],
    'test': [],
    'lab': [78.2],
    'final_grade': 0
}

students = {}
for student in [student1, student2]:
    name = student['name']
    students[name] = {
        'assignment': student['assignment'],
        'test': student['test'],
        'lab': student['lab'],
        'final_grade': student['final_grade']
    }

print(students)
