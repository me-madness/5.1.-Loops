n = int(input())
min_number = 10000000000000

for i in range(n):
    num = int(input())
    if num < min_number:
        min_number = num
        print('Min number = ' + str(min_number))
    