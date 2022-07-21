counts, won = map(int, input().split())

coin_list = [int(input()) for _ in range(counts)]
coin_list.sort(reverse=True)

count = 0
for a in range(len(coin_list)):
    if won / coin_list[a] < 1:
        pass
    else:
        count += int(won / coin_list[a])
        won = won % coin_list[a]

print(count)