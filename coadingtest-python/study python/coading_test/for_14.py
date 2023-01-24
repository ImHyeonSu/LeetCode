a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())

int_list = [a, b, c, d, e, f, g]
result_i = 0
result_odd = []
for i in int_list:
    if (i%2) == 1:
        result_i += i
        result_odd.append(i)

if len(result_odd) == 0:
    print(-1)
else:
    print(result_i)
    print(min(result_odd))