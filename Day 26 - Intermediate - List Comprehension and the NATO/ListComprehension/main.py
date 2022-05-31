# 💪 This exercise is HARD
#
# Instructions
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained:
#
# 1
# 2
# 3
# and file2.txt contained:
#
# 2
# 3
# 4
# result = [2, 3]
#
# IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
def sanitize(test_list):
    res = []
    [res.append(x) for x in test_list if x not in res]
    return res

with open('file1.txt') as f:
    file_one_data = sanitize([int(number) for number in f.read().strip().split('\n')])
with open('file2.txt') as f:
    file_two_data = sanitize([int(number) for number in f.read().strip().split('\n')])
result=[number for number in file_one_data if number in file_two_data]
# Write your code above 👆

print(result)