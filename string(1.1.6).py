# string example
my_str_1 = 'Hello'
my_str_2 = "World"
print(my_str_1, my_str_2)
# multiline string
my_str_3 = '''multiline
string'''
my_str_4 = """another
multiline
string"""
print(my_str_3, my_str_4)
# single -><- double quotation
msg = "It's a sunny day"
msg1 = 'It\'s a sunny day'
quote = 'She said, "Hello world"'
quote1 = "She said, \"Hello world\""
print(msg, msg1, quote, quote1)
# string concatenation
my_str_5 = "hello"
my_str_6 = "world"
age = 56
str_plus_str = my_str_5 + " " + my_str_6 + " " + str(age)
print(str_plus_str) # str + int = error
my_str_7 = "jon"
my_str_7 += str(age)
print(my_str_7)
my_str_8 = f"my name is {my_str_7} and I am {age} years old"
print(my_str_8)
# length and indexing
my_str_9 = "hello world"
print(len(my_str_9)) # length 11
print(my_str_9[0], my_str_9[-1]) # first and last index h d
print(my_str_9[1:4], my_str_9[:4], my_str_9[8:],my_str_9[:]) # ell hell rld hello world
print(my_str_9[:5:2],my_str_9[::-1]) # start:stop:step
print("hello" in my_str_9, "f" in my_str_9) # True False


