class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.players = []

    def show_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.name)
        self.players.append(new_player)

    def delete_player(self, name):
        for player in self.players:
            if name == player.name:
                self.players.remove(player)
                print(
                    f"Player with the name of {name} is removed from {self.name}")
                return
        else:
            print(f"Player with the name of {name} doesn't exist")
            return

    def show_total_xp(self):
        total = 0
        for player in self.players:
            total += player.xp
        print(f"The sum of our team's xp is {total}")


team_x = Team("Team X")
team_x.add_player("Nico")
team_blue = Team("Team Blue")

team_blue.add_player("Lynn")
team_blue.add_player("Lee")

team_blue.show_players()

team_blue.delete_player("l")

team_blue.show_total_xp()
