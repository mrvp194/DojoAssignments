sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def check_type(obj) :
    if isinstance(obj, int) :
        if obj >= 100 :
            print "That's a big number!"
        else :
            print "That's a small number"
    elif isinstance(obj, str) :
        if len(obj) >= 50 :
            print "Long sentence"
        else :
            print "Short sentence"
    elif isinstance(obj, list) :
        if len(obj) >= 10 :
            print "Big list!"
        else :
            print "Short list"

check_type(sI)
check_type(mI)
check_type(bI)
check_type(eI)
check_type(spI)
check_type(sS)
check_type(mS)
check_type(bS)
check_type(eS)
check_type(aL)
check_type(mL)
check_type(lL)
check_type(eL)
check_type(spL)