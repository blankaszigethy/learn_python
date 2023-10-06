people = [
{
  "first_name": "Blanka",
  "last_name": "Szigethy",
  "age": 20,
  "programming_skill": True,
},
{
  "first_name": "Dóra",
  "last_name": "Pekk-Juhász",
  "age": 28,
  "programming_skill": False,
},
{
  "first_name": "Zsolt",
  "last_name": "Tasnádi",
  "age": 36,
  "programming_skill": True,
  }
]

i = 0
while(i < len(people)):
  person = people[i]
  first_name = people[i]["first_name"]
  last_name = person["last_name"]
  age = person["age"]
  print(f"{first_name} {last_name}'s age is {age}")
  i = i + 1 # or i++

