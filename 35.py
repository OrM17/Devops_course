
def getname():
    temp_name = input("please tell me your name:")
    with open("names.txt", "a") as f:
        f.write(f"{temp_name}\n")
    f.close()


def namelist():
    my_file = open("names.txt")
    for line in my_file.readlines():
        print(f"hello {line}", end= ' ')

for i in range(3):
    getname()
namelist()

