#PYTHON EXPORT pyhat
EXPORT MOUSE3()
from hpprime import *
from math import *
t0 = eval("ticks()") # Save the current clock count for timing program
# Clear screen
fillrect(0,0,0,320,240,0,0)
# Start program proper
p=160; q=120
xp=144; xr=1.5*3.1415927
yp=56; yr=1; zp=64
#EXPORT Mouse3()
BEGIN
  PYTHON(MOUSE3);
END;