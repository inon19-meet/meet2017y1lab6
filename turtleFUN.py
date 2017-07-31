import turtle

turtle.penup()

turtle.shape('turtle')

square =turtle.clone()

square.shape('square')

square.goto(0,0)

square.pendown()

square.goto(100,0)

square.goto(100,100)

square.goto(0,100)

square.goto(0,0)

triangle =turtle.clone()

triangle.shape('triangle')

triangle.pendown()

triangle.goto(0,0)

triangle.goto(100,0)

triangle.goto(100-50,100)

triangle.goto(50-50,0)

turtle.mainloop()
