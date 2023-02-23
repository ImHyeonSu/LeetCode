a = int(input())
result_set = set()

for i in range(1,a+1,1):
    if (a % i) == 0:
        result_set.add(i)

if len(result_set) == 2:
    print("prime")
else:
    print("not prime")