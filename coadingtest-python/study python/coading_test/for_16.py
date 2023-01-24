a = int(input())
result = 0
count = 1
while result <= a:
    result += count
    count += 1
    if result == a:
        print(count-1)