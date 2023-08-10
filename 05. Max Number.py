n = int(input())
max_number = -10000000000000

for i in range(n):
    num = int(input())
    if num > max_number:
        max_number = num
        print('Max number = ' + str(max_number))
    