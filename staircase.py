

def staircase(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end='')
        for k in range(i):
            print("#", end='')
        print()


n=int(input())
staircase(n+1)
