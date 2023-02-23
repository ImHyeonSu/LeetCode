from math import ceil

a, b = map(int, input().split())

if (a%8) == 0 and (b%8) == 0:
    print("The number of whole tiles is {g} part tiles is 0".format(g=int((a/8)*(b/8))))
else:
    result = ceil(a/8)*ceil(b/8) - (a//8)*(b//8)
    print("The number of whole tiles is {g} part tiles is {gg}".format(g=(ceil(a / 8) * ceil(b / 8))-result, gg=result))
