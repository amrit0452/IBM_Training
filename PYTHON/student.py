name = "Amrit"
en_num = 1234
course = "Computer Science"
branch = "Software Engineering"
year_of_study = 4
gpa = 9.8


print("Name: ", name, "Enrollment Number: ", en_num, "Course: ", course)
print(f"Name: {name}, Enrollment Number: {en_num}, Course: {course} , Branch: {branch}")

coor = (5,6)
(x,y) = coor
print(f"Coordinates: x = {x}, y = {y}")

text = "     Python Programming    "

print(text.strip())  # Remove Leading and Trailing 
print(text.upper())  # Covert to uppercase
print(text.split())  # Split the text - returns list

print(f"Learning {text.strip()}") # f-strings
print(text[::-1])
print(text.replace("Python", "Java")) # Replace substring
print(text.strip()[7:])
print(text)