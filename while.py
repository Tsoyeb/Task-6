# A program to calculate the average of the numbers a user enters 

# Variables to hold the values. 
sum = 0 
number = 0 
counter =0

# If the user does not enter -1 the program will keep running 
while True: 
    number= int(input("Pick a number, any number, as many numbers as you like and I will work out the average but '-1' will exit the command: "))

    if number == -1:
        break
    sum += number 
    counter+= 1 

# Calculates the average of total numbers
average = (sum)/(counter)

print(f'Your total average is {average:.2f}')

