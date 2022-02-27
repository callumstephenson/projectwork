a = 1
b = 2
c = 2
while c <= 4000000:
    a,b = b, a+b
    if b % 2 == 0:
        c += b
print(c)