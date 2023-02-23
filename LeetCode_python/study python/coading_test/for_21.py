
a, b = map(int, input().split())

count =0
result_list = []
for i in range(1,a+1,1):
    if (a%i) == 0:
        result_list.append(i)

if len(result_list) < b :
    print(0)
else:
    print(result_list[b - 1])