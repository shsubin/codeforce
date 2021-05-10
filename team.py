inp = int(input())
temp = 0
for i in range(inp):
	abc = input()
	a = int(abc[0])
	b = int(abc[2])
	c = int(abc[4])
	if a == b == c == 1:
		temp += 1
	elif a == b == 1 or b == c == 1 or a == c == 1:
		temp += 1
print(temp)