student = {
    'name': 'Adam',
    'assignment': [82, 56, 44, 30],
    'test': [78, 77],
    'lab': [78.2, 77.2]
}

submission_count = len(student['assignment']) + len(student['test']) + len(student['lab'])
submission_check = {student['name']: submission_count}

print(submission_check)