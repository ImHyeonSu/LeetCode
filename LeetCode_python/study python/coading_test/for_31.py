a = 0
float_list = []
while a < 999:
    a = float(input())
    float_list.append(a)

for i in range(0,len(float_list),1):
    result_i = 0
    if i == 0:
        pass
    elif i != (len(float_list)-1):
        result_i = float_list[i] - float_list[i-1]
        print('{:.2f}'.format(result_i))
    else:
        print("End of Output")