name = str(input("please enter first name: "))
luckynumber = int(input("please enter your lucky number: "))
answer  = name + str(luckynumber) 

print(name, +luckynumber, "=", answer)


def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)

print(added_number + 20)



def absolute_value(num):

    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))

print(absolute_value(-4))