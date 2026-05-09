if __name__ == '__main__':
    students = []

    # Read the number of students
    n = int(input())

    # Read the students' names and grades
    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])

    # Find the unique grades and sort them
    unique_grades = sorted(set([grade for name, grade in students]))

    # Find the second lowest grade
    second_lowest_grade = unique_grades[1]

    # Find the names of students with the second lowest grade
    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]

    # Sort the names alphabetically
    second_lowest_students.sort()

    # Print the names
    for name in second_lowest_students:
        print(name)
