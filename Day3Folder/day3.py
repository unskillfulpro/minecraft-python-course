# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task
print("hello from day3")

########################################################################
#  Task 1:
# myName = input("What's your name?")
# Title = input("What's your title?")
# Command = input("What is your command?")
# print(Title +" " + myName + " wants "+ Command)



########################################################################
# Task 2:
# name = "JOPHIEL"
# numpens = 100
# print(name + " bought " + str(numpens) + " pens.")



########################################################################
# Task 3:
# Num1=input("Give a number.")
# NUm2=input("Give a number.")
# print(int(Num1) + int(NUm2))


########################################################################
# Task 4:
# amount=input("How many apples are you buying? An apple costs 0.67 dollars each")
# apple_cost =67
# price = int(amount)*apple_cost
# print("The "+ amount + "apples you bought cost"+ str(price) +" cents.")




########################################################################
# Task 5:
# age1=10
# age2=input("How old are you?")
# if int(age2)>age1:
#     print("You're old enought to enter!")
# else:
#     print("I'm sorry, you're too young.")


########################################################################:
# Task 6
# real_password="your password"
# guess=input("Enter your password.")


# if guess==real_password:
#     print("Acces granted.")
# else:
#     for letter in ("XXXx"):
#     print(letter)

# if letter=="x":
#     print("System locked.")




########################################################################
# Task 7:
import random
# for count in range (10):    
#     dicevalue = random.randint(1,100)
#     print(dicevalue)



########################################################################
# Task 8:
num1 = random.randrange(10,200,10)
num2 = random.randrange(5,20,5)
num3=num1/num2
print (str(num1) + " divided by " + str(num2) + " = ?")
guess= input("What is the answer?")

if int(guess)==num3:
    print("At least you got this correct")
else:
    print("Extra homework for you.")


####################################################################
# Additional exercise