#!/usr/bin/env python3


class Character:

    def __init__(self, favouriteWeapon):
        self.__fv = favouriteWeapon
        self.age = 0

    def favouriteWeapon(self):
        return self.__fv


class Elf(Character):

    def __init__(self):
        super().__init__("bow")

    def accept(self, visitor):
        visitor.visitElf(self)


class Orc(Character):

    def __init__(self):
        super().__init__("axe")

    def accept(self, visitor):
        visitor.visitOrc(self)


class Human(Character):

    def __init__(self):
        super().__init__("sword")

    def accept(self, visitor):
        visitor.visitHuman(self)


class Lord(Character):

    def __init__(self, *vassals):
        super().__init__("money")
        self.__vassals = vassals

    def vassals(self):
        return self.__vassals

    def accept(self, visitor):
        visitor.visitLord(self)

# Want to add message, but can't touch classes

class CharacterVisitor:
    pass


class MessagingVisitor(CharacterVisitor):

    def __init__(self):
        self.humanNm = 0

    def visitElf(self, elf):
        print("Elf: My {0} is ready!".format(elf.favouriteWeapon()))

    def visitHuman(self, human):
        if self.humanNm == 0:
            print("Human: I'm the only human!")
        else:
            print("Human: I will never walk alone")
        self.humanNm += 1

    def visitOrc(self, orc):
        print("Orc: Groughhh")

    def visitLord(self, lord):
        # treat lord as a separate person
        print("Lord: I'm lord. Get off my way")


class HiringCostCounter(CharacterVisitor):

    def __init__(self):
        self.__totalCost = 0

    def visitElf(self, elf):
        self.__totalCost += 15

    def visitHuman(self, human):
        self.__totalCost += 10

    def visitOrc(self, orc):
        self.__totalCost += 30

    def visitLord(self, lord):
        # Lord is not a fighter, we can entice his army.
        for v in lord.vassals():
            v.accept(self)

    def totalCost(self):
        return self.__totalCost

if __name__ == "__main__":
    msgVisitor = MessagingVisitor()
    hiringCounter = HiringCostCounter()

    for ch in [Elf(), Human(), Lord(Elf(), Elf(), Orc()), Orc(), Human()]:
        ch.accept(msgVisitor)
        ch.accept(hiringCounter)

    print("Total cost:", hiringCounter.totalCost())

# NB: visitor is not about traversal.
#     It's about adding actions to every item in hierachy.
#     Visitor can itself define traversal order or ignore it (lord example)
