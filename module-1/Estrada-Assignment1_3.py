#Andrew Estrada
#12/7/25
#Assignment 1.3
#This code takes a user's number input and counts it down to 0 with a nursery rhyme

try:
    bottles = int(input("Enter number of bottles:"))
#Takes the input from the user

    if (bottles) is 0:
        print("")
#Prints nothing if the user inputs 0
    elif (bottles) is 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, 0 bottles of beer on the wall.")
#Prints proper syntax if the user inputs 1
    else:
        for i in range(bottles, -1, -1):
            print((i)," bottles of beer on the wall,",(i), "bottles of beer.")
            print("Take one down and pass it around,",(i -1),"bottles of beer on the wall.")
#Prints the nursery rhyme with the user's input and subtracts it by 1 until it reaches 0
except ValueError:
    print("Please use a positive number.")
print("Time to buy more bottles of beer")
