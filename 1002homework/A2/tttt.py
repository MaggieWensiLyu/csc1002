# from turtle import *
# import time
# from winsound import PlaySound,SND_ASYNC
# import random

# tracer(10000000,0)
# size=200
# snakeSpeed=12
# stepNum=20
# stepSize=size/stepNum
# points=0
# direction=0
# snakeLen=4
# snake="0,0|-1,0|-2,0|-3,0|"
# fruit=[1,1]
# getFruit=False
# sleepTime=1/snakeSpeed

# setup(size+stepSize*10,size+stepSize*10)
# screensize(size,size)

# penup()
# goto(size/2+stepSize/2,size/2+stepSize/2)
# pendown()
# goto(size/2+stepSize/2,-size/2-stepSize/2)
# goto(-size/2-stepSize/2,-size/2-stepSize/2)
# goto(-size/2-stepSize/2,size/2+stepSize/2)
# goto(size/2+stepSize/2,size/2+stepSize/2)
# penup()

# def getSnake(barNum):
# 	barCount=0
#     STR=""
# 	x=0;y=0
# 	for i in range(len(snake)):
# 		if barCount==barNum:
# 			j=i
# 			while snake[j]!=',':
# 				STR+=snake[j]
# 				j+=1
# 			x=int(STR)
# 			j+=1
# 			STR=""
# 			while snake[j]!='|':
# 				STR+=snake[j]
# 				j+=1
# 			y=int(STR)
# 			break
# 		if snake[i]=='|':
# 			barCount+=1
# 	return [x,y]

# def move():
# 	#print("move!!!")
# 	#print(getFruit)
# 	newSnake=""
# 	if direction==0:
# 		readReturn=getSnake(0)
# 		newSnake+=str(readReturn[0]+1); newSnake+=","; newSnake+=str(readReturn[1]); newSnake+="|"
# 		for i in range(snakeLen-1):
# 			readReturn=getSnake(i)
# 			newSnake+=str(readReturn[0]); newSnake+=","; newSnake+=str(readReturn[1]); newSnake+="|"
# 	if direction==1:
# 		readReturn=getSnake(0)
# 		newSnake+=str(readReturn[0]); newSnake+=","; newSnake+=str(readReturn[1]-1); newSnake+="|"
# 		for i in range(snakeLen-1):
#             readReturn=getSnake(i)
# 			newSnake+=str(readReturn[0]); newSnake+=","; newSnake+=str(readReturn[1]); newSnake+="|"
# 	if direction==2:
# 		readReturn=getSnake(0)
# 		newSnake+=str(readReturn[0]-1); newSnake+=","; newSnake+=str(readReturn[1]); newSnake+="|"
# 		for i in range(snakeLen-1):
# 			readReturn=getSnake(i)
# 			newSnake+=str(readReturn[0]); newSnake+=","; newSnake+=str(readReturn[1]); newSnake+="|"
# 	if direction==3:
# 		readReturn=getSnake(0)
# 		newSnake+=str(readReturn[0]); newSnake+=","; newSnake+=str(readReturn[1]+1); newSnake+="|"
# 		for i in range(snakeLen-1):
# 			readReturn=getSnake(i)
# 			newSnake+=str(readReturn[0]); newSnake+=","; newSnake+=str(readReturn[1]); newSnake+="|"
# 	if getFruit==True:
# 		readReturn=getSnake(snakeLen-2)
# 		newSnake+=str(readReturn[0]); newSnake+=","; newSnake+=str(readReturn[1]); newSnake+="|"
# 		#print("GET FRUIT !!!!!!!!!!!!!!!!!!!!!!!!")
# 	return newSnake

# def drawSnake(clr):
# 	#print("drawSnake!!!")
# 	# if clr:
# 	# 	for i in range(snakeLen+2):
# 	# 		undo()
# 	#stepSize=size/stepNum
# 	pensize(stepSize-2)
# 	readReturn=getSnake(0)
# 	penup()
# 	goto(readReturn[0]*stepSize,readReturn[1]*stepSize,)
#     pendown()
# 	for i in range(snakeLen):
# 		readReturn=getSnake(i)
# 		goto(readReturn[0]*stepSize,readReturn[1]*stepSize,)
# 	penup()

# def check():
# 	#print("check!!!")
# 	readReturn=getSnake(0)
# 	global getFruit
# 	getFruit=False
# 	snkl=snakeLen
# 	for i in range(snakeLen-1):
# 		readReturn1=getSnake(i+1)
# 		if readReturn[0]==readReturn1[0] and readReturn[1]==readReturn1[1]:#hit self
# 			PlaySound("C:\\Windows\\media\\Windows Critical Stop.wav",SND_ASYNC)
# 			time.sleep(2)
# 			bye()
# 	if readReturn[0]>stepNum/2 or readReturn[1]>stepNum/2 or readReturn[0]<stepNum/-2 or readReturn[1]<stepNum/-2:#hit wall
# 		PlaySound("C:\\Windows\\media\\Windows Critical Stop.wav",SND_ASYNC)
# 		time.sleep(2)
# 		bye()
# 	if readReturn[0]==fruit[0] and readReturn[1]==fruit[1]:
# 		drawFruit()
# 		getFruit=True
# 		snkl=snakeLen+1
# 		PlaySound("C:\\Windows\\media\\Windows Hardware Insert.wav",SND_ASYNC)
# 	return snkl

# def drawFruit():
# 	#print("drawFruit!")
# 	pensize(stepSize+5)
# 	goto((fruit[0])*stepSize,fruit[1]*stepSize)
# 	color("white")
#     pendown()
# 	goto((fruit[0]+0.01)*stepSize,fruit[1]*stepSize)
# 	a=0
# 	while a!=snakeLen:
# 		fruit[0]=random.randint(stepNum/-2,stepNum/2)
# 		fruit[1]=random.randint(stepNum/-2,stepNum/2)
# 		a=0
# 		for i in range(snakeLen):
# 			readReturn=getSnake(i)
# 			if fruit[0]!=readReturn[0] or fruit[1]!=readReturn[1]:
# 				a+=1

# 	#outputStr='x'+str(fruit[0])+' y'+str(fruit[1])
# 	#print(outputStr)
# 	#stepSize=size/stepNum
# 	penup()
# 	goto((fruit[0])*stepSize,fruit[1]*stepSize)
# 	color("red")
# 	pendown()
# 	goto((fruit[0]+0.01)*stepSize,fruit[1]*stepSize)
# 	pensize(1)
# 	color("black")
# 	penup()
# 	goto(size/2+stepSize/2,size/2+stepSize/2)
# 	pendown()
# 	goto(size/2+stepSize/2,-size/2-stepSize/2)
# 	goto(-size/2-stepSize/2,-size/2-stepSize/2)
# 	goto(-size/2-stepSize/2,size/2+stepSize/2)
# 	goto(size/2+stepSize/2,size/2+stepSize/2)
# 	penup()

# def key_D():
# 	global direction
#     if direction!=2:
# 		direction=0
# 	#print("D!")
# def key_S():
# 	global direction
# 	if direction!=3:
# 		direction=1
# 	#print("S!")
# def key_A():
# 	global direction
# 	if direction!=0:
# 		direction=2
# 	#print("A!")
# def key_W():
# 	global direction
# 	if direction!=1:
# 		direction=3
# 	#print("W!")

# hideturtle()
# penup()
# pensize(size/stepNum-1)
# drawFruit()
# drawSnake(False)

# onkeypress(key_W,"Up")
# onkeypress(key_A,"Left")
# onkeypress(key_S,"Down")
# onkeypress(key_D,"Right")
# onkeypress(key_W,"w")
# onkeypress(key_A,"a")
# onkeypress(key_S,"s")
# onkeypress(key_D,"d")
# listen()
# while 1:
# 	time.sleep(sleepTime)
# 	color("white")
# 	drawSnake(True)
# 	snake=move()
# 	color("#235689")
# 	drawSnake(True)
# 	snakeLen=check()
# 	update()
# 	title(str(snakeLen-4))


# from turtle import *
# speed(2)
# def up():
# 	setheading(90)
# 	fd(30)
# def down():
# 	setheading(270)
# 	fd(30)
# listen()
# onkeypress(up,"Up")
# onkeypress(down,"Down")
# while True:
# 	fd(200)

# mainloop()
# import time
# game = True
# # snakes = draw_snake(1)
# # mons = draw_mons()
# # foods = draw_foods()
# score_cur = 0

# time_first = time.time()
# print(type(time_first))

# def move_mons(time_first):
#  k = time_first
#  t = time.time()
#  print(type(t))
#  print(type(k))
#  if k - t > 0:
# 	 print("yes")
#  else:
# 	 print("no")
# move_mons(time_first)

import turtle
li = []
k = 1
li.append(k)
# # turtle.reset()
t = turtle.Turtle()
# # t.shapesize(30,30)
# t = turtle.Turtle("square")
# # t.shape("square")
# t.color("black","")
# t.shapesize(500,500)
# # t.penup()
# # t.down()
t.forward(40)
li.append(t)

m = turtle.Turtle()
# m.shape("square")
# m.color("black","")
# m.shapesize(500,80)
# # m.penup()
# # m.up()
# # m.forward(290)

# # turtle.update()

# turtle.mainloop()
d = m.towards(t)
t.distance(m)
print(t.distance(m) <= 2)
# print(type(l))
print(li[0])