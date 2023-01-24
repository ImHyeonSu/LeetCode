a, b, c, d, e, f, g = map(int, input().split())

int_list = [a, b, c, d, e, f, g]
result = a
for i in int_list:
    if i > result:
        pass
    else:
        result = i


print(result)
