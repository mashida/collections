COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

#supplied_set = set(input("Enter your cover: "))

#def covers(supplied_set):
#    result = set()
#    for x in COURSES:
#        if COURSES[x] & supplied_set:
#            result.add(x)
#    return result

#print(result)

#print(covers(input("Enter your cover: ")))


#def covers_all(supplied_set):
#words = input("Enter: ")
#list1 = list(words)
supplied_set = set(input("Enter: "))
result = set()
print("Создал пустую переменную result")
for x in COURSES:
    print("Сравниваю {} с {}.".format(supplied_set, COURSES[x]))
    if supplied_set <= COURSES[x]:
        result.add(x)
#    return result

#print(covers_all(set(input("Enter: "))))

print("Result: {}".format(result))
