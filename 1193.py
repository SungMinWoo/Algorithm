user = int(input())
turn = 1
num = 0
while True:
    turn += num
    if user < b:
        if num % 2 != 0:
            start = user - (turn - num)
            numer = num - start
            denomi = start + 1
            break
        else:
            start = user - (turn - num)
            denomi = num - start
            numer = start + 1
            break
    num += 1
print(f'{numer}/{denomi}')