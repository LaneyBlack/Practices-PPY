class Person:
    person_dict = dict()

    def __init__(self, name, surname, sex, birth_date):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.birth_date = birth_date
        Person.person_dict["Person" + str(len(Person.person_dict) + 1)] = self.__dict__

    def show_info(self):
        print(self.__dict__)
        # jest tam napisane w postaci krotki, listy lub slownika wiec wybralem slownik

    @staticmethod
    def show_persons():
        return Person.person_dict


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


pers = Person("Ivan", "Afanasenka", "Man", "07.05.2003")
Person("Anton", "Reut", "Man", "27.02.2004")
pers.show_info()
print(Person.show_persons())
gamer = Gamer("Anton", "Reut", "Man", "27.02.2004", "Laney_Black", "Human", "areut74@gmail.com")
gamer.show_info()
print(Gamer.show_gamers())
print(Person.show_persons())
