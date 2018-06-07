def line():
    print("="*60)

a = 5
b = 20
print("a: {}, b: {}".format(a,b))

a, b = b, a
print("a: {}, b: {}".format(a, b))

a = 5
b = 20
c = b, a
print("c: {}".format(c))

line()

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print("add(5,5): {}".format(add(5,5)))
print("add(32): {}".format(add(32)))
print("add(5,5,18,34,19,22): {}".format(add(5,5,18,34,19,22)))

line()

def add(base, *args):
    total = base
    for num in args:
        total += num
    return total

print("add(5,20): {}".format(add(5,20)))
