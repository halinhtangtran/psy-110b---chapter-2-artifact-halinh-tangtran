##Programming Project 01: Arithmetic Tutor
##Ha Linh Tang Tran

##import the random module
import random

print("Welcome to the Arithmetic Tutor :)")

acceptable_choices = ["n","N","y","Y"]


while True:
    user_choice = input("\nDo you want to practice arithmetic? (y/n) ")

##if input not in list, ask again
    if user_choice not in acceptable_choices:
        print("Enter 'Y' or 'y' to continue. Enter 'N' or 'n' to stop.")

##if user says 'no', end program
    elif (user_choice == "n") or (user_choice == "N"):
        print("Thank you for using. Goodbye!")
        break

##if user says 'yes', continue
    else:
##generate random numbers
        num_1 = random.randint(1,100)
        num_2 = random.randint(1,100)

##generate random equations and assign correct answers
        random_i = random.randint(1,3)
        random_equation = ""
        if random_i == 1:
            random_equation = "+"
            correct_answer = num_1 + num_2
            
        elif random_i == 2:
            random_equation = "-"
##make sure that the results for substrations not negative
            if num_2 > num_1:
                num_2 = random.randint(1, num_1)
            correct_answer = num_1 - num_2
    
        else:
            random_equation = "*"
            correct_answer = num_1 * num_2
            
##user can only have 3 attempts
        attempt_count = 0
        while attempt_count < 3:
##get user's answer
            user_answer = input("\nWhat is "
                                + str(num_1) + " "
                                + random_equation + " "
                                + str(num_2) + "? ")
            
##if wrong answer, ask to answer again
##if answer wrong 3 times, give correct answer and move to the next problem
##if answer correct, break and loop again
            if int(user_answer) != correct_answer:
                attempt_count += 1
                if attempt_count == 3:
                    print("\nSorry, that's incorrect! The correct answer is"
                          , correct_answer)
                else:
                    print("\nSorry, that's incorrect!")
            else:
                print("\nCorrect!")
                break

            






    









