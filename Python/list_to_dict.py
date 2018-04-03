name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2) :
    new_dict = {}
    if len(list2) > len(list1) :
        keys = list2
        values = list1
    else :
        keys = list1
        values = list2
    for index in range(len(values)) :
        new_dict[keys[index]] = values[index]
    return new_dict

print make_dict(name, favorite_animal)