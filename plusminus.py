from decimal import Decimal

def plusminus(n,ar):
    s1,s2,s3=0,0,0
    for i in range(n):
        if(ar[i]>0):
            s1+=1
        elif(ar[i]<0):
            s2+=1
        elif(ar[i]==0):
            s3+=1
#    print(Decimal(s1/n), float(s2/n), float(s3/n))
    print ('{0:.6f}'.format(s1/n))
    print ('{0:.6f}'.format(s2/n))
    print ('{0:.6f}'.format(s3/n))




n=int(input())
ar=[int(n) for n in input().split()]
print(ar)
result=plusminus(n,ar)
