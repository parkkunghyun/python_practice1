#  모듈과 패키지
# import random -> random.randint(1,1000)->모듈을 모아놓은 단위 -> 패키지임!
# module == py를 의미 같은 폴더에 있는애는 import로 가져오기!


import fah_converter #모든 코드가 메모리로 로딩! 모듈의 이름적고 함수명을 적어주면 작동함
# 같은 폴더안에 있을경우만 가능
print("Enter a celsius value: ")
celcius = float(input())
fahrenheit = fah_converter.convert(celcius)
print(f'{fahrenheit}')

# __pycache__라는 폴더가 생김 -> 컴파일된 파일임!, 코드를 쉽게 로딩할수있게 파이썬 인터프리터가 먼저 컴파일해줌! -> 즉 기계어로 번역했다고 생각하면됨
# 모듈안에는 함수와 클래스등이 존재가 가능 -> 일부만 로딩하기
# namespace하기 -> import fah_converter as fah 별명 -> 이게 읽는 입장에서 편함!
# from fah_converter import convert

# 파이썬 기본제공라이브러리
import time
print(time.localtime())
import random
print(random.randint(1,100))

# 패키지 -> 대형프로젝트를 만드는 코드의 묶음, __init__, __main__등 키워드 파일명이 사용됨
