# code copied from luggage.py

def line():
    print("="*60)

def packer(name=None, **kwargs):
    print(kwargs)


def unpacker(first_name=None, last_name=None, appeal=None):
    if first_name and last_name:
        print("Hi {} {} {}!".format(appeal, first_name, last_name))
    else:
        print("Hi no name!")

packer(name="Kenneeth", num=42, spanish_inquisition=None)
name = {"last_name": "Serditov",
        "first_name": "Nikita"}
unpacker(**name)

course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 191, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long.".format(course, minutes))

line()

# list(enumerate("abc"))
print(list(enumerate("abc")))

line()

for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print("{}: {}".format(index+1,letter))

line()

count = 1
for letter in "abcdefghijklmnopqrstuvwxyz":
    print("{}: {}".format(count, letter))
    count += 1
