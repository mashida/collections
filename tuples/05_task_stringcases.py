def stringcases(string):
    return(tuple([string.upper(),
                 string.lower(),
                 string.title(),
                 string[::-1]]))

print(stringcases("NiKiTa"))
