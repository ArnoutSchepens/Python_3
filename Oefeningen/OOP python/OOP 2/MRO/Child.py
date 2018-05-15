
from Mother import Mother
from Father import Father

class Child(Mother, Father):
    
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def __repr__(self):
        return f"I have {self.eye_color} eyes, {self.hair_type} {self.hair_color} hair"


if __name__ == "__main__":
    c = Child()
    print(c)