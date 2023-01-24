a = 1
int_list = []
while a > 0:
    a = map(int, input().split())
    int_list.append(a)

A, B, C, D, F = 0, 0, 0, 0, 0
for i in int_list:
    if (i >= 90) and (i <=100):
        A +=1
    elif (i >= 80) and (i <=89):
        B +=1
    elif (i >= 70) and (i <=79):
        C +=1
    elif (i >= 60) and (i <=69):
        D +=1
    else:
        F +=1

print(len(int_list))
print(A)
print(B)
print(C)
print(D)
print(F)