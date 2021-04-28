from math import sqrt
import turtle
import random
import time
screen = turtle.Screen()
screen.setup(1000,800)
screen.bgcolor("white")
screen.title("Snake by Lyu Minen")
# up = turtle.Turtle()
# up.shape("square")
# up.shapesize(50,80)
# up.color("black", "")
# down = turtle.Screen()
# down.setup(500,500)
# t = turtle.Turtle()
# t.penup()
# t.goto(0,80)
# t.pendown()
# t.shape("square")
# t.color("black","")
# t.resizemode("user")
# t.shapesize(5,5,12)
# t.resizemode("auto")
screen.tracer(0)   # make teh refresh to manual

def find_pos():
    # pos = 
    # return pos
    pass
def creat_food():
    for i in range(9):
        food = turtle.Turtle()          #creat a small turtle to make sure the number can be eat properly
        food.hideturtle()
        num = turtle.Turtle()
        num.write(str(i),align = "center", font = ("Arial",30, "normal"))
        i += 1
        food.up()
        num.up()
        pos = random.choice(find_pos())   #randomly put the food
        food.goto(pos)
        num.goto(pos)
        food.down()
        num.down()

def creat_mons():
    mons = turtle.Turtle()
    mons.color("purple")
    mons.speed("slow")

def mons_move(mons,head):
    pos_head_x,pos_head_y = head.pos()
    mons.up()
    #find the shortest distance
    l = mons.distance(head.pos())
    r = mons.distance(head.pos())
    u = mons.distance(head.pos())
    d = mons.diatance(head.pos())
    dis = [d]
    dis.append(l)
    dis.append(r)
    dis.append(u)
    dir_curr = min(dis)
    if dir_curr == l :
     mons.heading((0,pos_head_y))
    elif dir_curr == r:
        mons.heading((660,pos_head_y))
    elif dir_curr == u:
        mons.heading((pos_head_x,0))
    else:
        mons.heading((pos_head_x,740))
    mons.up()            #move the monster
    mons.forward()
    time_0 = time.time()
    if time.time() - time_0 == 3: #every three time unit, refresh the monster
     mons.down()
     time_0 = time.time()

def creat_snake(body_len):
    head = turtle.Turtle()
    head.color("red")
    len = 1
    while body_len > len:
        body = head.clone()  #make sure the snake body are the same with the head
        body.color("blue")
        len += 1
    return len

def snake_move():
    pass

def check_lose(head,mons):
   if  mons.diatance(head.pos()) <= sqrt(5):
       game = False
       print("Game over")
   return game

def check_win(len):
    if len == 50:
        game = False
        print("Win")
    return game

def eat(food,head,len,score):
    distance = food.distance(head.pos())
    if distance <= sqrt(5):
        # len = food.   #cannot tell the number
        score += 1
        pass

   
    

turtle.listen()
turtle.mainloop()
