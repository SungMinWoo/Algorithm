import math

counts = int(input())

for count in range(counts):
    height, weight, num = map(int, input().split())
    room_num = num / height
    room_height = num % height
    if room_height == 0:
        room_height = height
    elif room_height == 1:
        room_height = room_height
    if room_num < 10 or room_num < 100:
        if math.ceil(room_num) == 10:
            room_num = math.ceil(room_num)
        elif room_num < 10:
            room_num = '0' + str(math.ceil(room_num))
        elif 10 < room_num < 100:
            room_num = math.ceil(room_num)
    elif room_num == 10:
        room_num = math.trunc(room_num)
    else:
        room_num = math.trunc(room_num)
    print(f'{room_height}{room_num}')
