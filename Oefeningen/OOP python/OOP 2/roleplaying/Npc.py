
from Character import Character

class NPC(Character):

    def __init(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return f"I heard there were monsters running around last night!"


if __name__ == "__main__":
    villager = NPC("Bob", 10, 12)
    villager
    print(villager.name)
    print(villager.hp)
    print(villager.level)
    print(villager.speak())