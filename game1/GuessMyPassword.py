# guess my passworld.py

import random

resp1="try again"
resp2="possible, but not exact"
resp3="uncollect. it is easy that my password"
resp4="good job"
MY_PASSWORD="my password" #변수가 아닌 상수에는 대문자



def is_correct(guess, password):
    if guess == password:
        guess_correct =True
    else:
        guess_correct=False
    return guess_correct


#user_input = input("type text")
#print(user_input)

#############start
print("hi\n")
users_guess = input("type you guessed password")

#CHECKING PASSWORD
true_or_false = is_correct(users_guess, MY_PASSWORD)

#GAME RE START UTIL USER TYPE EXACT PASSWORD
while true_or_false == False:
    computer_response = random.randint(1,3)
    if computer_response ==1:
        print(resp1)
    elif computer_response==2:
        print(resp2)
    else:
        print(resp3)

        users_guess = input("\n what is next password?")
        true_or_false = is_correct(users_guess, MY_PASSWORD)

print(resp4)
input("\n type enter and than game will be end")
