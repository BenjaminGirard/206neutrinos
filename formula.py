#!/usr/bin/env python3
## formula.py for  in /home/tetard/EPITECH_Y2/maths/206neutrinos
## 
## Made by benjamin girard
## Login   <tetard@epitech.net>
## 
## Started on  Fri May  5 17:09:40 2017 benjamin girard
Last update Tue Oct 10 23:51:09 2017 benjamin
##

from math import sqrt

def average(res, line):
    result = res[2] * (res[0] - 1)
    result += int(line)
    res[2] = result / res[0]

def standard_dev(res, line):
    stdev = (res[1] ** 2) * (res[0] - 1)
    stdev += (int(line) - res[2]) ** 2
    res[1] = sqrt(stdev / res[0])

def harmonic_average(res, line):
    haverage = (res[0] - 1) / res[4]
    haverage += 1.0 / float(line)
    res[4] = res[0] / haverage

def quadratic_average(res, line):
    qaverage = ((res[1] ** 2) + (res[2] ** 2)) * (res[0] - 1)
    qaverage += float(line) ** 2
    res[3] = sqrt(qaverage / res[0])

def actualize_res(res, line):
    res[0] += 1
    quadratic_average(res, line)
    harmonic_average(res, line)
    average(res, line)
    standard_dev(res, line)

def print_all(res):
    print("antal mãlinder :\t\t{}".format(res[0]))
    print("standardafvilgelse :\t\t{:.2f}".format(res[1]))
    print("aritmetisk gennemsnit :\t\t{:.2f}".format(res[2]))
    print("kvadratisk gennemsnit :\t\t{:.2f}".format(res[3]))
    print("harmonisk gennemsnit :\t\t{:.2f}".format(res[4]))
    print("")
