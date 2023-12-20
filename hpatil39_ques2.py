#!/usr/bin/env python3

import sys
count = 0
def pair(input: str ) -> None:
    """
    Checks if parentheses are paired correctly 
    if ch encounters '(', it increments count by 1
    if ch encounters ')', it decrements count by 1
     If the count goes negative, the loop is terminated with a break statement which means
     there are more ) than (
    If count is equal to 0, it means that the parentheses are correctly paired, and it prints "paired"
    """
for ch in input("Enter the Newick string: "):
    if ch == '(': count += 1
    elif ch == ')': count -= 1
    if count < 0: break
print("paired" if count == 0 else "not paired")

pair(input)