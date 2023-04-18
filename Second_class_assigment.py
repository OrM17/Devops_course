# A:
def check_whois_bigger():
    x = input("Please pick a number:")
    y = input('Please pick the second number number:')
    if x > y:
        print("BIG")
    elif x == y:
        print("Variables are equals")
    else:
        print("small")


check_whois_bigger()

# B:
for i in range(5):
    print("iteration number", i + 1)

# C:
seasons = ["1", "2", "3", "4"]


def check_the_season():
    for x in range(len(seasons)):
        if x == 0:
            print("- 1 = summer")
        elif x == 1:
            print("- 2 = winter")
        elif x == 2:
            print("- 3 = fall")
        elif x == 3:
            print("- 4 = spring")


check_the_season()

# D: it will run 10 time, it will print the number 10.

count = 1
while count < 11:
    print(count, )
    count = count + 1

# E:
age = 28
last_name_first_letter = 'M'
shekels_to_dollar_rate = 3.6
flew_abroad = True
apartment_number = 19

print(age)
print(last_name_first_letter)
print(shekels_to_dollar_rate)
print(flew_abroad)
print(apartment_number)
print(shekels_to_dollar_rate + age)


# F:
def user_number():
    phone_numbner = input("what is your number:")
    print(phone_numbner)


user_number()


# G:
def printhello():
    print("hello")


printhello()


def calculate():
    x = 5 + 3.2
    print(x)


calculate()


# H:

def whatisyourname():
    name = input("please tell me what is your name:")
    print(name)


whatisyourname()


def culnum():
    x = input("Please pick a number:")
    y = input('Please pick the second number number:')
    res = int(x) / 2
    res2 = int(y) / 2

    print(res, res2)


culnum()


# I:

def culnum(x,y):

    return x + y

print(culnum())

def stingappend():
    x = input("Please write a string:")
    y = input('Please additional  string:')
    print(x, " ", y)


stingappend()
