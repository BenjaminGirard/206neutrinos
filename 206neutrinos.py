#!/usr/bin/env python3
## neutrinos.py for  in /home/tetard/EPITECH_Y2/maths/206neutrinos
## 
## Made by benjamin girard
## Login   <tetard@epitech.net>
## 
## Started on  Fri May  5 17:11:06 2017 benjamin girard
## Last update Fri May  5 17:38:30 2017 benjamin girard
##

import sys
import formula

def try_int2(strint):
    try:
        res = int(strint)
        return res
    except ValueError:
        return "NOP"

def try_int(strint):
    try:
        ret = int(strint)
        if ret < 0:
            sys.exit(84)
        return ret
    except ValueError:
        sys.exit(84)

def args():
    if (len(sys.argv) != 5):
        sys.exit(84)
    res = [try_int(sys.argv[1]), try_int(sys.argv[4]), try_int(sys.argv[2]), 0, try_int(sys.argv[3])]
    return res

def get_line():
    try:
        line = input("indtast din vaerdi : ")
    except EOFError:
        sys.exit(0)
    if line == "ENDE":
        return line
    while try_int2(line) == "NOP":
        try:
            line = input("indtast din vaerdi : ")
        except EOFError:
            sys.exit(0)
    return line

if __name__ == "__main__":
    res = args()
    line = get_line()
    while line != "ENDE":
        formula.actualize_res(res, line)
        formula.print_all(res)
        line = get_line()
