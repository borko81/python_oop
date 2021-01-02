class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        data = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for s, m in self.skills.items():
            data += f"==={s} - {m}\n"
        return data


player = Player("George", 50, 100)
player2 = Player("Borko", 50, 100)
print(player.player_info())
print(player.add_skill('Test', 50))
print(player2.player_info())
