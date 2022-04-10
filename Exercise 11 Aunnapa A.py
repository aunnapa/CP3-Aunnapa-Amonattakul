numberInput = int(input('Number :'))
for x in range(numberInput):
    print(' '*(numberInput-x) + '*'+ ('*'*(x*2)))
