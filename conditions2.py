MALE = 1
FEMALE = 2


current_animal = {
    "num_of_legs": 4,
    "gender": 1,
    "name": "Muffin",
}

name = current_animal["name"]

print(name)

if current_animal["gender"] == MALE and current_animal["num_of_legs"] == 4:
    print(f"{current_animal['name']} is a 4 legs male animal")
elif current_animal["gender"] == FEMALE and current_animal["num_of_legs"] == 4:
    print(f"{current_animal['name']} is a 4 legs female animal")
elif current_animal["gender"]== MALE and current_animal["num_of_legs"] == 2:
    print(f"{current_animal['name']} is a 2 legs male animal")
elif current_animal["gender"] == FEMALE and current_animal["num_of_legs"] == 2:
    print(f"{current_animal['name']} is a 2 legs female animal")
else:
    print(f"{current_animal['name']} is an unkwnown animal")





