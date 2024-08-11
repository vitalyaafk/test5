def Sum(a,b,fff):
    if fff == 1:
        return str(a + b)
    elif fff == 2:
        return str(a - b)
    elif fff == 3:
        return str(a * b)
    elif fff == 4:
        if b == 0:
            print("Nein!!!!!!")
        else:
            return str(a / b)
    elif fff == 3:
        return str(a * b)
    else:
        return "Ogurec"
#a = b = fff = 0
while True:
    num = int(input("???: 1 - +, 2 - -, 3 - *, 4 - /, 5 - exit"))
    if Sum == 5:
        break
    a = int(input("1 number"))
    b = int(input("2 number"))
    print("Answer:", Sum(a,b,num))