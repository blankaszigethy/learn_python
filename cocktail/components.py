COMPONENTS = [
    "wines",
    "gins",
    "soft_drinks"
]

WINES = [
    "kéknyelű",
    "kadarka",
    "kékfrankos",
    "furmint",
    "juhfark"
]

GINS = [
    "gordon's",
    "hendrick's",
    "beefeater",
    "bobby's"
]

SOFT_DRINKS = [
    "coca cola",
    "fanta",
    "sprite",
    "nestea",
]

def print_wines():
    i = 0
    while (i < len(WINES)):
        print(WINES[i])
        i = i + 1

def print_gins():
    i = 0
    while (i < len(GINS)):
        print (GINS[i])
        i = i + 1

def print_soft_drinks():
    i = 0
    while (i < len(SOFT_DRINKS)):
        print(SOFT_DRINKS[i])
        i = i + 1

def print_subcomponents(category):
    if category == "wines":
        print_wines()

    if category == "gins":
        print_gins()

    if category == "soft_drinks":
        print_soft_drinks()


def print_all():
    i = 0
    while(i < len(COMPONENTS)):
        category = COMPONENTS[i]
        print(f"*** {category} ***")
        print_subcomponents(category)
        i = i + 1

print_all()