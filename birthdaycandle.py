
def birthdaycandle(arr,x):
    max=arr[0]
    count=0
    for i in range(x):
        if(arr[i]>=max):
            max=arr[i]
    for i in range(x):
        if(arr[i]==max):
            count=count+1
    print(count)

x=int(input())
arr=[int(x) for x in input().split()]
birthdaycandle(arr,x)
