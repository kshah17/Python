##tutorial 
#1

import pdb

pdb.set_trace()

a = "aaa"
b = "bbb"
c = "ccc"

final = a + b + c
print(final)

#2

import pdb
a = "aaa"
b = "bbb"
c = "ccc"

def final(var1,var2,var3):
    pdb.set_trace()
    return(var1+var2+var3)

print(final(a,b,c))


#3 

def tailRecursion(factorial, result = 1): #A function to find the factorial of a number using tail recursion
    if factorial == 1:
        return result
    else:
        return tailRecursion((factorial--),(factorial + result))


import pdb
def tailRecursion(factorial, result = 1):
    if factorial == 1:
        return result
    else:
        tempResult = factorial * result
        return tailRecursion((--factorial), tempResult)
print(tailRecursion(2,1))

#ex1

user_funds = 10.31
item_price == price["Burger"]

if item_price < user_funds:
    print("You have enough money!")
elif item_price = user_funds:
    print("You have the precise amount of money")
else item_price < user_funds:
    print("Sorry you don't have enough money")

#2

def product(n):
    total = 0
    for n in n:
        total *= i
return total

print(product([4,4,5]))


#3
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True
print(is_prime(17))

#4

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n = n + 1

print(item_list[4])
