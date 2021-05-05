## With Statement Example 
'''
with open("filename.txt", "w") as file:
    for n in range(1,11):
        newline = "This is line" + str(n) + "\n"
        file.write(newline)
'''

## Keeps even lines and discards odd ones
'''
file = open("filename.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("filename.txt", "w")
file.write(outfile)
file.close()
'''
## Opens files and prints first, third and first(again) lines
'''
file = open("filename.txt", "r")

print(file.readline())
file.readline()
print(file.readline())
file.seek(0)
print(file.readline())

file.close()
'''

## Excercises
#1 - read and display 1st and 4th team
'''
file = open("teams.txt", "r")

for line in range (1,5):
    if line == 1 or line % 4 == 0:
        print(file.readline())
    else:
        file.readline()

file.close()
'''
''' 
#2 Edit top line so it is replaced with "This is a new line" 
## print out edited file line by line

# incorrect
with open("teams.txt", "w") as file:
    for line in range (1,5):
        if line == 1:  
            newline = "this is a new line" 
            file.write(newline)
       

file = open("teams.txt", "r")
lines = file.readline()
print(lines)

file.close()

## Correct
a_file = open("teams.txt", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "This is a new line\n"

a_file = open("teams.txt", "w")
a_file.writelines(list_of_lines)
a_file.close()

'''