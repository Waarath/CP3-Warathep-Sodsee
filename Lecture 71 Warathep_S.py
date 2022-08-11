MenuList = []
PriceList = []

def Showbill():
    TotalPrice = 0
    print('Food'.center(20,'-'))
    for number in range(len(MenuList)):
        print(MenuList[number],PriceList[number])
        TotalPrice += int(PriceList[number])
    print("Total Price :", TotalPrice,'THB')


while True:
    ProductName = input('Type product : ')
    if (ProductName.lower() == 'exit'):
        break
    else:
        ProductPrice = input('Type price : ')
        MenuList.append(ProductName)
        PriceList.append(ProductPrice)

Showbill()
