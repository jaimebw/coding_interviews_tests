#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaime Bowen Varela
"""
Problem Statement
You are given a string of lower case letters. Your task is to figure out the index of 
the character on whose removal it will make the string a palindrome. 
There will always be a valid solution.
In case the string is already a palindrome, then -1 is also a valid answer along with possible indices.
Input Format
The first line contains T, i.e. the number of test cases.
T lines follow, each containing a string.
"""


def palindrome_index():
    num_cases = int(raw_input())
    for case in range(num_cases):
        s = raw_input()
        print(get_index(s))


def get_index(s):
    for i in range((len(s) + 1) // 2):  # seria 2
        if s[i] != s[len(s) - i - 1]:  # iter0 = s[0] != s[3], iter1 = s[1] != s[2]
            if is_palindrome(s[:i] + s[i + 1 :]):  # comprueba quitando el elemneto i de
                # de la palabra para comprobar si es palidnromo
                return i
            else:
                return len(s) - i - 1
    return -1


def is_palindrome(string):
    # comprueba si la función es palindromo
    for index, char in enumerate(string):
        if char != string[-index - 1]:
            return False
    return True


word = "anan"
print(get_index(word))
# print(is_palindrome(word))
