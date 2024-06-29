def create_player(name, xp, team):
    return {
        "name": name,
        "XP": xp,
        "team": team
    }


def introduce_player(player):
    name = player["name"]
    team = player["name"]
    print(f"Hello! my name is {name} and I play for {team}")


nico = create_player("Nico", 1500, "Team X")
lynn = create_player("Lynn", 1500, "Team Blue")

teams = {
    "Team X": [nico],
    "Team Blue": [lynn]
}
