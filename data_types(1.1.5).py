# data types 
my_int_var = 10
print("integer:", my_int_var)
my_float_var = 10.5
print("float:", my_float_var)
my_complex_var = 6 + 4j
print("complex:", my_complex_var)
my_string_var = "hello"
print("string:", my_string_var)
my_boolean_var = True
print("boolean:", my_boolean_var)
my_set_var = {1, 6, 9}
print("set:", my_set_var)
my_dictionary_var = {"name": "Alice", "age": 25}
print("dictionary:", my_dictionary_var)
my_tuple_var = (1, 6, 9)
print("tuple:", my_tuple_var)
my_range_var = range(5)
print("range:", my_range_var)
my_list = [22, "hello world", 3.14, True]
print("list:", my_list)
my_none_var = None
print("None:", my_none_var)
# immutable variables string, int, float, bool, tuple, range
greeting = "hello"
greeting = "hi" #reassignment
print(greeting) #error if greeting[0] = "H"
# mutable variables lists and dictionary
nums = [7, 4, 9]
nums = [9, 0]
nums[0] = 6 #not error
print(nums)
# use of type() function
my_var_1 = "hello world"
my_var_2 = 43
print(type(my_var_1), type(my_var_2))
# all data type and variable type
my_integer_var = 10
print('Integer:', my_integer_var, '| Type:', type(my_integer_var))  # Integer: 10 | Type: <class 'int'>

my_float_var = 4.50
print('Float:', my_float_var, '| Type:', type(my_float_var))  # Float: 4.50 | Type: <class 'float'>

my_complex_var = 3 + 4j
print('Complex:', my_complex_var, '| Type:', type(my_complex_var))  # Complex: (3+4j) | Type: <class 'complex'>

my_string_var = 'hello'
print('String:', my_string_var, '| Type:', type(my_string_var))  # String: hello | Type: <class 'str'>

my_boolean_var = True
print('Boolean:', my_boolean_var, '| Type:', type(my_boolean_var))  # Boolean: True | Type: <class 'bool'>

my_set_var = {7, 5, 8}
print('Set:', my_set_var, '| Type:', type(my_set_var))  # Set: {7, 5, 8} | Type: <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var, '| Type:', type(my_dictionary_var))  # Dictionary: {'name': 'Alice', 'age': 25} | Type: <class 'dict'>

my_tuple_var = (7, 5, 8)
print('Tuple:', my_tuple_var, '| Type:', type(my_tuple_var))  # Tuple: (7, 5, 8) | Type: <class 'tuple'>

my_range_var = range(5)
print('Range:', list(my_range_var), '| Type:', type(my_range_var))  # Range: [0, 1, 2, 3, 4] | Type: <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print('List:', my_list, '| Type:', type(my_list)) # List: [22, 'Hello world', 3.14, True] | Type: <class 'list'>

my_none_var = None
print('None:', my_none_var, '| Type:', type(my_none_var))  # None: None | Type: <class 'NoneType'>

# check data types
if isinstance("21", str):
    print(1) # it will print 1
isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False

