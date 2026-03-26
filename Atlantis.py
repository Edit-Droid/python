Atlantis
--------

clear_screen

Dimensions: The plotting area is 320 pixels wide by 220 pixels high, allowing space for soft menu keys.
Origin: The pixel coordinate 0,0 is the top-left corner.

draw_filled_polygon
draw_line

mouse
 Using the hpprime library, specifically hpprime.eval('mouse(1)') or hpprime.eval('mouse(2)'), you can detect touch coordinates (), types of touches, and clear pending inputs

import hpprime as h

  def mouseClear(): # Clear out old mouse events like button bounces.
    while h.eval('mouse(1)')>=0:
      pass

  def mousePt(): # Wait forever for a screen touch.
    while True:
      h.eval('wait(0.1)') # Throttle i/o loop.
      f1,f2 = h.eval('mouse') # Touch info for fingers 1 and 2.
      if len(f1) > 0: # Got a finger touch!
        return f1,f2 # [x,y,xOrig,yOrig,type], [x,y,xOrig,yOrig,type]

https://udel.edu/~mm/hp/primePython/#:~:text=2.3%20Screen%20Tap%20Events,my%20programs%20requiring%20mouse%20input%3A


Images

https://stackoverflow.com/questions/78863038/hp-prime-draw-image-with-python

You can store files (like images) inside applications on the HP Prime.
Using the command AFiles(filename) inside of an application script lets you access those files.
By using G1(or G2-G9) = AFiles(filename) and then P_BLITing the image you stored in G1 to G0, you will have the entire image instantly drawn for you.

 cyan
 magenta
 yellow
 black
 white
 red
 green
 blue 
