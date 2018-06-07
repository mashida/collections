def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total

print("multiply(17,21): {}".format(multiply(17,21)))
