def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multipication(a,b):
    return a*b

def division(a,b):
    return a/b



while True:
    print("--------------------------------")
    print("Enter the numbers:-")
    print("Enter the First number:-")
    a = int(input())
    print("Enter the Second number1-")
    b = int(input())
    print("--------------------------------")
    print("Basic Calculator")
    print("1. Addition")
    print("2. Substrat")
    print("3. Multipication")
    print("4. Division")
    print("5. Stop")
    ch = input()
    print("--------------------------------")
    if ch == '1':
        print(str(a) +" + "+ str(b) + " = ", addition(a,b))
    elif ch == '2':
        print(str(a) +" - "+ str(b) + " = ", substraction(a,b))
    elif ch == '3':
        print(str(a) +" * "+ str(b) + " = ", multipication(a,b))
    elif ch == '4':
        print(str(a) +" / "+ str(b) + " = ", division(a,b))
    elif ch == '5':
        break
    else:
        print("Invalid Input")
