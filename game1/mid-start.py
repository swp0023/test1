# my magic 8 ball = shorter version

import random
#답을 튜플에 적습니다.

answers = (
    "do it!",
    "that's okay",
    "what",
    "you dont know",
    "your crazy",
    "you can do it",
    "you dont need doing it",
    "yes your right."
)

print("my magic 8 ball에 오신 것을 환영합니다.")

question=input("질문을 입력하고 엔터치세요.\n")

print("고민중..."*4)
choice = random.randint(0,7)
print(answers[choice])
input("\n\n 마치려면 엔터키를 누르세요.")
