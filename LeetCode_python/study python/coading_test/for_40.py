
a = int(input())
int_list = []
counter = 1
result = 0
list_counter = 0
for i in range(a):
    int_list.append(counter)
    counter += 2


for i in range(0,len(int_list), 1):
    result += (int_list[i]*(int_list[len(int_list)-1-i]))

print(result)