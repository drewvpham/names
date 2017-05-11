students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def name(students):
    for i in range(len(students)):
        for key, value in students[i].iteritems():
            print value,
        print ''

name(students)


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

def namer(users):
    for type in users:
        print type
        count=0
        for people in users[type]:
            count+=1
            first=people['first_name']
            last=people['last_name']
            length=len(first)+len(last)
            print '{} - {} {} - {}'.format(count, first, last, length)



namer(users)
