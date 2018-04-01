
def minmax(arr,x):
    max=arr[0]
    min=arr[0]
    s=0
    for i in range(x):
        s=s+arr[i]
        if(arr[i]>max):
            max=arr[i]
        elif(arr[i]<min):
            min=arr[i]
    print(s-min, s-max)




x=5
arr=[int(x) for x in input().split()]
minmax(arr,x)
