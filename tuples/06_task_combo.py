def combo(var1, var2):
    list_1 = []
    for index in range(len(var1)):
        list_1.append((var1[index], var2[index]))
    return list_1

print(combo([1, 2, 3], 'abc'))
