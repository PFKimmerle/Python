from animal import Lion, Tiger, Bear

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()

# Initialize the zoo
zoo1 = Zoo("John's Zoo")

# Adding animals
zoo1.add_animal(Lion("Nala", 3))
zoo1.add_animal(Lion("Simba", 4))
zoo1.add_animal(Tiger("Rajah", 5))
zoo1.add_animal(Tiger("Shere Khan", 7))
zoo1.add_animal(Bear("Baloo", 10))

# Display all info
zoo1.print_all_info()

# Feeding all animals
for animal in zoo1.animals:
    animal.feed()

# Display all info after feeding
zoo1.print_all_info()
