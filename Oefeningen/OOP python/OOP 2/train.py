
class Train:
    
    def __init__(self, cars):
        self.cars = cars

    def __repr__(self):
        return f"{self.cars} car train"
    
    def __len__(self):
        return self.cars

a_train = Train(4)
print(a_train)
print(len(a_train))