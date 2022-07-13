UserInput = input("User : ")
PasswordInput = input("Password : ")

if UserInput == "admin" and PasswordInput == "4567":
    print("********** W Shop **********")
    print("1.Water  : 20 THB")
    print("2.Milk   : 30 THB")
    print("3.Toys   : 100 THB")
    print("****************************")

    UserSelect = int(input("Please select product by Number : "))
    if UserSelect == 1:
        Product1 = int(input("Water QTY : "))
        Product1Price = 20
        if Product1 >= 1:
            Total1 = print("Total water price :",Product1*Product1Price,"THB")

    elif UserSelect == 2:
        Product2 = int(input("Milk QTY : "))
        Product2Price = 30
        if Product2 >= 1:
            Total2 = print("Total water price :",Product2*Product2Price,"THB")

    elif UserSelect == 3:
        Product3 = int(input("Toys QTY : "))
        Product3Price = 100
        if Product3 >= 1:
            Total3 = print("Total water price :",Product3*Product3Price,"THB")

    print("****************************")
    print("Thank you for shop with us.")
else:
    print("Error,Please try agian")
