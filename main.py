from time import sleep
print("Loading...")
sleep(.5)
print("Welcome!!!\n"
      "This is a CGPA Calculator created by GitHub user _tallCoder02\n"
      "_______________________________________________________________")
L = []
QualityPoints = []
TotalQualityPoints = 0
TotalCourseUnits = 0
x = ""
i = 1

try:
    while x != "N":
        print(f"Course No.:[{i}]")
        course_code = input("Course Code(e.g. FSC111)>> ")
        course_mark = int(input("Course Mark/Score(e.g. 70)>> "))
        course_units = int(input("Course Credit Units(e.g. 3)>> "))
        if 0 <= course_mark <= 39:
            grade_point = 0
        elif 40 <= course_mark <= 44:
            grade_point = 1
        elif 45 <= course_mark <= 49:
            grade_point = 2
        elif 50 <= course_mark <= 59:
            grade_point = 3
        elif 60 <= course_mark <= 69:
            grade_point = 4
        elif 70 <= course_mark <= 100:
            grade_point = 5
        L += [[course_code, course_mark, course_units, grade_point]]
        TotalCourseUnits += course_units
        TotalQualityPoints += (course_units * grade_point)
        QualityPoints.append(f"{course_units * grade_point}")
        i += 1
        x = input("Continue (Y or N): ")
        if x == 'N':
            break
        elif x == 'Y':
            pass

    CGPA = round(TotalQualityPoints/TotalCourseUnits, 2)
    print(f"CGPA: {CGPA}")

except ValueError or TypeError as e:
    print(f"Error message: {e}")
