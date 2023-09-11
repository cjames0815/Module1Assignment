# The lyrics for the Twelve Days of Christmas in a list
lyrics = [
    "A partridge in a pear tree",
    "Two turtle doves, and",
    "Three French hens",
    "Four calling birds",
    "Five golden rings",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming"
]

#Using a try and execpt as validation
# Prompt the user for input
try:
    number = int(input("Enter a number between 1 and 12: "))
    
# Check if the input is within the valid range 
    if 1 <= number <= 12:
        print(f"On the {number}th day of Christmas, my true love gave to me:")
        
#For loop will output the rest of the lyrics depending on what number you choose        
        for i in range(number, 0, -1):
            print(lyrics[i - 1])
#If any other number outside the range is inputted it will error to a Value error  
    else:
        print("Invalid number. Please enter a number between 1 and 12.")
#Outputs a error with invalid integers
except ValueError:
    print("Invalid input. Please enter a valid number.")