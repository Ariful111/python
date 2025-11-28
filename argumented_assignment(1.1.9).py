# argumented assignment for int, float( ++ or -- have no mathmatical meaning in python )
my_int_1 = 10
my_int_1 += 5
print(my_int_1) # 15
my_int_1 -= 5
print(my_int_1) # 10
my_int_1 *= 5
print(my_int_1) # 50
my_int_1 /= 2
print(my_int_1) # 25
my_int_1 %= 9
print(my_int_1) # 7
my_int_1 //= 3
print(my_int_1) # 2
my_int_1 **= 5
print(my_int_1) # 32

# string only allows += and *= operations
my_str_1 = "Hello"
my_str_1 += " World"
print(my_str_1) # Hello World
my_str_2 = "World"
my_str_2 *= 3
print(my_str_2) # WorldWorldWorld