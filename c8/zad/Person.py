import datetime
class Person:
    person_dict = dict()

    def __init__(self, name, surname, sex, birth_date):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.birth_date = birth_date
        Person.person_dict["Person" + str(len(Person.person_dict) + 1)] = self.__dict__

    @staticmethod
    def show_persons():
        return Person.person_dict
    def show_info(self):
        print(self.__dict__)
        # jest tam napisane w postaci krotki, listy lub slownika wiec wybralem slownik

    def calc_age(self):
        today = datetime.date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))



pers = Person("Ivan", "Afanasenka", "Man", datetime.date(year=2003, month=5,day=7))
print(pers.name ,"'s age is",pers.calc_age())

