a, b, c = map(int, input().split())

result_list = [a,b,c]
result_list.sort()
re_list = []
for i in result_list:
    re_list.append(i - result_list[0])

if (re_list[1] - re_list[0]) == (re_list[2] - re_list[1]):
    result_list.append(result_list[2]+(re_list[1] - re_list[0]))
    print(result_list[3])
elif (re_list[1] - re_list[0]) > (re_list[2] - re_list[1]):
    result_list.append(result_list[0]+(re_list[2] - re_list[1]))
    result_list.sort()
    print(result_list[1])
elif (re_list[1] - re_list[0]) < (re_list[2] - re_list[1]):
    result_list.append(result_list[1]+(re_list[1] - re_list[0]))
    result_list.sort()
    print(result_list[2])