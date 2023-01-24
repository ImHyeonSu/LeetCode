count = int(input())
a = 0
b = 1
int_list = []
result_i =0
counte = 1
while a < count:
    int_list.append(b)
    b += 2
    a += 1
print(int_list)

for i in range(0,len(int_list),1):
    result_i += (int_list[i] + int_list[len(int_list) - counte])
    counte += 1
