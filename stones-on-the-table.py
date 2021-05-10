inp = int(input())
color = input()
temp = 0
for i in range(inp+1):
    if i == inp - 1:
        break
    if color[i] == color[i+1]:
        temp += 1
print(temp)