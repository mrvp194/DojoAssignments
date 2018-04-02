# input
word_list = ['hello','world','my','name','is','Anna']
char1 = 'o'
# output
# new_list = ['hello','world']

def find_characters(arr, char) :
    new_list = []
    for obj in arr :
        if obj.find(char) >= 0 :
            new_list.append(obj)
    print new_list

find_characters(word_list, char1)