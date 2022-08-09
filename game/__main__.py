from sound import echo
# 패키지내 다른 폴더의 모듈을 부를때는 상대참조로 부른다 ..soud.echo등
# 폴더 자체를 실행시킬수 있다
if __name__ == '__main__':
    print("hello game")
    print(echo.echo_play())


