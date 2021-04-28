import turtle
import time
import random
import math
 
screen = turtle.Screen()
screen.setup(width = 600, height = 800)
screen.title =("Lyu Minen's snake")
screen.tracer(0)

def draw_snake(len):
 snakes = []
 head = turtle.Turtle()
 head.shape("square")
 head.color = ("red")
 head.penup()
 snakes.append(head)
 for i in range (1,len):
     body =turtle.Turtle()
     body.shape("square")
     body.color("blue")
     body.penup()
     body.goto(0-20*i,0)
     snakes.append(body)
 return snakes 

def move_snake():
  global snakes
  global head
  h_x = head.xcor()
  h_y = head.ycor()
  if h_x <= 280 and h_x >= -280 and h_y <= 280 and h_y >= -280:  
      for snake in range(len(snakes)-1,0,-1):     #make the next turtle stand on the position of the last one
         s_body = snakes[snake]
         pos_x = snakes[snake - 1].xcor()
         pos_y = snakes[snake - 1].ycor()
         s_body.goto(pos_x,pos_y)
      head.forward(20)

def right_snake():
    global snakes
    global head
    if head.heading() != 180:
        head.setheading(0)
        head.fd(20)

def left_snake():
    global snakes
    global head
    if head.heading() != 0:
     head.setheading(180)
     head.fd(20)

def up_snake():
    global snakes
    global head
    if head.heading != 270:
        head.setheading(90)
        head.fd(20)

def down_snake():
    global snakes
    global head
    if head.heading != 90:
       head.setheading(270)
       head.fd(20)

def draw_mons():
    mons = turtle.Turtle()
    mons.shape("square")
    mons.color("purple")
    mons.penup()
    return mons

# def move_mons(mons,time_first):
#     k = time_first
#     mons.speed("slowest")
#     t_now = time.time()
#     if t_now - k >= 1.0:
#         x = mons.xcor()
#         y = mons.ycor()
#         mons.towards(snakes[0].pos())
#         if x <= 280 and x >= -280 and y <= 280 and y >= -280:
#             mons.forward(5)
#         else:
#             mons.fd(0)
#         time_first = time.time()

def draw_foods():
    foods = []
    for i in range(9):
        food = turtle.Turtle()
        food.hideturtle()
        food.penup()
        food.goto(random.randint(-280,280),random.randint(-280,280))   #choose the position ranodmly
        food.write(str(i + 1),True,align="center")
        foods.append(food)
    return foods

def change_snake(exp_len):
    global snakes
    for i in range(exp_len):
        snake = turtle.Turtle()
        snake.shape("square")
        snake.color("blue")
        # snake.penup()
        snakes.insert(1,snake)     #make the new body into the second position



def check_eat():
    global foods
    global snakes
    global score_cur
    global head
    print(type(snakes[0]))
    # print(type(foods[2]))
    for i in range(len(foods)):
    #   pos = foods[i].pos()
    #   dis = snakes[0].distance(foods[i])
      food = foods[i]
      if head.distance(food) < 150:
          exp_len = i + 1
          foods[i].undo()
          snakes = change_snake(exp_len)
          score_cur = score(exp_len)


def score(exp_len):
    global score_cur
    score_cur = exp_len +score_cur
    return score_cur
    
def gameover():
    global snakes
    global head
    if head.distance(mons) < 15:
        game = False
        return game

def game_win():
    global snakes
    if len(snakes) == 46:
       print("win")
       return False
    else:
        return True

def on_Snake():
    move_snake()
    check_eat()
    screen.update()
    screen.ontimer(on_Snake,500)

def on_Mons():
    global snakes
    global mons
    d = mons.towards(snakes[0])
    l = abs(180 - d)
    r = abs(0 - d)
    u = abs(90 - d)
    d = abs(270 - d)
    min = l
    for i in [r,u,d]:
        if i > min:
            min = i
        else:
            continue
    if min == l:
        dir = 180
    if min == r:
        dir = 0
    if min == u:
        dir = 90
    if min == d:
        dir = 270
    
    mons.setheading(dir)
    mons.fd(20)
    screen.update()
    screen.ontimer(on_Mons,1000)

def g_start(x,y):
    screen.onscreenclick(None)

    screen.onkey(left_snake(),"Left")
    screen.onkey(right_snake(),"Right")
    screen.onkey(down_snake(),"Down")
    screen.onkey(up_snake(),"Up")

    screen.ontimer(on_Snake(),500)
    screen.ontimer(on_Mons(),1000)

# def play():
#     game = True
#     score_cur = 0
#     while game:
#         screen.onkey(right_snake(),"Right")
#         screen.onkey(left_snake(),"Left")
#         screen.onkey(up_snake(),"Up")
#         screen.onkey(down_snake(),"Down")

#         screen.update()
#         screen.ontimer(0.1)
#         move_snake()
#     # move_mons(mons,time_first)
#         score_cur = check_eat(score_cur)
#         game = gameover()
#         game = game_win()
# # t = turtle.Turtle()
# # t.penup()
# # t.down()
# # t.forward(40)
# # t.shape("square")
# # t.color("black","")
# # t.shapesize(500,500)

# # m = turtle.Turtle()
# # m.penup()
# # m.up()
# # m.forward(290)
# # m.shape("square")
# # m.color("black","")
# # m.shapesize(500,80)


# draw_snake(1)
# draw_mons()
# draw_foods()
# time_first = time.time()

# screen.onclick(play())
# screen.listen()
# screen.onkey(right_snake(),"Right")
# screen.onkey(left_snake(),"Left")
# screen.onkey(up_snake(),"Up")
# screen.onkey(down_snake(),"Down")





# screen.mainloop()

if __name__ == "__main__":
    snakes = draw_snake(1)
    foods = draw_foods()
    mons = draw_mons()
    score_cur = 0
    head = snakes[0]
    snakes[0] = head

    screen.onscreenclick(g_start)
    screen.update()
    screen.listen()
    screen.mainloop()
