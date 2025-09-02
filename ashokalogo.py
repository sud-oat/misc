import turtle
def draw_curve(angle, direction, forward_length, curve_length, remove_angle):
   t.penup()
   t.goto(0, -70)
   t.circle(70, angle, steps=100)  # positioning
   t.pendown()
   t.fillcolor("white")
   t.pencolor("white")  # Added pencolor
   t.begin_fill()
   t.circle(165, direction * curve_length, steps=100)  # curved pattern
   if forward_length > 0:
       t.penup()
       t.right(remove_angle * -direction)
       t.forward(direction * forward_length)
       t.pendown()
   t.end_fill()
   t.setheading(0)

def draw_circle(size, fill_color):
   t.penup()
   t.goto(0, -size)
   t.pendown()
   t.fillcolor(fill_color)
   t.pencolor(fill_color)  # Added pencolor
   t.begin_fill()
   t.circle(size, steps=100)
   t.end_fill()
 
def draw_round(curve_length, forward_length, remove_angle):
   curr = 0
   for i in range(10):
       draw_curve(curr, 1, forward_length, curve_length, remove_angle)
       curr += 36
   
   curr = 0
   for i in range(10):
       draw_curve(curr, -1, forward_length, curve_length, remove_angle)
       curr -= 36

t = turtle.Turtle()
t.speed(0)  # maximum speed
t.pensize(1)

draw_circle(255, "#c51230")
draw_round(150, 10, 0)
draw_circle(234, "#c51230")
draw_round(125, 20, 65)
draw_circle(203, "#c51230")
draw_round(99, 30,76)
draw_circle(169, "#c51230")
draw_round(-75, 30,75)
draw_circle(135, "#c51230")
draw_round(55, 30,75)
draw_circle(108, "#c51230")
draw_round(39,30,75)
draw_circle(90, "#c51230")
draw_round(27,30,75)
draw_circle(77, "white")

t.hideturtle()
turtle.done()
