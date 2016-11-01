# mycalculator_expt1.py

from tkinter import*
from decimal import*
#키 임력 함수
def click(key):
    display.insert(END, key)

#######메인
window =Tk()
window.title("MyCalculator")

#내용 수정이 가능한 엔트리 위젯을 사용해 결과 디스플레이 사용
display = Entry(window, width=45, bg="light green")
display.grid()

#숫자 버튼 생성:
#def click1():
#    display.insert(END, "1")
#Button(window, text="1", width=5, command=click1).grid(row=1,column=0)

#숫자 버튼 프레임 생성
num_pad=Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

#숫자 버튼에 제공될 숫자:
num_pad_list=[
    '7','8','9',
    '4','5','6',
    '1','2','3',
    '0','.','=']

#반복문으로 숫자 버튼 생성
r=0 # 행 카운터
c=0 # 열 카운터

for btn_text in num_pad_list:
    Button(num_pad, text=btn_text, width=5,command=click).grid(row=r, column=c)
    c=c+1
    if c>2:
        c=0
        r=r+1

# 연산자 프레임 생성
operator=Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list=[
    '*','/',
    '+','-',
    '(',')',
    'C']

# 반복문 안에서 연산자 버튼 생성
r=0
c=0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c=c++1
    if c>1:
        c=0
        r=r+1

def my_function(x="default text"):
    print(x)
my_function("two")
my_function(3)
myfunction()


#######메인 반복문 실행
window,mainloop()
