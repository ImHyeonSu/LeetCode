a, b, c, d, e, f, g, h, i, j = map(int, input().split())

int_list = [a, b, c, d, e, f, g, h, i, j]
result_sum = 0
result_max = a
result_min = a
for i in int_list:
    result_sum += i
    if i > result_max:
        result_max = i
    if i < result_min:
        result_min = i
print(result_sum, result_max, result_min)