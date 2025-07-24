
#print("fuck what they say"*500)
print("Hello, welcome to my project")
name = input("what is your name?\n->>")
menu = """>Black coffe
>Latte
>Pasta"""
if name == "Purvesh":
    evil_status = input("Are you Pakiztani\n").lower()
    if evil_status == "yes":
        print("You are not allowed here get out")
        quit ()
else:
    print ("Welcome " + name)
print (name + " ,Here you go this is our menu\n" + menu)
#print("Hello " + name + ",thank you so much for checking out my project.")
#1.give coustermer a menu
#2.ask them what they want
#3.and what they ordered will be ready in few mins and 
#4.keep the menu variable
menu = """>black coffe
>latte
>pasta"""
order = input().lower()
if order in ["black coffe", "latte", "pasta"]:
   print ("What size " + order + " would you like " + name)
else:
    print("Sorry " + name + " we dont serve " + order + " here")
    quit ()
size = input("Small , Large , Venti\n").lower()

if order == "latte":
    whipped_cream = input("Do you want whipped cream?\n").lower().strip()
    if whipped_cream == "yes":
        price_whippedcreame = 10.99
else:
    price_whippedcreame = 0
quantity = int(input("How many " + order + " would you like?\n"))
tip = 2
if size == "large":
    price = 6.99
elif size == "venti":
    price = 9.99
elif size == "small":
    price = 3.99
else:
    print("Sorry we dont have that size")
    exit ()

total = (price + price_whippedcreame) * quantity + tip

print ("Your total bill will be $", total)
print("Thank you for your order " + name + ", your " + size + " " + order + "" + order.title() + " will be ready in few mins")



