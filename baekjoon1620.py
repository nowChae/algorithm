N, M =map(int,input().split())
import sys
input = sys.stdin.readline

number_book = {}
name_book = {}
n=1

for _ in range(N):
    name = input().strip()
    number_book[n] = name
    name_book[name] = n
    n += 1

for _ in range(M):
    question = input().strip()
    
    if question.isalpha():
        print(name_book[question])
    elif question.isdigit():
        print(number_book[int(question)])
