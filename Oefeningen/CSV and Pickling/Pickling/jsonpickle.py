
import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
c = Cat("Charles", "Tabby")
frozen = jsonpickle.encode(c)
print(frozen)