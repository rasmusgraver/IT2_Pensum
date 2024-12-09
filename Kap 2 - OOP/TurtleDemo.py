# NB: Installer turtle med:
# pip3 install PythonTurtle  
from turtle import Turtle, Screen

padde = Turtle()
padde.speed(2)
farger = ["red", "green", "blue", "orange", "black", "purple"]
for farge in farger:
    padde.color(farge)
    padde.forward(100)
    padde.left(60)

# Om man trenger å endre noe på screen (som bakgrunsfarge)
screen = Screen()
# Men også: exitonclick - vinduet blir stående (og forsvinner ikke med en gang)
screen.exitonclick()
