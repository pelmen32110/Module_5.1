class House:
    def __init__(self, name,numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
    def go_to(self,new_floor):
        if self.numbers_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
            return None
        for i in range(new_floor+1):
            print(i)
        



House_1 = House('HZ',21)
House_2 = House('GoPro',33)

House_1.go_to(13)
House_2.go_to(34)
