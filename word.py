inp = input()
lower = 0
upper = 0
for i in inp:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1

if lower >= upper:
    print(inp.lower())
else:
    print(inp.upper())

