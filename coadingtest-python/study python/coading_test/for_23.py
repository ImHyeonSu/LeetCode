a = int(input())

result = 0
for i in range(1,a,1):
    if (a%i) == 0:
        result +=i

if result == a:
    print("yes")
else:
    print("no")