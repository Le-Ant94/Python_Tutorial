lucky_numbers = [1,2,3,4,5]
friends = ["Kevin", "Angela", "Jim", "Jim"]

print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(2, "Oscar")
print(friends)
friends.remove("Jim")
print(friends)
print(friends.count("Jim"))
print(lucky_numbers.reverse())
