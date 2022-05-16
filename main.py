import os

# Parent Directory path
parent_dir = "D:/PycharmProjects/100-Days-of-Python/"

for i in range(1,101):
    # Path
    path = os.path.join(parent_dir, 'Day '+str(i))
    os.mkdir(path)