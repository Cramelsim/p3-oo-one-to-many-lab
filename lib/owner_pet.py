class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    all=[]
    
    def __init__(self, name, pet_type ,owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner or None")
        
        self.name=name
        self.pet_type=pet_type
        self.owner=owner

        Pet.all.append(self) 
#add pet on list
        if owner:
           owner.add_pet(self)

class Owner:
    def __init__(self,name):
       if not isinstance(name, str):
            raise Exception("Name must be a string")
       self.name = name
       self._pets = []  
       
    def pets(self):
        return self._pets
    
    def add_pet(self, pet):
        if not isinstance (pet,Pet):
            raise Exception ("Pet must be an instance of pet class")
        pet.owner=self
        self._pets.append(pet)

    def get_sorted_pets(self):
         return sorted(self._pets, key=lambda pet: pet.name)