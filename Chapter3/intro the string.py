# 1. What is a String in Python?
# A string is a sequence of characters (letters, numbers, or symbols) enclosed in quotes (" " or ' ').
# examples
name = "Anas"
country = "Pakistan"


# this is positvie slicing 
# what is string slicing?
# String slicing means extracting a specific part of a string.
# example
country = "palestine"
# example 1 for understand
# print(country[start:end])
print (country[1:3]) # python counts from 0:[1:3]starts at index 1 and stops right before index 3.


# nagitive slicing
friend = "manan"
print(friend[-4:-1])
print(friend[1:4])


dost = "hamza"
print(dost[:4]) #start from zero ends with name end menas empty menas full.
print(dost[2:]) #start with 2 ends with name end 


#[start:end:steps]
alp = "anaskhan"  #a  n  a  s  k  h  a  n
print(alp[1:3:4]) #0  1  2  3  4  5  6  7

abc = "abcdefghi23456"
print(abc[1:14:5])