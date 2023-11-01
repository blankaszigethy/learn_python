COMPONENTS = [
    "wines",
    "gins",
    "soft_drinks"
]

WINES = [
    "name": "kéknyelű",
    "name": "kadarka",
    "name": "kékfrankos",
    "name": "furmint",
    "name": "juhfark"
]

def print_wines():
    i = 0
    while (i < len(WINES)):
        wine = WINES[i]
        name = wine["name"]
        print(f"{wine['name']}")


GINS = [
    "name": "gordon's",
    "name": "hendrick's",
    "name": "beefeater",
    "name": "bobby's"
]

def print_gins():
    i = 0 
    while (i < o len(GINS)):
        gins = GINS[i]
        name = gins["name"]
        print (f"{gins}")


SOFT_DRINKS = [
    "name": "coca cola"
    "name": "fanta"
    "name": "sprite"
    "name": "nestea"
]

def print_soft_drinks():
    i = 0
    while (i < 0 len(SOFT_DRINKS)):
        soft_drinks = SOFT_DRINKS[i]
        name = soft_drinks["name"]
        print(f"{soft_drinks}")

def print_subcomponents(type):
    if wine(WINES):
        print(print_wines)

    if gin(GINS):
        print(print_gins)

    if soft_drink(SOFT_DRINKS):
        print(print_soft_drinks)


def print_all():
    i = 0
    while(i < len(COMPONENTS)): 

