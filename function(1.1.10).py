# built in input and print function
name = input("input your name:")
print("Hello", name) # Hello name

print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0

# custom function
def hello():
    print("Hello World")
hello() # Hello World

def calculate_sum(a, b):
    print(a+b)
calculate_sum(3, 4) # 7
my_sum = calculate_sum(7, 4) # 11
print(my_sum) # None

def calculate_sum_1(a, b):
    return(a+b) # default return value is None
calculate_sum_1(3, 4) # no outout
my_sum_1 = calculate_sum_1(7, 4) # no output
print(my_sum_1) # 11

