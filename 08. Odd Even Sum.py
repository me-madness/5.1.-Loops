import math

n = int(input())
even_sum = 0
odd_sum = 0

for i in range(1, n+1):
    num = float(input())
    if i %2 == 0:
        even_sum += num
    else:
        odd_sum += num
        
if even_sum == odd_sum:
    print('Yes, sum = %d' % even_sum)    
else:
    print('No, diff = %d' % math.fabs(odd_sum - even_sum))            