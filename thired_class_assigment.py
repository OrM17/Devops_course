# 1 + 2:
try:
    a = int(input("enter a number please "))
    b = int(input("enter a number please "))
    result = a / b
except BaseException as e:
    print("someting went worng")
    print(e.args)


# 3: yes, at the end it will print finally

# 4: all types of except can be caught in this handler

# 5: it's showing only part of the issue, it will not show all the problen, so it better to add by yourself an error
# note.

# 6:
# IOError - it's an input or output error, if I will try to write to non exist file it will cause an IOerror
#  ZeroDivisionError - will rise if I will try divide a number in zero

# 7:
def create_file():
    file = open("C:/tmp/words.txt", 'w')
    file.close()


# 8:
def write_in_file():
    file = open("C:/tmp/words.txt", 'w')
    file.write("Or")
    file.close()


# 9:
def readfile():
    file = open("C:/tmp/words.txt", 'r')
    for line in file.readline():
        print(f"hello {line}", end=' ')


# 10"
def hebrewfile():
    with open('C:/tmp/hebrew.txt', mode='w', encoding='utf-8') as file:
        file.write('שלום עולם.')

    with open('C:/tmp/hebrew.txt', mode='r', encoding='utf-8') as file:
        lines = file.read()
    print(lines)

