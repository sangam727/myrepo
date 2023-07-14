#this logic use for and if loop
total1 = 0 
for number in range(1,101):
    if number % 2 == 0:
        total1 += number
print(total1)


###this is other way 
total2 = 0
for number in range(2,101,2):
    total2 += number
print(total2)
