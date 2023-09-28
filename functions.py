def get_pan():
    print("get a pan")

def get_meal(meal):
    print(f"get {meal}")

def bake_meal(meal):
    print(f"bake {meal}")

def clean_pan():
    print("clean the pan")

def bake(meal):
    get_pan()
    get_meal(meal)
    bake_meal(meal)
    clean_pan()

bake("eggplant")
bake("tomato")