menuList = []
priceList = []
def showbill():
    print('----My Food----')
    for x in range(len(menuList)):
        print(menuList[x], priceList[x])

while True:
    menuName = input('Please Enter Menu: ')
    if menuName.lower() == 'exit':
        break
    menuPrice = input('Price: ')
    menuList.append(menuName)
    priceList.append(menuPrice)

showbill()
totalPrice = 0
for y in range(len(priceList)):
    totalPrice += int(priceList[y])
print('Total:',totalPrice,'THB')



