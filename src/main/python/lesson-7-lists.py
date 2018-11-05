friends = ["Adam", "Tom", "Dick", "Harry"];

print(friends)
print(friends[0])
print(friends[0:3]) # ['Adam', 'Tom', 'Dick']
print(friends[1:]) # ['Tom', 'Dick', 'Harry']
print(friends[1:3]) # ['Tom', 'Dick']

friends[1] = "Mike"
print(friends)

# list function

friends.extend(["Lucky"])
print(friends) # ['Adam', 'Mike', 'Dick', 'Harry', 'Lucky']

friends.append("Tommy")
print(friends) # ['Adam', 'Mike', 'Dick', 'Harry', 'Lucky', 'Tommy']

friends.insert(1, "Kelly")
print(friends) # ['Adam', 'Kelly', 'Mike', 'Dick', 'Harry', 'Lucky', 'Tommy']

friends.remove("Kelly")
print(friends) # ['Adam', 'Mike', 'Dick', 'Harry', 'Lucky', 'Tommy']

friends.pop()
print(friends) # ['Adam', 'Mike', 'Dick', 'Harry', 'Lucky']

print(friends.index("Lucky")) # 4


friends.append("Tommy")
friends.append("Tommy")
print(friends.count("Tommy")) # 2

friends.sort()
print(friends) # ['Adam', 'Dick', 'Harry', 'Lucky', 'Mike', 'Tommy', 'Tommy']

friendsCopy = friends.copy();
print(friendsCopy) # ['Adam', 'Dick', 'Harry', 'Lucky', 'Mike', 'Tommy', 'Tommy']

