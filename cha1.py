# we are going to solve more challenge 
# the sum of all the multiples of 3 and 5 less then 1000

sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
    
print(sum)