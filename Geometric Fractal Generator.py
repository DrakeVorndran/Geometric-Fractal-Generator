import turtle
from math import *

def uI(question,typ):
  while True:
    
    try:
      if(typ!=bool):
        userIn = typ(raw_input(question))
      else:
        userIn = (raw_input(question)).upper()
        if(userIn=="TRUE"):
          return(True)
        elif(userIn=="False"):
          return(False)
        else:
          userIn = int("if it works it works")

      break
    except(ValueError):
      print"Oops, that is not a "+str(typ)
  return userIn

colors = ["#000000","#30BCED","#303036","#F18F01","#FC5130"]


itts = uI("How many itterations deep do you want to go?",int)
i = 1
sides = uI("How many sides do you want your regular polygon to have?",int)
clear = uI("Do you want me to clear the screen after every itteration(makes intresting outline rather than orignal)",bool)
print clear
box = 400
div = 0
count = 1
while count*(360.0/sides)<180:
  div+=sin(radians(count*(360.0/sides)))
  count+=1
s = box/div



t = turtle.Turtle()
t.speed(999)
xl = [-s/2]
yl = [-box/2]
al = [0]
xh = []
yh = []
ah = []
div = 0
down = []
for x in range(1,sides-1):
  down.append(x)
t.pu()
c = len(colors)-1
def tri():
  t.pu()
  for x in range(sides):
    if clear:
      t.pd()
    else:
      if(i!=1):
        if(x in down):
          t.pd()
        else:
          t.pu()
      else:
        t.pd()
    xh.append(t.xcor())
    yh.append(t.ycor())
    ah.append(t.heading())
    t.forward(s)
    t.left(360.0/sides)
  t.pu()
  
    
    

while i!=itts:
  t.color(colors[c])
  while(len(xl)>0):
    t.setx(xl.pop(0))
    t.sety(yl.pop(0))
    t.seth(al.pop(0))
    tri()
  i+=1
  xl=xh
  yl=yh
  al=ah
  xh=[]
  yh=[]
  ah=[]
  if clear and i!=itts:
    t.clear()
  if sides==3:
    s/=2
  else:
    div = 1+cos(radians(360.0/sides))
    count= 2
    while (count*(360.0/sides))<90:
      div+=cos(radians(count*(360.0/sides)))
      #print div
      count +=1
    s = (s/2)/div
  #print s
  c-=1
raw_input("Press enter to end simulation")
  