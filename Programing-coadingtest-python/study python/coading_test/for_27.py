a = int(input())
result_i = 0
class gg():
    def mul_1(b: int) ->int:
        result_b = 1
        for i in range(2,b+1,1):
            result_b += i
        return result_b

for i in range(1,a+1,1):
    int_mul = gg.mul_1(i+1)
    result_i += (i*int_mul)

print(result_i)