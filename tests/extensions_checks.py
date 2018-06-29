import os

files = ["a.jpg", "b.c", "r.jpeg", "m.png", "d.txt"]

for file in files:
    extension = os.path.splitext(file)[1]
    if extension in [".jpg", ".jpeg", ".png"]:
        print("yes: ", extension)
    else:
        print("no: ", extension)
