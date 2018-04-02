# multiples part 1
for num in range(1, 1000, 2) :
    print num

# multiples part 2
for num in range(5, 1000005, 5) :
    print num

# sum list
a = [1, 2, 5, 10, 255, 3]
sum1 = 0
for num in a :
    sum1 += num
print sum1

# average list
b = [1, 2, 5, 10, 255, 3]
sum2 = 0
for num in b :
    sum2 += num
avg = sum2/len(b)
print avg
