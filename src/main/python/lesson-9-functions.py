# indentation define the function scope

# function 1 start
def greet(name, age):
    print("Hello "+name+", you are "+ str(age))
# function 1 end

def getGreet(name, age):
    return "Hello "+name+", you are "+ str(age)

def cube(num):
    return num*num*num;


# function 1 call
greet("Adarsh", 25)
greet("Mike", 26)

print(getGreet("Adarsh", 26))

result = cube(3)
print(result)