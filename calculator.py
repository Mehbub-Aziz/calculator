from math import *
def add(x,y):
 print("\nThe Sum of no.s is:",x+y)
def sub(x,y):
 print("\nThe Subtraction of no.s is:",x-y)
def mul(x,y):
 print("\nThe Multiplaction of no.s is:",x*y)
def power(x,y):
 print("\nThe Exponent of no.s is:",int(pow(x,y)))
def div(x,y):
 print("\nThe Divison of no.s is:",x/y)
def root(n):
 print("\nThe Square root of no. is:",int(sqrt(n)))
def mod(x,y):
 print("\nThe Modulus of no.s is:",x%y)
def trigno():
 while True:
    print("\n\n1. Sine\n2. Cosine\n3. Tangent\n4. Back")
    ch=int(input("\nEnter your choice: "))
    if ch==1:
        n=float(input("\nEnter the angle in radians: "))
        print("\nSin: ",sin(n))
    elif ch==2:
        n=float(input("\nEnter the angle in radians: "))
        print("\nCos: ",cos(n))
    elif ch==3:
        n=float(input("\nEnter the angle in radians: "))
        print("\nTan: ",tan(n))
    elif ch==4:
        break
    else:
        print("\nEnter Correct choice !")
def convo():
 while True:
    print("\n\n1. Degrees to Radians\n2. Radians to Degrees\n3. Back")
    ch=int(input("\nEnter your choice: "))
    if ch==1:
        n=int(input("\nEnter the angle in degrees: "))
        print("\nAngle in Radians is: ",radians(n))
    elif ch==2:
        n=float(input("\nEnter the angle in radians: "))
        print("\nAngle in Degrees is: ",degrees(n))
    elif ch==3:
        break
    else:
        print("\nEnter Correct choice !")
def menu():
 while True:
    print("\n1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n5. Modulus\n6. Square root\n7. Exponent Power\n8. Trigonometric Functions\n9. Angle Conversion\n10. Exit")
    choice=int(input("\nEnter your Choice: "))
    if choice==1:
        x,y=int(input("\nEnter 1st No. ")),int(input("\nEnter 2nd No. "))
        add(x,y)
    elif choice==2:
        x,y=int(input("\nEnter 1st No. ")),int(input("\nEnter 2nd No. "))
        sub(x,y)
    elif choice==3:
        x,y=int(input("\nEnter 1st No. ")),int(input("\nEnter 2nd No. "))
        mul(x,y)
    elif choice==4:
         x,y=float(input("\nEnter 1st No. ")),float(input("\nEnter 2nd No. "))
         div(x,y)
    elif choice==5:
        x,y=int(input("\nEnter 1st No. ")),int(input("\nEnter 2nd No. "))
        mod(x,y)
    elif choice==6:
        n=int(input("\nEnter No. "))
        root(n)
    elif choice==7:
        x,y=int(input("\nEnter Base: ")),int(input("\nPower: "))
        power(x,y)
    elif choice==8:
        trigno()
    elif choice==9:
        convo()
    elif choice==10:
        print("\nExiting...")
        break
    else:
        print("\nEnter Correct choice !")
    menu()