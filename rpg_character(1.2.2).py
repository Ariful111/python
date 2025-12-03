full_dot = '●' 
empty_dot = '○' 
def create_character(char_name, s1, s2, s3): 
    if not isinstance(char_name, str): 
        return "The character name should be a string" 
    elif len(char_name) > 10: 
        return "The character name is too long" 
    elif " " in char_name: 
        return "The character name should not contain spaces" 
    elif any(not isinstance(x, int) for x in (s1, s2, s3)): 
        return "All stats should be integers" 
    elif any(x < 1 for x in (s1, s2, s3)): 
        return "All stats should be no less than 1" 
    elif any(x > 4 for x in (s1, s2, s3)): 
        return "All stats should be no more than 4" 
    elif s1 + s2 + s3 != 7: 
        return "The character should start with 7 points" 
    else: 
        """ here you can use direct a list as alternative of for loop ------
        lines = [char_name, "STR " + full_dot * s1 + empty_dot * (10 - s1), "INT " + full_dot * s2 + empty_dot * (10 - s2), "CHA " + full_dot * s3 + empty_dot * (10 - s3)] """
        lines = [char_name]
        for stat_name, value in zip(["STR", "INT", "CHA"], [s1, s2, s3]):
            bar = full_dot * value + empty_dot * (10 - value)
            lines.append(f"{stat_name} {bar}")
        return "\n".join(lines) 
print(create_character("ren", 4, 2, 1))