SHOTS = [
    "Tatratea",
    "Tubi",
    "Tequila",
    "Jagermeister",
    "Abszint",
]

i = 0 

while i < len(SHOTS):
    print(SHOTS[i])
    i = i + 1

PEOPLE = [
{
    "first_name": "Dora",
    "last_name": "Pekk-Juhasz",
    "favourite": ["Tubi"],
},
{
    "first_name": "Zsolt",
    "last_name": "Tasnadi",
    "favourite": ["Tequila"],
},
{
    "first_name": "Balazs",
    "last_name": "Bellanyi",
    "favourite": ["Vodka"],
},
{
    "first_name": "Mira",
    "last_name": "Harmati",
    "favourite": ["Tatratea"],
},
{
    "first_name": "Blanka",
    "last_name": "Szigethy",
    "favourite": ["Abszint", "Tubi"],
}
]

j = 0

while j <len(PEOPLE):
    first_name = PEOPLE[j]["first_name"]
    last_name = PEOPLE[j]["last_name"]
    favourite = PEOPLE[j]["favourite"]
    print(f"{first_name} {last_name}")

    avalilable = False
    k = 0 
    while k < len(favourite):
        l = 0
        while l < len(SHOTS):
            if favourite[k] == SHOTS[l]:
                avalilable = True
            l = l + 1
        k = k + 1
    j = j + 1

    if avalilable:
        print("Favourite drink is avalilable")
    else:
        print("Favourite drink is unavalilable")                
        


    


