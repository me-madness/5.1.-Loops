import math

n = int(input())
left_sum = 0
right_sum = 0


for i in range(0, n):
    numbers_for_left_side = float(input())
    left_sum += numbers_for_left_side
    
for i in range(2, n+2):
    numbers_for_right_side = float(input())    
    right_sum += numbers_for_right_side
    
if left_sum == right_sum:
    print('Yes, sum = %d' % left_sum)    
else:
    print('No, diff = %d' % math.fabs(right_sum - left_sum))    