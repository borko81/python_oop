from player import Player
#from OOP.define_classes.exersise.guild_system.project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name not in map(lambda x: x.name, self.players):
            return f"Player {player_name} is not in the guild."
        check = filter(lambda x: x.name == player_name, self.players)
        check[0]
        self.players.remove(next(check))
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        data = f"Guild: {self.name}\n"
        for p in self.players:
            data += p.player_info()
        return data



player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())