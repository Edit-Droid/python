#PYTHON name
# 20190704 HP Prime
# micro python
# print string array
# Hello World
from graphic import *
from math import *
from urandom import *

clear_screen()

j=3
#a="Hello World"
#print (j)
#print (a)

e=[red,yellow,blue,green,black,cyan,magenta]

for j in range(100):
  #x=a[j]
  #print (x)
  c=randint(1,350)
  d=randint(1,250)
  f=randint(10,50)
#  e=randrange('blue','red')
  draw_filled_circle(c,d,f,choice(e))
  draw_filled_circle(c,d,f,choice(e))
#end

EXPORT test0004()
BEGIN
  PYTHON(name);
END;