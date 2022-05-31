import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dataframe = pandas.DataFrame(student_dict)

# print(student_dataframe)

# for (key, val) in student_dataframe.items():
#     print(key)

for (index, row) in student_dataframe.iterrows():
    print(row.student, int(row.score), 'in row', index)