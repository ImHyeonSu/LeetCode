# count = int(input())
# a = 0
# int_list = []
# while a < count:
#     b = int(input())
#     a += 1
#     int_list.append(b)
#
# max_i = int_list[0]
# min_i = int_list[0]
# for i in int_list:
#     if i > max_i:
#         max_i = i
#     if i < min_i:
#         min_i = i
# minus_i = max_i-min_i
# counter_max = 0
# counter_min = 0
# while minus_i > 17:
#     if minus_i > 17:
#         max_i -= 1
#         counter_max += 1
#     else:
#         print((counter_max**2)+(counter_min**2))
#     minus_i = max_i-min_i
#     if minus_i > 17:
#         min_i +=1
#         counter_min += 1
#     else:
#         print((counter_max**2)+(counter_min**2))
#     minus_i = max_i - min_i
# print((counter_max**2)+(counter_min**2))