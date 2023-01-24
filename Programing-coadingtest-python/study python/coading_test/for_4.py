
a = int(input())

if a >= 2 & a <= 9:
    for i in range(1,10,1):
        print("{gg}*{ggg}={gggg}".format(gg=a,ggg=i,gggg=(a*i)))
