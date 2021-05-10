inp = int(input())
a = []
x = 0
for i in range(inp):
	b = input()
	a.append(b)
for c in a:
	if c == 'X++' or c == '++X':
		x+=1
	elif c == '--X' or c == 'X--':
		x-=1
print(x)