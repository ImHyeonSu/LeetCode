
a = input()
a = int(a)
result_str = ""

for i in range(1,a+1,1):
    result_str += str(i)
    if i <a:
        result_str += " "
    else:
        pass
print(result_str)