import math
a = int(input())
str_a = list(str(a))

if len(str_a) >= 2 and (int(str_a[1]) == 4):
    if len(str_a) >= 3 and (int(str_a[2]) >= 4):
        a = round(a, -(len(str_a) - 1))
        a += (10**(len(str_a)-1))
        print(a)
    else:
        print(round(a, -(len(str_a) - 1)))
else:
    print(round(a, -(len(str_a) - 1)))