
#print("fuck what they say"*500)
print("Hello, welcome to my Cafě")
name = input("what is your name?\n->>").lower()
menu = """>Black coffe
>Latte
>Pasta"""
if name == "Stan".lower():
    menu = """>Black coffe
>Latte
>Pasta
>Bag of Coke"""""    
else:
   print ("Welcome " + name.capitalize())

if name.lower() == "purvesh" or name.lower() == "krishna":
    evil_status = input("Are you Pakiztani\n").lower()
    good_deeds = int(input("How many good deeds have you done today\n"))
    if evil_status == "yes" and good_deeds < 4:
        print("You are not welcome here "+ name.capitalize() + " get out")
        quit ()
else:
    print ("Welcome " + name.capitalize())
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
price = 0 
price_whippedcream = 0
tip = 2
valid_orders = ["black coffe", "latte", "pasta"]
if name.lower() == "stan":
    valid_orders.append("bag of coke")
if order in ["black coffe", "latte", "pasta", "bag of coke"]:
   print ("What size " + order + " would you like " + name)
else:
    print("Sorry " + name + " we dont serve " + order + " here")
    quit ()
#size = input("Venti, Tall, Grande \n").lower()
if order == "pasta":
    size = input("Small, Large\n").lower().strip()
else:
    size = input("Venti, Tall, Grande \n").lower().strip()
if order == "latte":
    whipped_cream = input("Do you want whipped cream?\n").strip().lower()
    if whipped_cream == "yes":
        price_whippedcream = 10.99
    else:
        price_whippedcream = 0
quantity = int(input("How many " + order + " would you like?\n"))
tip = 2
if order == "bag of coke":
    price = 50
elif size == "small":
    price = 7
elif size == "large":
    price = 10
elif size == "tall":
    price = 6.99
elif size == "grande":
    price = 9.99
elif size == "venti":
    price = 3.99
else:
    print("Sorry we dont have that size")
    exit ()

total = (price + price_whippedcream) * quantity + tip

print ("Your total bill will be $", total)
print("Thank you for your order " + name + ", your " + size + " " + order.title() + " will be ready in few mins")



