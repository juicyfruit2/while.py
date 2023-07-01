# a program that always asks the user to enter a number

# created variables 
count = 0 
total = 0 

# loop will activate and ask user to enter a number consistently  
while True :
    user = int(input("Enter any random number:")) 

# when -1 is enterd the loop will stop and print out the average number    
    if user == -1:
        break 
    count = count + 1 
    total = total + user 
    avg = total/count 

print(f"the average number is", avg)
    
        










    

