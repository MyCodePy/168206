#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A = ['A:我没有偷钻石。         ',False,False]
B = ['B:D就是罪犯。            ',False,False]
C = ['C:B是盗窃这块钻石的罪犯。',False,False]
D = ['D:B有意诬陷我。          ',False,False]
Z = [A,B,C,D]


def RE():
    for i in Z:
        i[1] = False 

def com():
    for i in Z:
        RE()#清0
        i[1] = True
        if A[1] == B[1] and B[1] != D[1]:
            break
    if not A[1]:
        A[2] = not A[1]

def main():
    com()
    for i in Z:
        if i[2] and not i[1]:
            print(i[0],end = '-->假话...罪犯！\n')
        elif i[1]:
            print(i[0],end = '-->真话...\n')
        else:
            print(i[0],end = '-->假话...\n')
            

main()
'''
#方法二
for people in ['A','B','C','D']:
    if (people=='A')+(people!='B')+(people!='D')+(people=='D') == 3:
        print(people +'是罪犯！')
'''
