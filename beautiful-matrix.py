row1 = input().split(' ')
row2 = input().split(' ')
row3 = input().split(' ')
row4 = input().split(' ')
row5 = input().split(' ')
mat = row1 + row2 + row3 + row4 + row5
matrix = [int(i) for i in mat]
a = matrix.index(1)
print(abs(a-12))


