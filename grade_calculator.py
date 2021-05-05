## grade calculator

print("Welcome to Grade Calculator")                                             # Welcome note

maths_mark = int(input("Please enter Maths Mark out of 100: "))                  # User inputs maths mark
physics_mark = int(input("Please enter Physics Mark out of 100: "))              # User inputs Physiscs mark
chemistry_mark = int(input("Please enter Chemistry Mark out of 100: "))          # User inputs chemistry mark
percentage = int((maths_mark + physics_mark + chemistry_mark) / 3)               # Averages marks

print (f"Your percentage Average is {percentage}")                               # prints percentage Average

if percentage > 70:                                                              # Prints scores using if loop
    print ("You achieved an A")
elif percentage >= 60:
    print ("You achieved a B")
elif percentage >= 50:
    print ("You achieved a C")
elif percentage >= 40:
    print ("You achieved a D")
else:
    print ("Unfortunately you Failed")