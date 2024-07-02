x=2
y=2
def Add(x,y):
    return x+y
def Substract(x,y):
    return x-y
def Multiply(x,y):
    return x*y
def Divide(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
while True:
    choice=input("Enter choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        x=float(input("Enter first num:"))
        y=float(input("Enter second num:"))
        if choice =='1':
            print(x,"+",y,"=",x+y)
        if choice == '2':
            print(x, "-", y, "=", x - y)
        if choice == '3':
            print(x, "*", y, "=", x * y)
        if choice == '4':
            print(x, "/", y, "=", x / y)


