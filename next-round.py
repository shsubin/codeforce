inp = input().split(' ')
n = int(inp[0])
k = int(inp[1])
a = input().split(' ')
list = [int(i) for i in a]
# print(list)
temp = 0
for i in list:
    if i != 0 and i >= list[k-1]:
        temp += 1
print(temp)
