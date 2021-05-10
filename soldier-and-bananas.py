inp = input().split(' ')
inter = [int(i) for i in inp]
a = 0
for i in range(1, inter[2]+1):
    a += inter[0]*i
loan = abs(a - inter[1])
if a <= inter[1]:
    print('0')
else:
    print(loan)
