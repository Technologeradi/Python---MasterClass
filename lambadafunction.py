while True:
    print("Enter the First number :")
    a = int(input())
    print("Enter the Second number :")
    b = int(input())
    print("1.Addition")
    print("2.Substraction")
    print("3.Multipication")
    print("4.Division")
    print("enter your Choise :")
    ch = int(input())

    if ch == 1:
        x = lambda a,b: a+b
        print(x(a,b))
    elif ch == 2:
        x = lambda a,b: a-b
        print(x(a,b))
    elif ch == 3:
        x = lambda a,b: a*b
        print(x(a,b))
    elif ch == 4:
        x = lambda a,b: a/b
        print(x(a,b))
    else:
        print("Invalid Input")