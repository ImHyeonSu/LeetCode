a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
g = float(input())
h = float(input())
i = float(input())
j = float(input())
k = float(input())
l = float(input())

float_list = [a,b,c,d,e,f,g,h,i,j,k,l]
result = 0
for i in float_list:
    result += i

print("${g}".format(g=round((result/12),2)))
