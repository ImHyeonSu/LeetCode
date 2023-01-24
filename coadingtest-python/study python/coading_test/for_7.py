a, b, c, d, e, f, g = map(int, input().split())

list_input = [a,b,c,e,d,f,g]
one_result = 0
two_result = 0
three_result = 0

for i in list_input:
    if i < 10:
        one_result += i
    elif (i >=10) & (i <100):
        two_result += i
    elif i >= 100:
        three_result +=i
print("{g} {gg} {ggg}".format(g=one_result, gg=two_result, ggg=three_result))
