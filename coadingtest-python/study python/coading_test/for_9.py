a, b, c, d, e, f, g = map(int, input().split())

int_list = [a, b, c, d, e, f, g]
result = 0
for i in int_list:
    if i > result:
        result = i


print(result)
