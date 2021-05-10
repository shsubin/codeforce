inp = int(input())
output = []
for i in range(inp+1, 10000):
    if len(set(str(i))) == 4:
        output.append(i)
print(output[0])

