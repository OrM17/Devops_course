result = 0
try:
    a = int(input("enter a number please "))
    b = int(input("enter a number please "))
    result = a / b
except BaseException as e:
    print("someting went worng")
    print(e.args)
print(result)
print("Or")
