my_tuple = (1,2,3)
print(my_tuple)

my_second_tuple = 1, 2, 3
print(my_second_tuple)

my_third_tuple =(5)
print(my_third_tuple)

my_third_tuple_2 = (5,)
print(my_third_tuple_2)

my_fourth_tuple = tuple([1, 2, 3])
print(my_fourth_tuple)

# my_tuple[0] = 5 # TypeError: 'tuple' object does nt support item assignment
# my_tuple[0] += 2 # TypeError: 'tuple' object does not support item assignment
print(my_tuple[0])

tuple_with_a_list = (1, "apple", [3, 4, 5])
print("tuple_with_a_list: ", tuple_with_a_list)
# tuple_with_a_list[0] = 2 # TypeError: 'tuple' object does not support item assignment
# tuple_with_a_list[1] = "pear" # TypeError: 'tuple' object does not support item assignment
tuple_with_a_list[2][1] = 7
print("New tuple_with_a_list: ", tuple_with_a_list)
