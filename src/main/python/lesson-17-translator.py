def translate(phrase):
    translate = ""

    for letter in phrase:
        if letter in "aeiou":
            translate+="g"
        elif letter in "AEIOU":
            translate+="G"
        else:
            translate+=letter

    return translate

print(translate(input("Enter a phrase: ")))