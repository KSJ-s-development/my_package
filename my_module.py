from .. import out # 현재 폴더의 out.py 파일을 호출

def my_function():
    print("모듈 내에 있는 함수")

my_variable = "모듈 내에 있는 변수"

print("my_module.py",__name__)
print("out.py",out.__name__)
