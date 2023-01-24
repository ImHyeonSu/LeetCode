a, b = map(int, input().split())

result_str = ""
if a> b:
    before_b = b
    b = a
    a = before_b
else:
    pass
for i in range(a,b+1,1):
    result_str += str(i)
    if i < b:
        result_str += " "
    else:
        pass
print(result_str)