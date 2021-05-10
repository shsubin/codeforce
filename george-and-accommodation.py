inp = int(input())
temp = 0
for i in range(inp):
    a = input().split(' ')
    inta = [int(b) for b in a]
    if inta[1]-inta[0]>=2:
        temp += 1
print(temp)
