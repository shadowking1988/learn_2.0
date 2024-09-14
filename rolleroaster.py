print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))  # ask user for height in cm

if  height >= 120:  # if height is greater than or equal to 120 cm
    print("You can ride the roller coaster!")   # print that you can ride the roller coaster
    age = int(input("What is your age? "))  # ask user for age
    if age <=12:
        print("Please pay $5.")  # print that please pay $5
    elif age <= 18:  # if age is less than 12
        print("Please pay $7.")  # print that please pay $5
    elif age > 55:  # if age is between 45 and 55
        print("Free ride!")  # print that free ride
    else:
        print("Please pay $12.")  # print that please pay $12
else:  # if height is less than 120 cm
    print("Sorry, you have to grow taller before you can ride.")  # print that you have to grow taller before you can ride
    print("Better luck next time!")  # print that better luck next time