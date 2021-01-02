from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {self.pokemon[-1].pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name not in [p.name for p in self.pokemon]:
            return "Pokemon is not caught"
        check = [p for p in self.pokemon if p.name == pokemon_name]
        if len(check) > 0:
        	self.pokemon = [p for p in self.pokemon if p.name != check[0]]
        	return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = ''
        result += f'Pokemon Trainer {self.name}\n'
        result += f'Pokemon count {len(self.pokemon)}\n'
        for p in self.pokemon:
            result += f'- {p.pokemon_details()}\n'
        return result


# Data
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
