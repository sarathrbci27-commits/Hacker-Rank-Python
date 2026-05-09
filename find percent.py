if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_marks[name] = marks

    query_name = input()

    # Calculate the average marks for the query_name
    avg_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    # Print the average marks with two decimal places
    print(f"{avg_marks:.2f}")
