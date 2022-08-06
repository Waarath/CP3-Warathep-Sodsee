def Vatcalculate():
    TypePrice = int(input("Type Price : "))
    result = TypePrice+(TypePrice*7/100)
    return result

print(Vatcalculate())