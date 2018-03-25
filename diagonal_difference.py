size = int(input())
matrix=[]

# reading input
for _ in range(size):
    row=list(map(int, input().split()))
    matrix.append(row)
print(matrix)

#print(matrix[-1][0])
#print(matrix[-2][1])
#print(matrix[-3][2])

# initialize s1 for right diagonal and s2 for left diagonal

s1, s2= 0,0

for i in range(size):
    s1+=matrix[i][i]
    s2+=matrix[-i-1][i]

print (abs(s1-s2))
