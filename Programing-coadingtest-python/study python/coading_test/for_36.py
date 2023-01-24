a = float(input())

length_i = 0
count_i = 1
while length_i <= a:
    for i in range(1,count_i+1,1):
        length_i +=1/(i+1)
    if length_i < a:
        count_i += 1
        length_i = 0
    else:
        print("{a} card(s)".format(a=count_i))