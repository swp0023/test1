# mynmber.py
# 함수를 직접 만들어봅니다.

import random

#숫자를 골라봅시다.
computer_number = random.randint(1,100)

#is_same() 함수를 만듭니다.
def is_same(target, number):
    if target == number:
        result="win"
    elif target > number:
        result="low"
    else :
        result = "high"
    return result

#start game
print("hi \n i choose number that located inner from 1 to 100")

#receive input number guessing by user
guess=int(input("type number"))
#use is_same() fuction
higher_or_lower = is_same(computer_number, guess)

# game continue until user find number
if __name__ == '__main__':
    while higher_or_lower !="win":
        if higher_or_lower == "low":
            guess=int(input("higher than you thought. guess again.\n"))
        else :
            guess=int(input("lower than you thought. guess again.\n"))

        higher_or_lower=is_same(computer_number, guess)

# end game
input("\nbingo!\n good job.\n if you wanna finish this game, type enter.")

