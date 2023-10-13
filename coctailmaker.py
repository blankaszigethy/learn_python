COCKTAILS = [
 {
     "name": "Negroni",
     "components":["gin", "campari", "vermut"],
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
    "name": "Bloody Mary",
    "components": ["vodka", "tomato juice", "pepper"],
    "contains_alcohol": True,
}

]

def header():
    string = "Python Cocktail Maker"
    return string

def main():
    header_text = header()
    print(header_text)


def print_coctails():
    i = 0
    while(i < len(COCKTAILS)):
        night = COCKTAILS[i]
        name = COCKTAILS[i]["name"]
        components = COCKTAILS["components"]
        contains_alcohol = COCKTAILS["contains_alcohol"]
        print(f"Name: {name} Components: {components} Alcoholic: {contains_alcohol}")
        i = i + 1


