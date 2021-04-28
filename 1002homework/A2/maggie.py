import turtle
import time
import random
import math

screen = turtle.Screen()
screen.setup(width = 1000, height = 800)
screen.title =("Lyu Minen's snake")
screen.tracer(0)

g_snakes = []
g_mons = None
g_left_t = None
g_mid_t = None
g_right_t = None
g_contact = None
g_state = None
g_time = None
g_game = True 
g_time_first = time.time()
g_time = 0
# g_head = None

def draw_snake(len):
 s = []
 h = turtle.Turtle()
 h.shape("square")
 h.color = ("red")
 h.penup()
 s.append(h)
 for i in range (1,len):
     body =turtle.Turtle()
     body.shape("square")
     body.color("blue")
     body.penup()
     body.goto(0-20*i,0)
     s.append(body)
 return s 

def move_snake():
  global g_state
  global g_game
#   g_game = game_win()
#   g_game = gameover() 
  if g_game == True: 
    h_x = g_head.xcor()
    h_y = g_head.ycor()
    if h_x <= 250 and h_x >= -250 and h_y <= 250 and h_y >= -250:  
        for snake in range(len(g_snakes)-1,0,-1):     #make the next turtle stand on the position of the last one
            s_body = g_snakes[snake]
            pos_x = g_snakes[snake - 1].xcor()
            pos_y = g_snakes[snake - 1].ycor()
            s_body.goto(pos_x,pos_y)
        g_head.forward(20)
    else:
        g_state = "Pause"
  g_game = game_win()
  g_game = gameover()

def right_snake():
    global g_state
    if g_head.heading() != 180:
        g_head.setheading(0)
        g_state = "Right"
        # g_snakes[0].fd(20)

def left_snake():
    global g_state
    print('left snake')
    if g_head.heading() != 0:
     g_head.setheading(180)
     g_state = "Left"
    #  g_head.fd(20)

def up_snake():
    global g_state
    if g_head.heading != 270:
        g_head.setheading(90)
        g_state = "Up"
        # g_head.fd(20)

def down_snake():
    global g_state
    if g_head.heading != 90:
       g_head.setheading(270)
       g_state = "Down"
    #    g_head.fd(20)

def draw_mons():
    m = turtle.Turtle()
    m.shape("square")
    m.color("purple")
    m.penup()
    m.goto(-120,-40)
    return m

def on_dir_mons():
    d = g_mons.towards(g_head)
    l = abs(180 - d)
    r = abs(0 - d)
    u = abs(90 - d)
    d = abs(270 - d)
    min = l
    for i in [r,u,d]:
        if i < min:
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
    
    # screen.update()
    # screen.ontimer(on_dir_mons,500)
    return dir
    

def draw_foods():
    foods = []
    for i in range(9):
        food = turtle.Turtle()
        food.hideturtle()
        food.penup()
        food.goto(random.randint(-250,250),random.randint(-250,250))   #choose the position ranodmly
        food.write(str(i + 1),True,align="center")
        foods.append(food)
    return foods

def change_snake(exp_len):
    for i in range(exp_len):
        snake = g_snakes[1].clone()  #copy the previous body
        # snake.hideturtle()
        # snake.shape("square")
        # snake.color("blue")
        # snake.penup()
        g_snakes.insert(1,snake)     #make the new body into the second position
        # snake.showturtle()

def check_Contact():
    global g_contact
    for i in range (len(g_snakes)):
        if g_snakes[i].distance(g_mons) < 15:
            g_contact += 1
            break


def check_eat():
    global foods
    global score_cur
    # print(type(g_snakes[0]))
    # print(type(foods[2]))
    for i in range(len(foods)):
    #   pos = foods[i].pos()
    #   dis = snakes[0].distance(foods[i])
      food = foods[i]
      if g_head.distance(food) < 15:
          exp_len = i + 1
          foods[i].undo()
          g_snakes = change_snake(exp_len)
          score_cur = score(exp_len)


def score(exp_len):
    global score_cur
    score_cur = exp_len +score_cur
    return score_cur
    
def gameover():
    res = g_head.distance(g_mons) < 15
    if(res):
        print('lose game')
        g_mons.write("game over")
    return res

def game_win():
    if len(g_snakes) == 46:
       print("win")
       g_mons.write("win")
       return True
    else:
        return False

def on_Snake():
    move_snake()
    check_eat()
    screen.update()
    screen.ontimer(on_Snake,500)

def on_Mons():
    # global snakes
    global g_game
    # g_game = game_win()
    # g_game = gameover()
    if g_game == True: 
        print('on_mons', len(g_snakes))
    
        dir = on_dir_mons()
         
        g_mons.setheading(dir)
        g_mons.fd(20)
        screen.update()
        screen.ontimer(on_Mons,1000)
    g_game = game_win()
    g_game = gameover()

def on_Write():
    global g_time
    time_now = time.time()
    g_time =  int(time_now - g_time_first)

    g_left_t.clear()
    g_right_t.clear()
    g_mid_t.clear()

    g_left_t.write("Contact :" + str(g_contact))
    g_mid_t.write("Time:" + str(g_time))
    g_right_t.write("Status:" + g_state)
    screen.update()
    screen.ontimer(on_Write(),1200)

def g_start(x,y):
    global g_time_first
    # global g_game
    screen.onscreenclick(None)
    # g_time_first = time.time()
    # g_left_t.write("Contact :" + str(g_contact))
    # g_mid_t.write("Time:" + str(g_time))
    # g_right_t.write("Status:" + g_state)
    # while game:
    screen.onkey(left_snake,"Left")
    screen.onkey(right_snake,"Right")
    screen.onkey(down_snake,"Down")
    screen.onkey(up_snake,"Up")
    # g_game = game_win()
    # g_game = gameover()
    # time_now = time.time()
    # g_time =  int(time_now - g_time_first)
    # screen.ontimer(on_Write(),1100)
    screen.ontimer(on_Snake(),500)
    screen.ontimer(on_Mons(),1000)
    screen.ontimer(on_Write(),1100)

        # g_game = game_win()
        # g_game = gameover()
        # time_now = time.time()
        # g_time =  int(time_now - time_first)      

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



t = turtle.Turtle("square")
t.pensize(8)
t.penup()
t.goto(-250,250)
t.pendown()
t.pencolor("black")
t.setheading(0)
t.hideturtle()
t.forward(500)
t.right(90)
t.forward(500)
t.right(90)
t.forward(500)
t.right(90)
t.forward(580)
t.right(90)
t.forward(500)
t.right(90)
t.forward(80)
t.right(90)
t.forward(500)
# g_left_t = turtle.Turtle()
# g_right_t = turtle.Turtle()
# g_mid_t = turtle.Turtle()


# screen.mainloop()

if __name__ == "__main__":
    # turtle.shapesize(500,580)
    # turtle.shape("square")
    # turtle.color("black","")
    # t = turtle.Turtle()
    # t.ht()
    # t.goto(-250,520)
    # t.pensize(80)
    # t.setheading(0)
    # t.forward(500)
    g_left_t = turtle.Turtle()
    g_right_t = turtle.Turtle()
    g_mid_t = turtle.Turtle()
    g_mid_t.hideturtle()
    g_right_t.hideturtle()
    g_left_t.hideturtle()
    g_left_t.penup()
    g_left_t.goto(-200,290)
    g_right_t.penup()
    g_right_t.goto(130,290)
    g_mid_t.penup()
    g_mid_t.goto(20,290)
    g_contact = 0
    g_state = " "
    g_time = 0

    t = turtle.Turtle("square")   
    t.shapesize(500,80)
    t.color("black","")
    t.up()
    t.goto(0,290)
    g_snakes = draw_snake(3)
    print(len(g_snakes))
    foods = draw_foods()
    g_mons = draw_mons()
    score_cur = 0
    g_head = g_snakes[0]
    # snakes[0] = head

    screen.onscreenclick(g_start)
    screen.update()
    screen.listen()
    screen.mainloop()
