a = int(input())
result_a = 0
result_b = 0
b = a+1
for i in range(1,a,1):
    result_a += i
while result_a > result_b:
    result_b += b
    b +=1

if result_a > result_b:
    print("X")
elif result_a == result_b:
    print("O")
elif result_a < result_b:
    print("X")