import turtle
import random
import time

x=[random.randrange(0,100) for x in range(10)]
ts=[]
cnt=20
for j in range(len(x)):
  ts.append(turtle.Turtle())
  ts[j].hideturtle()
  ts[j].penup()
  ts[j].goto(cnt,0)
  ts[j].pendown()
  ts[j].write(x[j])
  cnt+=20
pos=turtle.Turtle()
pos.hideturtle()
def current_pos(start,st):
  pos.speed(0)
  pos.clear()
  pos.penup()
  if st==0:
    pos.fd(15)
    pos.rt(90)
    pos.fd(5)
  else:
    pos.fd(start)
    pos.rt(90)
  pos.pendown()
  pos.lt(90)
  pos.fd(20)
  pos.lt(90)
  pos.fd(20)
  pos.lt(90)
  pos.fd(20)
  pos.lt(90)
  pos.fd(20)
  pos.lt(90)
for i in range(len(x)):
  cnt=20
  for j in range(len(x)):
    current_pos(cnt,j)
    if j<len(x)-1 and x[j]<x[j+1]:
      x[j],x[j+1]=x[j+1],x[j]
      ts[j].clear()
      ts[j].left(90)
      ts[j].penup()
      ts[j].fd(40)
      ts[j].pendown()
      ts[j].write(x[j+1])
      ts[j].penup()
      ts[j].backward(40)
      ts[j].right(90)
      time.sleep(1)
      ts[j+1].clear()
      time.sleep(1)
      ts[j].clear()
      ts[j].write(x[j])
      ts[j+1].write(x[j+1])
      time.sleep(1)
      

