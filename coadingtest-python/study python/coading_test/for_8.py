
a = int(input())
count = 0
str_result = ""
for i in range(1,a+1,1):
    count += i
    if i < a:
        str_result += str(i)
        str_result += "+"
    else:
        str_result += str(i)
        str_result += "="
        str_result += str(count)
print(str_result)