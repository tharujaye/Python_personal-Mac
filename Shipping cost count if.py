print("\t\t\t\t\t\tWelcome to shipping center")

Pweight=0

print ("Let me calculate the shipping cost")
Pweight=float(input("\tEnter the estimeating weight of your package in (kg) here : "))

shippingCost=int(Pweight*5/100)

if Pweight>25:
    print("your shipping cost is ",shippingCost ,"$")
else:
    print("Your package is free of shipping cost!")

print ("\t\tcontinue shopping >>>")