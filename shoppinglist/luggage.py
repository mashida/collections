def packer(name=None, **kwargs):
    print(kwargs)


def unpacker(first_name=None, last_name=None, appeal=None):
    if first_name and last_name:
        print("Hi {} {} {}!".format(appeal, first_name, last_name))
    else:
        print("Hi no name!")

packer(name="Kenneeth", num=42, spanish_inquisition=None)
name = {"last_name": "Serditov",
        "first_name": "Nikita",
        "appeal": "Sir"}
unpacker(**name)
