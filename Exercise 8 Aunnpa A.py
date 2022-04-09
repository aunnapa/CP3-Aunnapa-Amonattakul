usernameInput = input('username : ')
passwordInput = input('password : ')
if usernameInput == 'aunnapa' and passwordInput == '123456':
    print('Log-in success! ')
    print('รายการสินค้า')
    print('-------------------------')
    print('1.กล้วย ราคา 10 บาท')
    print('2.ขนมปัง ราคา 5 บาท')
    print('3.น้ำเปล่า ราคา 7 บาท')
    print('--------เลือกสินค้า----------')
    userSelected = int(input())
    if userSelected == 1:
        qty = int(input('กรุณาระบุจำนวนที่ต้องการ : '))
        print('ราคารวม :', 10*qty)
    elif userSelected == 2:
        qty = int(input('กรุณาระบุจำนวนที่ต้องการ : '))
        print('ราคารวม :', 5*qty)
    elif userSelected == 3:
        qty = int(input('กรุณาระบุจำนวนที่ต้องการ : '))
        print('ราคารวม :', 7*qty)
    else:
        print('ไม่มีสินค้าดังกล่าว')