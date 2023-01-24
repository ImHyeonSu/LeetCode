a, b, c, d, e, f, g = map(int, input().split())

int_list = [a, b, c, d, e, f, g]
result_max = 0
result_min = a
for i in int_list:
    if i >= result_min:
        if i > result_max:
            result_max = i
    else:
        result_min = i


print(result_max, result_min)
