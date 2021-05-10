inp = int(input())
if inp % 2 != 0:
    a = -((inp+1)//2)
        # a += ((-1)**i)*i
else:
    a = inp//2
print(a)
