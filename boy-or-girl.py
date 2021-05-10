inp = input()
a = []
for i in inp:
    a.append(i)
if len(set(a)) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')