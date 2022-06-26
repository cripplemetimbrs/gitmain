print("Hello, welcome to Networkchuck coffee!!!!!!!")
name = ("may i have your name please?\n")
    #a function to take input from the customer, and convert the input into a string. one input was given it can be used further with another step. making it print(input( instead will print the input.


# User Creating the “Variable by Question, Name” - If ben comes in then do the bounce - Printing the Variable “Name” inside a string

print("Hello, welcome to Networkchuck coffee!!!!!!!")
name = input("May i have your name please?\n")
    #a function to take input from the customer into a string. one input was given it can be used further with another step. making it print(input( instead will print the input.
if name == "ben" or name == "patricia":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds < 4:
        print("You're not welcome here evil" + name + "Get out!!")
        exit()
    else:
        print("Oh hello " + name + ", come on in!!")
else:
    print("Hey " + name + ", thanks for coming in today.\n\n\n")
        #To use this, we defined the input with only 1 variable that we ask from the user, like a name input, it took the name given as the input and used it as the next name continuously. You can name your variable whatever you want, and you can also set it to a vfunction or a string. I also have learned “IF & else” syntax that for one set of code to interact with another set of code it needs to be nested underneath it with a tab space. **We learn to greater than > we learned less than <, less than equal to < =, greater than equal to > =, 2 equals == are necessary for two different outcomes and if it is true or false. else wont run if its not true because its in line. creating variables and creating the conditions for it to work using math. can use, if not and or elif else. !# ifnot**


# Creating the “Menu Variable” - User Creating the “Variable by Question, Order”

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"
print("Hello " + name + ", What would you like from our menu today? Here is what we are serving.\n" + menu)
order = input()
    #this will await for input from the customer.. and save it as the variable “order” because we asked “what would they like from the menu?” they knew to input their order.

# Declared the Variable “Price” - User is Creating the “Variable by Question, quantity” - Creating the Variable “Total” using math, then Converting it back

if order == "Frappuccino":
    price = 8
elif order == "black coffee":
    price = 5
elif order == "espresso":
    price = 3
elif order == "cappucino":
    price = 6
elif order == "latte":
    price = 7
else:
    print("Sorry, we dont have that here.")
    price = 0
quantity = input("How many " + order + "would you like?\n")
total = price * int(quantity)
    #Now instead of it multiplying and number or an integer by a string it multiplies an integer by an integer by converting quantity which was a string now into a number
print("Thank you. Your total is: $" + str(total))
    #Here I learned how to turn a string into an integer and an integer into a string


# Creating the Print summary function with our 3 strings and 3 variables together.

print("Sounds good " + name + ", well have your  " + quantity + " " + order + " ready for you in just a moment.")