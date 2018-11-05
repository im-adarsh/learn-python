is_male =  True
is_tall = True

if is_male and is_tall:
    print("You are tall male")
elif is_male and not(is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("You are not male but are tall")
else:
    print("You are neither male nor tall")