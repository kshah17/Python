### class : students 
## attributes : name, age, class
# method: prints average of 3 inputted test scores

class student:
  def __init__(self, name, age, class_ = "student"):
    self.name = name
    self.age = age
    self.class_ = class_
  def average(self, mark1, mark2, mark3):
    self.mark1 = mark1
    self.mark2 = mark2
    self.mark3 = mark3
    print("Your average is: ", (mark1 + mark2+ mark3) / 3)

john = student("john", 5, )
jane = student("jane", 2, )
john.average

print(getattr(jane, "age"))

#self.a =
self.b = 
self.c =
class.method

##example
class Dog:
	energy = "high"
	def speak(self):
		print ("woof")
bilbo_waggins =Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak()
