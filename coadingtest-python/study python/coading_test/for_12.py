a, b, c, d, e, f, g = map(int, input().split())
int_list = [a, b, c, d, e, f, g]

before_b = a
result = 0
for i,b in enumerate(int_list):
    if b > before_b:
        before_b = b
        result = i
print(result+1)