monthConversions = {
    "Jan" : "January",
    "Feb" : "Feburary",
    "Mar" : "March"
}

print(monthConversions["Jan"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Jan1", "Not found"))