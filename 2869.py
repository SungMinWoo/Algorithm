import math
day, night, height = map(int, input().split())

meter = 0

time = (height - night)/(day - night)

print(math.ceil(time))