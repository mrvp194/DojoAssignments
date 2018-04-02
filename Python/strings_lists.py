words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
new_words = words.replace('day', 'month')
print new_words
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
y = ["hello",2,54,-2,7,12,98,"world"
first = y[0]
last = y[len(y)-1]
new_list = [first, last]
z = [19,2,54,-2,7,12,98,32,10,-3,6]
tmp = z[:len(z)/2]
new_z = z[len(z)/2:]
new_z.insert(0,tmp)
print new_z