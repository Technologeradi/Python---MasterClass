#Creating a list
List = []
print("--------------------------------------")
print("To-do List:-")
print("--------------------------------------")
for x in range(len(List)):
    print(str(x) +" "+ List[x])
print("--------------------------------------")
print("Total Items:"+str(len(List)))
#Main meun
while True:
    print("\n")
    print("What you wanna do ?")
    print("1.Add")
    print("2.Remove")
    print("3.Display")
    print("4.Stop")
    ch = int(input())
    if ch == 1:
        print("Enter todo")
        List.append(input())
    elif ch == 2:
        print("Delete #")
        List.pop(int(input()))
    elif ch == 3:
        for x in range(len(List)):
            print(str(x) + " " + List[x])
        print("--------------------------------------")
        print(len(List))
    elif ch == 4:
        break
    else:
        print("Invalid Input")


