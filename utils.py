#한 줄 짜리 주석, 두줄 이상 3따옴표 사이
"""
코드 작성 일자: 23.03.10
코드 작성자: Ethan
코드 이름: utils.py
코드 목적: 유용한 함수를 따로 저장, 프리셋 목적
"""


def factorial(x):
    if x <= 1 :
        return 1
    return x * factorial(x-1)


def gugudan(x) :
        for i in range(9) :
            print((i+1) * x)




