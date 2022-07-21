user = int(input()) - 1
incre = 0
step = 0
if user == 0:
    print(incre + 1)
else:
    while True:
        step += incre * 6
        incre += 1
        if user - step <= 0:
            break
    print(incre)