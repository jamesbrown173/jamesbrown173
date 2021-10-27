


lucky_numbers = [4, 5, 6, 7, 8, 34, 67, 88]
friends = ["marc", "kevin", "baxter", "peter","peter","peter", "petricia"]

friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("marc")
friends.extend(lucky_numbers)

print(friends)

print(friends.index("kevin"))

print(friends.count("peter"))


friends2 = friends.copy()

print(friends2)
