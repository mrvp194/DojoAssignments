# Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_name(arr) :
    for obj in arr :
        print "{} {}".format(obj['first_name'], obj['last_name'])

print_name(students)

# Part 2

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_users(obj) :
    for key, arr in obj.items() :
        count = 0
        print key 
        for names in obj[key] :
            name_length = len("{}{}".format(names['first_name'], names['last_name']))
            count += 1
            print "{} - {} {} - {}".format(count, names['first_name'], names['last_name'], name_length)

print_users(users)    