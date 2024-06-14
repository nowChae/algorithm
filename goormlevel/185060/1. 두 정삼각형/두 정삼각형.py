# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
import copy
input = sys.stdin.readline

n = int(input())
A = []
B = []

for _ in range(n):
	A.append(list(map(int, input().split(' '))))
for _ in range(n):
	B.append(list(map(int, input().split(' '))))
	
	
def symm(A, n):
	changed_A = copy.deepcopy(A)
	
	for i in range(n):
		for j, a in enumerate(A[i]):
			changed_A[i][i - j] = a
			
	return changed_A

def turn(A, n):
	changed_A = copy.deepcopy(A)
	
	for i in range(n):
		for j in range(len(A[i])):
			changed_A[i][j] = A[(n-1)-i+j][(n-1)-i]
		
	return changed_A
	
turn(A, n)
	
def compare(A, B, n):
	result = 0
	for i in range(n):
		for j in range(len(A[i])):
			if A[i][j] != B[i][j]:
				result += 1
				
	return result
	
com_rst = []
one_turn = turn (A, n)
two_turn = turn(one_turn, n)
sym = symm(A, n)
sym_one_turn = turn(sym, n)
sym_two_turn = turn(sym_one_turn, n)

com_rst.append(compare(A,B,n))
com_rst.append(compare(one_turn,B,n))
com_rst.append(compare(two_turn,B,n))
com_rst.append(compare(sym,B,n))
com_rst.append(compare(sym_one_turn,B,n))
com_rst.append(compare(sym_two_turn,B,n))
print(min(com_rst))