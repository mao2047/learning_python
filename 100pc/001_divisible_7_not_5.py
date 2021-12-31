multiple = []

for number in range (2000, 2301):
    if number % 5 != 0 and number % 7 == 0:
            multiple.append(number)

print(*multiple, sep = ', ')
