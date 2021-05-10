inp = int(input())
a = ''
for i in range(inp):
	a = a + input() + ' '
for ch in ['1 1','0 0']:
	if ch in a:
		a = a.replace(ch, ', ')
b = a.split(',')
print(len(b))