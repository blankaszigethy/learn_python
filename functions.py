# bake function
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

# bake("eggplant")
# bake("tomato")

# salary function

def calculate_salary(workdays, hourly_wage, daily_workhours):
    salary = workdays * hourly_wage * daily_workhours
    return salary

def print_salary(name, salary):
    print(f"{name}'s salary in this month is {salary}HUF")

bubus_salary = calculate_salary(20, 2500, 4)
print_salary("Bubu", bubus_salary)

tasis_salary = calculate_salary(21, 10750, 8)
print_salary("Tasi", tasis_salary)

