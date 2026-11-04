print("STUDENT MARKS CALCULATOR")

name = input("Enter student name: ")

subjects = ["Tamil", "English", "Maths", "Science", "Computer"]
marks = []

for subject in subjects:
    mark = int(input("Enter " + subject + " mark: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")
