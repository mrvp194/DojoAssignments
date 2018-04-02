def type_list(l) :
    string = ""
    num = 0
    str_instances = 0
    int_instances = 0
    for obj in l :
        if isinstance(obj, str) :
            string += (" " + obj)
            str_instances += 1
        elif isinstance(obj, int) or isinstance(obj, float) :
            num += obj
            int_instances += 1
        
    if str_instances > 0 and int_instances > 0 :
        print "the list you entered is of mixed type"
        print "String:" + string
        print "Sum: " + str(num)
    elif str_instances > 0 :
        print "The list you entered is of string type"
        print "String:" + string
    elif int_instances > 0 :
        print "The list you entered is of integer type"
        print "Sum: " + str(num)


l = ['magical unicorns',19,'hello',98.98,'world']
j = [2,3,1,7,4,12]
k = ['magical','unicorns']
type_list(l)
type_list(j)
type_list(k)