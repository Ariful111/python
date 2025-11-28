# uppercase, lowercase, capitalize string
my_str_1 = "Hello World"
uppercase_my_str_1 = my_str_1.upper()
lowercase_my_str_1 = my_str_1.lower()
capitalize_my_str_1 = uppercase_my_str_1.capitalize()
print(uppercase_my_str_1) # HELLO WORLD
print(lowercase_my_str_1) # hello world
print(capitalize_my_str_1) # Hello World
print(my_str_1.isupper()) # False
print(my_str_1.islower()) # False
print(my_str_1.istitle()) # True (capiralize means title, numeric data is not upper/ lower/ title)

# trim character from left/right/both sides
my_str_2 = "  hello world  "
my_str_3 = "---hello world---"
trimmed_my_str_2 = my_str_2.strip() # same with strip(" "), default both sides
trimmed_my_str_3 = my_str_3.lstrip("-")
print(trimmed_my_str_2) # hello world 
print(trimmed_my_str_3) # hello world---


# replacd method
my_str_4 = my_str_1.replace("Hello", "Hi")
print(my_str_4)


# seperate/split words in list( normally use in taking input: a, b, c = input().split() ) 
my_str_5 = "apple,banana,orange"
split_words_1 = my_str_1.split() # same with split(" "), default split by space
split_words_2 = my_str_5.split(",") # if character not found list item will be one
print(split_words_1) # Hello World
print(split_words_2) # apple-banana-orange


# join elements of a list
my_list_1 = ["apple", "orange"]
my_list_2 = [1, 6, 9]
my_str_6 = "-".join(my_list_1) # join by inside of quotation
my_str_7 = "".join(map(str, my_list_2)) # join only string and output is also string
print(my_str_6) # apple-orange
print(my_str_7) # 169


# find first and last portion 
starts_with = my_str_1.startswith("Hello")
ends_with = my_str_1.endswith("lds")
print(starts_with, ends_with) # True False


# find word(first character)/character index
word_index = my_str_1.find("World")
character_index = my_str_1.find("o")
unknown_index = my_str_1.find("Z")
print(word_index, character_index, unknown_index) # 6 4 -1


# count specific word/ character/ portion
count_word = my_str_1.count("Hello")
count_char = my_str_1.count("l")
print(count_word, count_char) # for words count: count space by count(" ") then add 1

