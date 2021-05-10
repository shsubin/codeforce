inp = int(input())
a = input().split(' ')
b = [int(i) for i in a]
temp = 0
for i in b:
    if i == 1:
        temp += 1
if temp > 0:
    print('HARD')
else:
    print('EASY')