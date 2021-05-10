inp = int(input())
for i in range(inp):
	string = input()
	if len(string) <= 10:
		print(string)
	else:
		a = len(string[1:-1])
		print(string[0] + str(a) + string[-1])