
for i in range(1,10000+1,1):
    int_list = []
    before_i = i
    before_i_count = list(str(before_i))
    int_list = list(str(i**2))
    result_i = before_i
    result_i_b = ""
    for u in range((len(int_list) - len(before_i_count)),len(int_list),1):
        result_i_b += int_list[u]
    if result_i == int(result_i_b):
        print(result_i)
print