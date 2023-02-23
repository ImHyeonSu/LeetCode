a, b = map(int, input().split())

one_result = 0
tow_result = 0
counter = 0

for i in range(1, a+b, 1):
    if (a%i)==0 and (b%i) == 0:
        one_result = i
while tow_result <= 0:
    counter +=1
    if (a*counter)%b == 0:
        tow_result = (a*counter)

print(one_result,tow_result)