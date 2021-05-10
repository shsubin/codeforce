inp = int(input())
b = 'that I love '
a = 'that I hate '
c = 'that I love that I hate '

if inp == 1:
    print('I hate it')
else:
    if inp%2==0:
        print('I hate ' + c*((inp//2)-1) + b + 'it')
    else:
        print('I hate ' + c*((inp//2)-1) + c + 'it')
