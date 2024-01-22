a = 2
b = 4
c = 6
if(a+b==6):
    print("Yes")
else:
    print("no")





try:
    a = int(input("Enter First Digit :"))
    b = int(input("Enter Second Digit :"))
    c = input("What Is Answer :")
    z = a + b

    if (int(a) + int(b) == int(c)):
        print("Correct Answer")
    else:
        print("Wrong Answer")
except ValueError:
    print(c , "This is not Digit")