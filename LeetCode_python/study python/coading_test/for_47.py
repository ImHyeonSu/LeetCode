a = int(input())
counter = 0
a = bin(a)
a = a[2:]
a = a[::-1]
result_list = []
for i in range(0,len(a),1):
    if a[i] == '1':
        result_list.append(i)
str1 = ""
for i in result_list:
    str1 += str(i)
    if i == result_list[len(result_list)-1]:
        pass
    else:
        str1 += " "
print(str1)