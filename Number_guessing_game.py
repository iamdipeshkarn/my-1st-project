import random
import math  

#taking inputs
lower = int(input("enter lower value:"))  
#taking inputs
upper = int(input("enter upper value:")) 

#generating ramdom number,
#the lower and upper
x = random.randint(lower,upper)    
print("\n\tYou've only", round(math.log(upper - lower + 1, 2)),
      "chances to guess the integer!\n")

#lnitializating the number of guesses
count = 0 

#for calculation of minimum number of 
#guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    #taking number as a guess
    guess = int(input("guess a number:")) 
    if x == guess: #condition testing
        print ("congratulations you did it in", count, "try") #
        #once guessed loop will break
        break 
    elif x > guess:
        print("you guessed to small!")
    elif x < guess:
        print("you guessed too high!")

#if guessing is more than required guesses
#shows this output        
                
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck Next time!")