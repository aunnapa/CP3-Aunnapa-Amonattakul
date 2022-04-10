def vatCalculate():
    totalPrice = int(input('Total Price : '))
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatCalculate())
