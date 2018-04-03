info = {
    "name" : "Michael",
    "age" : 26,
    "country" : "The United States",
    "language" : "Python"
}

def print_info(obj) :
    for key, value in obj.items() :
        print "My {} is {}".format(key, value)

print_info(info)