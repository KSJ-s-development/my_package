from my_package import my_module

print(__name__)
print(my_module.__name__)

if __name__ == "__main__":
    print("코드 실행")