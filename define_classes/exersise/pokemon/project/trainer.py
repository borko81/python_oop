from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return 'This pokemon is already caught'
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.name} with health {pokemon.health}'

    def release_pokemon(self, pokemon_name):
        check = [p.name for p in self.pokemon if p.name == pokemon_name]
        if len(check) > 0:
            #print(check[0])
            self.pokemon = [p for p in self.pokemon if p.name != check[0]]
            return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        data = ''
        data += f'Pokemon Trainer {self.name}\n'
        data += f'Pokemon count {len(self.pokemon)}\n'
        for i in self.pokemon:
            data += f'- {i.pokemon_details()}\n'
        return data


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())