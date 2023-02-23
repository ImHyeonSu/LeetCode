a = int(input())
check_list = list()
i = 0
while i < a:
    check_list.append(int(input()))
    i += 1

check_list.sort()
result = 2*(check_list[3]-check_list[0])
print(result)

