from person import Person
import random

PEPOPLE = [
    Person(first_name="Dora", last_name="Pekk-Juhasz", sex="female"),
    Person(first_name="Zsolt", last_name="Tasnadi", sex="male"),
    Person(first_name="Balazs", last_name="Bellanyi", sex="male"),
    Person(first_name="Blanka", last_name="Szigethy", sex="female"),
]
def drawed_example():
    tasi = PEPOPLE[1]
    manci = PEPOPLE[0]
    manci.set_drawed(tasi)
    print(manci.drawed.get_full_name())

drawed_example()


def main():
    random.shuffle(PEPOPLE)
    i = 0
    while i < len(PEPOPLE):
        person = PEPOPLE[i]
        print(person.get_full_name())
        i = i + 1

main()
