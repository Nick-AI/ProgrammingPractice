##This code is too inefficient to solve all test cases in the given timelimit
##I am currently working on an approach using matrix multiplication similar to how Fibonacci numbers can be
##calculated in O(logn) time with that technique

possible = 0

def staircase_helper(steps, walked):
    global possible
    if walked+1 < steps:
        staircase_helper(steps, walked+1)
    elif walked+1 == steps:
        possible += 1
    else:
        return
    if walked+2 < steps:
        staircase_helper(steps, walked+2)
    elif walked+2 == steps:
        possible += 1
    else:
        return
    if walked+3 < steps:
        staircase_helper(steps, walked+3)
    elif walked+3 == steps:
        possible += 1
    else:
        return



def main():
    global possible
    reps = int(input())
    for _ in range(reps):
        staircase_helper(int(input()), 0)
        print(possible)
        possible = 0

if __name__ == '__main__':
    main()
