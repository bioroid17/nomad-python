# print("nico".upper())
# print("nico".endswith("a"))

# numbers = [5, 3, 1, 5, 7, 3, "True", True, 12]
# numbers.append(["🍕", "🍔"])
# print(numbers[-1])

# numbers = (1, 2, 3, 4, 5)

player = {
    "name": "nico",
    "age": 12,
    "alive": True,
    "fav_food": ("🍕", "🍔"),
    "friend": {
        "name": "lynn",
        "fav_food": ["🍎"]
    }
}

player["fav_food"] = "🍎"
player.pop("alive")
player["friend"]["fav_food"].append("🍌")
print(player)
