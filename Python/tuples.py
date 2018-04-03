my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def to_tuple(obj) :
    arr = []
    for name, num in obj.items() :
        tup = (name, num)
        arr.append(tup)
    return arr

print to_tuple(my_dict)