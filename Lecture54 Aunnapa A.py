def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        vatCalculator()
    elif userSelected == 2:
        priceCalculator()
    else:
        showMenu()
        menuSelect()

def vatCalculator():
    vat = 7
    totalPrice = int(input('Total price: '))
    result = totalPrice + (totalPrice * vat / 100)
    return print('Total Price + Vat =', result)

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return print('Total price =', price1 + price2)

login()