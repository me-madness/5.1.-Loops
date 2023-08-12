letters = input().lower()
vowels_sum = 0

for i in letters:
    if i == 'a':
        vowels_sum += 1
    elif i == 'e':
        vowels_sum += 2    
    elif i == 'i':
        vowels_sum += 3
    elif i == 'o':
        vowels_sum += 4
    elif i == 'u':
        vowels_sum += 5

print(vowels_sum)                   