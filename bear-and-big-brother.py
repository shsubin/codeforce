inp = input().split(' ')
a = [int(i) for i in inp]
temp = 0
while a[0] <= a[1]:
	a[0] = a[0]*3
	a[1] = a[1]*2
	temp += 1
print(temp)