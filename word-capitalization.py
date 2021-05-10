inp = input()
lst = [word[0].upper() + word[1:] for word in inp.split()]
inp = " ".join(lst)
print(inp)
