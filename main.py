<<<<<<< HEAD
import turtle
t=turtle.Turtle()
for i in range(30):
    t.forward(i*10)
    t.right(90)

turtle.done()
=======
# Inheritance

class humans():
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def display(self):
        print(self.color)
        print(self.weight)

class me(humans):
    def __init__(self, color, weight):
        super().__init__(color, weight)

ob1 = humans("Brown", "2kg")
ob2 = me("red", "2.5kg")

ob2.display()
>>>>>>> f8092a95e889da926979689dd06d750a9009209d
