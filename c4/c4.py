# Lab04 dictionarys

print("Declarations")
print("1---")
s = {}
print("Set =", s)
s = dict()
print("Dict =", s)
print("2---")
s = {"Nazwisko": "Wolf", "Wiek": 25}
print(s)
s = dict([("Nazwisko", "Wolf"), ("Wiek", 25)])
print(s)
s = dict(Nazwisko="Wolf", Wiek=25)
print(s)
print("Operations")
print("1---")
print(s["Nazwisko"])
print(s.get("Wiek"))
s["Nazwisko"] = "Blue"
print(s)
print("2---")
new_els = {"Zawód": "Informatyk", "Klasa": 1}
s.update(new_els)
s.update({"Poly":"is beautiful"})
print(s)
s.pop("Zawód")
print(s)
del s["Klasa"]
print(s)
print("Methods")
print("1---")
print(s.keys())
print(s.values())
print(s.items())
