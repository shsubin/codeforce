# inp = input().split(' ')
# a = [int(i) for i in inp]
a = [1000000000, 9]
# a = [512, 4]
b = a[0]
for i in range(a[1]):
	if b % 10 == 0:
		b = b//10
		print(b)
	while b % 10 != 0:
		b -= 1
		print(b)


# print(b)