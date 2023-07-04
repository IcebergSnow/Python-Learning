def factorial_iteration(num):
    the_factorial = num
    for i in range(2, num):
        the_factorial = the_factorial * i
    return the_factorial

def factorial_recursion(num):
    return 1 if num == 0 else num * factorial_recursion(num - 1)

def fibonacci_recursion(num):
    if num == 1:
        print(0)
        return [0,1]
    if num == 2:
        print(0)
        print(1)
        return [0,1]
    else:
        fiblist = fibonacci_recursion(num-1)
        current = fiblist[0]+fiblist[1]
        print(current)
        return [fiblist[1], current]
def fibonacci_interation(num):
    fiblist2 = [0, 0]
    for i in range(1, num+1):
        if i == 1:
            print(0)
        elif i ==2:
            print(1)
            fiblist2 = [0, 1]
        else:
            current2 = fiblist2[0] + fiblist2[1]
            print(current2)
            fiblist2[0] = fiblist2[1]
            fiblist2[1] = current2
