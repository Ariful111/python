# conditional operators
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

# conditional statement
age = 12
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
    
# multiple condition/ nested condition
is_citizen = True
age = 25
if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
    
# note: falsy values are: None, False, 0, 0.0, ""
# note: truthy values are: True, 1, 456, 8.9, "hh"
print(bool(None)) # False
print(bool(False)) # False
print(bool(0))  # False
print(bool(0.00)) # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool(-78)) # True
print(bool(7.90)) # True
print(bool('Hello')) # True

# AND
is_citizen = True
age = 25
print(is_citizen and age) # 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
    
# OR
is_student = True
is_employed = False
age = 19
print(age or is_employed) # 19

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
    
# NOT
is_admin = False
if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy