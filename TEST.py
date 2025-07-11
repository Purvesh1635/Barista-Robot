
#adding hastag before something is just like a not for me or else who is reading code cause terminal wont read it
#print("""i am iron man.  
#no iam tony stark.


















#no i am poppy""")
#print("I am Iron Man " + "No I am Tony Stark " + "No I am Poppy")
#print("I am Iron Man \n" + "No I am Tony Stark \n" + "No I am Poppy")
#print("fuck what they say"*500)
print("Hello, welcome to my project")
name = input("what is your name?\n->>")
print ("Hello " + name + ",thank you so much for checking out my project.")
#1.give coustermer a menu
#2.ask them what they want
#3.and what they ordered will be ready in few mins and 
#4.keep the menu variable
menu = """>BLACK COFFE
>LATTE
>PASTA"""

print (name + " ,Here you go this is our menu\n" + menu)
order = input()
price = 5
quantity = int(input("How many " + order + " would you like?\n"))

print ("What size Latte would you like " + name)
size = input("Small , Large , Venti\n")

tip = 2
total = (price * quantity + tip)
print ("Your total bill will be $", total)
print("Thank you for your order " + name + ", your " + size + " " + order + " will be ready in few mins")



