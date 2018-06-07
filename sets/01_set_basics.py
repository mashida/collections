def line():
    print("="*60)

a = set([1, 3, 5])
print(a)
print(set([1, 3, 5]))
print({1, 3, 5})

line()

print(type({}))
print(type({1, 3, 5}))
print(type(set()))

print({1, 11, 13, 7, 5, 3})

low_primes = {1, 3, 5, 7, 11, 13}
print(low_primes)

line()

low_primes.add(17)
print(low_primes)

low_primes.update({19, 23}, {2, 29})
print(low_primes)

line()

low_primes.add(15)
print(low_primes)
low_primes.remove(15)
print(low_primes)

try:
    low_primes.remove(100)
except KeyError as err:
    print("KeyError: {} while removing '100'".format(err))

print(low_primes)

# Удаление возможно не существующего элемента без вызова ошибки
low_primes.discard(100)

line()

while low_primes:
    print(low_primes.pop()/3)
