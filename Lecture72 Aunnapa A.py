menuList = []
def showbill():
    print('----My Food----')
    for x in range(len(menuList)):
        print(menuList[x])

while True:
    menuName = input('Please Enter Menu: ')
    if menuName.lower() == 'exit':
        break
    menuPrice = input('Price: ')
    menuList.append(menuName,menuPrice)

showbill()
totalPrice = 0
for y in range(len(menuList)):
    totalPrice += int(menuList[y][1])
print('Total:',totalPrice,'THB')



