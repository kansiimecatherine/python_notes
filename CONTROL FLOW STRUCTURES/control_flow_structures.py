#control flow structures
# These determine the order in which programs are executed basing on conditions or loops.

#Types
#1conditional statements
#These execute programs based on a particlar program.

#Examples
# -if #The if block executes a particular condition and this is always true. 
# -elif 
# -else 

#create a program that asks a user for the food type bought from the market.
# the program should print you bought chicken if the user enters chicken,
# the program should print liver if you bought liver else the program should print 
# fish. 

#approach one
def food_types():
    food_type =input("Enter the food type bought:").lower()
    if food_type == 'chicken':
        print("You bought chicken from the market.")
    elif food_type == 'liver':
        print("You bought liver from the market.")
    elif food_type == 'fish':
        print("You bought fish from the market.")
    else:
        print("Choose from chicken,liver or fish")
food_types()

#approach two:
food_type = input("Enter the food type bought:").lower()
if food_type != 'chicken' or food_type != 'liver' or food_type != 'fish':
    print(f"choose from chicken,liver or fish.")
elif food_type == 'chicken':
    print(f"You bought chicken from the market.")
elif food_type == 'liver':
    print(f"You bought liver from the market.")
else:
    print(f"You bought fish from the market.")

#Using logical operators ("or" "and" )


       
       

    


