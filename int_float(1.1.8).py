# int float basic operation
my_int_1 = 200
my_int_2 = 4
my_float_1 = 4.4
add = my_int_1 + my_int_2 + my_float_1
diff = my_int_1 - my_int_2 - my_float_1
product = my_int_1 * my_int_2 * my_float_1
div = my_int_1 / my_int_2 / my_float_1
print(add, diff, product, div)

# modulus operation
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulus:', mod_ints) # Integer Modulus: 8
print('Float Modulus:', mod_floats) # Float Modulus: 1.1999999999999993

# round values
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

# floor values
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0

# exponentiation or power
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3

# changing data type 
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)  # 56.0
print(type(my_float_1))  # <class 'float'>

my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12
print(type(my_int))  # <class 'int'>

my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>

# absolute value
num = -15
absolute_value = abs(num)
print(absolute_value) # 15

# another numbering system
my_int = 56

binary_representation = bin(my_int)
print(binary_representation)  # 0b111000

octal_representation = oct(my_int)
print(octal_representation) # 0o70

hex_representation = hex(my_int)
print(hex_representation) # 0x38


