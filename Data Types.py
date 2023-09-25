from math import *

num_int = 10 # this is an integer
num1_int = 9    # this is an integer
num_float = 5.0 # this number is a float
num1_float = 2.1 # this number is a float
num2_float = 2.9 # this number is a float
print(num_int * (num_int + num_float))

print(num_int % 3) #to find the reaminder

print(max(num_int, 9))
print(max(num_int, 21))

print(abs(-num_int))
print(abs(num_int))

print(pow(num_int, 2)) #power of int
print(pow(num_int, 3))

print(round(num1_float))
print(round(num2_float))

print(floor(num1_float))  #chop off the decimal point
print(floor(num2_float))

print(ceil(num1_float)) #round the number up
print(ceil(num2_float))

print(sqrt(num_int))
print(sqrt(num1_int))

import math as m
print(m.exp(num_int))
print(m.exp(num1_int))
