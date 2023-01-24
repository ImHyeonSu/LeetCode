a, b, c, d, e = map(int, input().split())

int_list = [a,b,c,d,e]
result_i = 0
for i in int_list:
    result_i += (i**2)
result_i %= 10
print(result_i)