from my_package import my_module # my_package폴더의 my_module.py 파일을 호출

print(__name__)
print(my_module.__name__)

if __name__ == "__main__":
    print("코드 실행")