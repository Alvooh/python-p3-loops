#!/usr/bin/env python3

def happy_new_year():
    num = 10 
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")


def square_integers(int_list):
    new_list = list()
    for i in int_list:
        new_item = i * i
        new_list.append(new_item)
    return new_list

    
    # code goes here!
    pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
  
        elif i % 3 == 0:
            print("Fizz") 

        elif i  % 5 == 0 :
            print("Buzz")
        
        else:
            print(i)

    
