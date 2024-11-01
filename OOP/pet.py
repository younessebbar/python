class Pet:
    allowed = ["cat", "dog", "fish", "mouse"]
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet")
        self.name = name
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Elton", "dog")