COCKTAILS = [
    {
        "name": "Negroni",
        "components": ["gin", "campari", "vermut"],
        "contains_alcohol": True,
    },
    {
        "name": "Daiquiri",
        "components": ["rum", "sugar", "lemon"],
        "contains_alcohol": True,
    },
    {
        "name": "Margarita",
        "components": ["agave", "lemon", "tequila"],
        "contains_alcohol": True,
    },
    {
        "name": "Mojito",
        "components": ["rum", "mint", "lemon"],
        "contains_alcohol": True,
    },
        {
        "name": "Virgin Mojito",
        "components": ["mint", "lemon"],
        "contains_alcohol": False,
    },
    {
        "name": "Bloody Mary",
        "components": ["vodka", "tomato juice", "pepper"],
        "contains_alcohol": True,
    }
]

STOREROOM = [
    "gin",
    "campari",
    "vermut",
    "rum",
    "pepper"
]

def header():
    return "Python Cocktail Maker"

def is_available(component):
    j = 0
    while(j < len(STOREROOM)):
        if STOREROOM[j] == component:
             return True
        j += 1
    return False

def checker(coctail):
    i = 0
    while(i <len(coctail["components"])):
        component = coctail["components"][i]
        if not is_available(component):
            return False
        i += 1
    return True

def print_coctails():
    i = 0
    while (i < len(COCKTAILS)):
        coctail = COCKTAILS[i]

        print(f"Name: {coctail['name']}")
        print("Components:")

        j = 0
        while(j < len(coctail["components"])):
            print(f"- {coctail['components'][j]}")
            j += 1

        if coctail["contains_alcohol"]:
            print("Alcoholic: Yes")
        else:
            print("Alcoholic: No")

        if checker(coctail):
            print("Can we do it? Yes")
        else:
            print("Can we do it? No")

        print("---------------------------")
        i = i + 1

def main():
    header_text = header()
    print(header_text)
    print_coctails()

main()