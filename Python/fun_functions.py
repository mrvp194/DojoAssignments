def odd_even() :
    for num in range(1,2001) :
        if num % 2 == 0 :
            print "Number is {}.  This is an even number.".format(num)
        else :
            print "Number is {}.  This is an odd number".format(num)

def multiply(arr, num) :
    for index in range(len(arr)) :
        arr[index] *= num
    return arr

def layered_multiples(arr) :
    new_array = []
    for num in arr :
        tmp = []
        for n in range(num) :
            tmp.append(1)
        new_array.append(tmp)
    return new_array

odd_even()
a = [2,4,10,16]
b = multiply(a, 5)
print b
x = layered_multiples(multiply([2,4,5],3))
print x