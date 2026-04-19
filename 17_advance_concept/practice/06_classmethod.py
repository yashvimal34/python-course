class Animal:
    species = "Mammel" # This is class attribute.

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species
    
    @classmethod
    def get_species(cls):
        return cls.species
    
print(Animal.get_species())
Animal.set_species("Reptile")
print(Animal.get_species())