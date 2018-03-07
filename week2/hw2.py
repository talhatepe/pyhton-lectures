while True:
    num1 = input("Num 1: ")
    num1 = int(num1) - 1
    num2 = input("Num 2: ")
    num2 = int(num2)
    str = input("String: ")
    str2 = str[num2:]
    str = str[:num1]
    print (str,str2)
