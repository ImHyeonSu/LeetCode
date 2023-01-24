a, b, c = map(int, input().split())
gen_a = 0
counter = 0
if b > 0:
    while gen_a <c:
        if gen_a ==0:
            gen_a +=a
        else:
            gen_a += b
        counter +=1
        if gen_a == c:
            print(counter)
        elif gen_a > c:
            print("X")
    if a >= c:
        print("X")
else:
    gen_a = a
    while gen_a > c:
        gen_a +=b
        counter += 1
        if gen_a == c:
            counter += 1
            print(counter)
        elif gen_a < c:
            print("X")
