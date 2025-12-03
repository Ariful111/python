# local scope(doesn't alow accessing variables from outside of scope)
def my_func():
    my_var = 10
    print(my_var)
my_func() # 10

# enclosing scope(doesn't alow accessing variables fron inner scope to outer scope)
def outer_func():
    msg = "hello world"
    def inner_func():
        print(msg)
    inner_func()
outer_func() # hello world

    # use of nonlocal(reassign variables in nested function)
def outer_func_1():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope
    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()
    inner_func()
    print(res)  # Now res is accessible and modified
outer_func_1() # Hello there! # How are you?

# global variable(alow accessing from everywhere)
my_var = 100
def show_var():
    print(my_var)
show_var() # 100
print(my_var) # 100

    # use of global(make local variable global, change global variables)
my_var_1 = 7
def show_vars():
    global my_var_2 # global variable assignment
    my_var_2 = 10
    global my_var_1 # global variable change
    print(my_var_1, my_var_2)
    my_var_1 = 90
show_vars() # 7 10
print(my_var_1, my_var_2) # 90, 10

# built-in scope
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False

# extra info: python follows LEGB(local, Enclosing, Global, Built-in) rules to deteine the scope of a variable
# extra info: global keyword modify only trully global variables, not another functions variables
# extra info: nonlocal keyword modify only 1 step inner nested functions variables
