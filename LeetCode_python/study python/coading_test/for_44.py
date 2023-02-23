a, b = map(int, input().split())

result_i = 0
for i in range(1, a+b, 1):
    if (a%i) == 0 and (b%i)== 0:
        result_i = i

if result_i == 1:
    print("yes")
else:
    print("no")