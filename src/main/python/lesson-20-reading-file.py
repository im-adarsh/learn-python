# read file
employee_file = open("./static/employee.txt", "r")

print(employee_file.readable())
#print(employee_file.read())

print(employee_file.readlines())

print(employee_file.readline())
print(employee_file.readline())

employee_file.close()

# write file
employee_file = open("./static/employee.txt", "a")

employee_file.write("new line \n")

employee_file.close()