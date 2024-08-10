import math
from turtle import*
def heart1(x):
    return 15*math.sin(x)**3
def heart2(x):
    return 12*math.cos(x)-5*\
           math.cos(2*x)-2*\
           math.cos(3*x)-\
           math.cos(4*x)
speed(1000)
bgcolor("black")
for i in range(6000):
    goto(heart1(i)*20,heart2(i)*20)
    for k in range(5):
        color("#f73487")
    goto(0,0)
    
done()
   
