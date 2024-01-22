def upper():
    a = input("What is your Name :")
    print(a,"Convert To =",a.upper())

def lower():
    a = input("What is your Name :")
    print(a,"Convert To =",a.lower())


z = int(input("UPPER = PRESS 1 \n lower = press 2 :"))
if(z==1):
    upper()
elif(z==2):
    lower()
else:
    print("Enter Valid Number")
