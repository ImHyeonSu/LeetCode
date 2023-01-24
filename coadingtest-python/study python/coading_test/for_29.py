a = float(input())
float_list = []
while a > 0:
    float_list.append(a)
    a = float(input())

result_i = 0
for i in float_list:
    if i > 0:
        result_i = (i/5.988023952095808)
        print("Objects weighing {g} on Earth will weigh {gg} on the moon.".format(g='{:.2f}'.format(i),
                                                                                  gg='{:.2f}'.format(result_i)))
    else:
        pass




