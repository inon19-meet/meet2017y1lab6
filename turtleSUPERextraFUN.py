import turtle

UP_ARROW = "Up"

LEFT_ARROW = "Left"

DOWN_ARROW = "Down"

RIGHT_ARROW = "Right"

SPACEBAR = "space"


Up = 0

Left = 1

Down = 2

Right = 3

direction = Up

                            #***************go Up
def Up():    
    global direction
    direction = Up
    old_pos = turtle.pos()
    x = old_pos[0]
    y = old_pos[1]
    turtle.goto(x,y+10)
    print(turtle.pos))
    print("you pressed Up")

                            #***************go Left
def Left():
    global direction
    direction = Left
    x = old_pos[1]
    y = old_pos[2]
    turtle.goto(x-10,y)
    print(turtle.pos))
    print("you pressed Left")
    
                            #***************go Down
def Down():
    global direction
    direction = Down
    x = old_pos[2]
    y = old_pos[3]
    turtle.goto(x,y-10)
    print(turtle.pos))
    print("you pressed Down")

                             #**************go Right
def Right():
    global direction
    direction = Right
    x = old_pos[3]
    y = old_pos[4]
    turtle.goto(x+10,y)
    print(turtle.pos))
    print("you pressed Right")

                             #***************onkeypress
    #Up***********************
turtle.onkeypress(Up,UP_ARROW)
    #Left******************************
turtle.onkeypress(Left,LEFT_ARROW)
    #Down************************
turtle.onkeypress(Down,DOWN_ARROW)
    #Right***************************
turtle.onkeypress(Right,RIGHT_ARROW)
    #tuertle.listen**********************&&!!!!!!!!!!!!!!!11
turtle.listen()

























    
