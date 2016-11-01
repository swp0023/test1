# my magic 8 ball

import random

#답변을 입력해봅시다.

ans1="자! 해보세요!"
ans2="됐네요, 이사람아!"
ans3="what? say again"
ans4="afraid because you dont know"
ans5="you are crazy"
ans6=" yes, you can do it"
ans7="you dont need doing it"
ans8="yes, your right."

print("mymagic8ball에 오신 것을 환영합니다.")
#사용자의 질문을 입력 받습니다.
question = input("조언을 구하고 싶으면 질문을 입력하고 엔터키를 누르세요.\n")
print("고민 중...\n"*4)

#질문에 알맞은 답변을 하는 일에 raindint()을 사용합니다.
choice=random.randint(1,8)
if choice==1:
    answer=ans1
elif choice==2:
        answer=ans2
elif choice==3:
        answer=ans3
elif choice==4:
        answer=ans4
elif choice==5:
        answer=ans5
elif choice==6:
        answer=ans6
elif choice==7:
        answer=ans7
else : answer=ans8

#화면에 답변을 출력합니다.
print(answer)

input("\n\n 마치려면 엔터 키를 누르세요.")
