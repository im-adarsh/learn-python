print("Adarsh\Kumar")
print("Adarsh\tKumar")
print("Adarsh\nKumar")

phrase= "Adarsh Kumar"
print(phrase) #Adarsh Kumar
print(phrase+" is cool.") # Adarsh Kumar is cool
print(phrase.lower()) # adarsh kumar
print(phrase.upper()) # ADARSH KUMAR
print(phrase.isupper()) # False
print(phrase.upper().isupper()) # True
print(len(phrase)) # 12
print(phrase[0]) # A
print(phrase.index("K")) # 7
print(phrase.index("umar")) # 8
print(phrase.replace("Adarsh", "Appu"))