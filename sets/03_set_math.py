def line():
    print("="*60)

set1 = set(range(10))
print("set1: {}".format(set1))

set2 = {1, 2, 3, 5, 7, 11, 13, 15, 17, 19, 23}
print("set2: {}".format(set2))

line()

# Lets use Union of that 2 sets: set1.union(set2)
# Calling Union - does not change set1. Calling Update does change set1 but does not resolve anything
print("Union of 2 sets: ", set1.union(set2))
print("set1: {}".format(set1))

# Using | instead of Union operand also worksL

print("Union of 2 sets using '|' symbol: ", (set1 | set2))

#print("Update of 2 sets: ", set1.update(set2))
#print("set1: {}".format(set1))

line()

#Lets use Difference method to show difference between 2 sets:

print("Difference of set1 from set2: ", set1.difference(set2))
print(set1)
print("Difference of set2 from set1: ", set2.difference(set1))
print(set2)

# Difference symbol is "-" so

print("Difference of set1 from set2 using '-' symbol: ", (set1 - set2))

line()

# symmetric difference using "^" symbol

print("Unique symbols of 2 sets using '^' symbol: ", (set1 ^ set2))

# or symmetric_difference method

print("Symmetric difference of 2 sets: ", set1.symmetric_difference(set2))

line()

#intrsection of 2 sets: using Intersectio method:

print("Intersection of 2 sets: ", set1.intersection(set2))

# operand for intersection is '&' symbol:

print("Intersection of 2 sets using '&' symbol: ", (set1 & set2))
