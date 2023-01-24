a = int(input())
result_i = 0

for i in range(1,a,1):
    if (a%i) == 0:
        result_i +=i

if result_i < a:
    print("  {a}  DEFICIENT".format(a=a))
elif result_i == a:
    print("  {a}  PERFECT".format(a=a))
else:
    print("  {a}  ABUNDANT".format(a=a))
