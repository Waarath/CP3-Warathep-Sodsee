def login():
    usernameinput = input("User : ")
    passwordinput = input("Password : ")
    if usernameinput == "admin" and passwordinput == "1234":
        return ShowMenu()
    else:
        return "Log in Failed"

def ShowMenu():
    print("-------- W Shop --------")
    print("1) Vat calculator")
    print("2) Price calculator")
    MenuSelect()

def MenuSelect():
    UserSelected = int(input("Select Number : "))
    if UserSelected == 1:
        print("Total Price(7%) :",VatCalculator(int(input("Price : "))))
    else:
        print("Total Price(7%) : ",PriceCalculator())

def VatCalculator(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result

def PriceCalculator():
    price1 = int(input("Price 1 : "))
    price2 = int(input("Price 2 : "))
    return VatCalculator(price1+price2)

print(login())