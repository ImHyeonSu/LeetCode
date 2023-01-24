a = int(input())
str_result = ""
str_result += str(a)
str_result += " "
while a > 1:
    if (a % 2) == 0:
        a //=2
        str_result += str(a)
        str_result += " "
    else:
        a *= 3
        a += 1
        str_result += str(a)
        str_result += " "

print(str_result)