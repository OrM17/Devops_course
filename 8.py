names = ["Or", "Tom", "Alon", "Kobi"]
for name in names:
    print(name, end="\n")
print(list(range(5)))
print(list(range(15, 1, -2)))

for i in range(len(names)):
    print(names[i])

a = 0
while a < 5:
    print(a)
    a += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 2:
        continue
    if  number == 3:
        break
    print(number)
else:
    print("finised seccessfully")

a = 0
if a < 5 :
    print(a)
