steps = [5 * x for x in range(8, 21)]


def grader(num_grade):
    for grade in steps:
        if grade-num_grade < 3 and grade-num_grade > 0:
            return grade
    return num_grade


def main():
    for rep in range(int(input())):
        print(grader(int(input())))


if __name__ == '__main__':
    main()
