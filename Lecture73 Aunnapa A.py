systemMenu = {'ข้าวขาหมู':60, 'ข้าวคากิ':65, 'ข้าวไข่เจียว':40, 'ข้าวมันไก่':50}
menuList = []
def showbill():
    print('----My Food----')
    for x in range(len(menuList)):
        print(menuList[x][0],menuList[x][1])

while True:
    menuName = input('Please Enter Menu: ')
    if menuName.lower() == 'exit':
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showbill()
totalPrice = 0
for y in range(len(menuList)):
    totalPrice += int(menuList[y][1])
print('Total:',totalPrice,'THB')



