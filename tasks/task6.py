# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    a,b,c=map(int,input().split())
    print(a**2 + b**2 == c**2 or a**2 +c**2 == b**2 or b**2 + c**2 == a**2)
   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()