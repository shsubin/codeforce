inp1 = input().split(' ')
inp2 = input().split(' ')

int1 = [int(i) for i in inp1]
int2 = [int(i) for i in inp2]
temp = 0
for i in int2:
    if i <= int1[1]:
        temp +=1
    elif i > int1[1]:
        temp+=2
print(temp)