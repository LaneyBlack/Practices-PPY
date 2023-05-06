from c8.zad import Person


class Gamer(Person):
    gamer_dict = dict()

    def __init__(self, name, surname, sex, birth_date, nickname, type, email):
        super().__init__(name, surname, sex, birth_date)
        self.nickname = nickname
        if type == "NPC" or type == "Human":
            self.type = type
        else:
            print("Wrong gamer type")
            self.type = "NPC"
        self.email = email
        Gamer.gamer_dict["Gamer" + str(len(Gamer.gamer_dict) + 1)] = self.__dict__

    def show_info(self):
        print(self.__dict__)

    @staticmethod
    def show_gamers():
        return Gamer.gamer_dict
