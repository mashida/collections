# 1. Takee a dictionary as an iterable in function
# 2. Count elements in each value of dictionary


treehouse = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
             'Kenneth Love': ['Python Basics', 'Python Collections', 'Awesome Python']}

#def num_teachers(dict_1):
#    num = 0
#    for key in dict_1:
#        num += 1
#        print("Key: {}, num: {}".format(key, num))
#    return num

#print("There are {} teachers.".format(num_teachers(treehouse)))

#def num_courses(dict_2):
#    num = 0
#    for key in dict_2:
#        num += len(dict_2[key])
#        print("Value: {}, len(value): {}".format(dict_2[key], len(dict_2[key])))
#    return num

#print("There are {} courses.".format(num_courses(treehouse)))

#def courses(dict_3):
#    c_list = []
#    for key in dict_3:
#        c_list.extend(dict_3[key])
#    return c_list
#
#print(courses(treehouse))

#def most_courses(dict_4):
#    max = 0
#    name = ''
#    for key in dict_4:
#        if max < len(dict_4[key]):
#            max = len(dict_4[key])
#            name = key
#    return name

#print(most_courses(treehouse))

def stats(dict_5):
    s_list = []
    for key in dict_5:
        s_list.append([key, len(dict_5[key])])
    return s_list

print(stats(treehouse))
