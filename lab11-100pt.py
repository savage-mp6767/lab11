##########################################
#                                        #
#           100pt - Lab 11               # 
#                                        #
##########################################

# Make the ball "wrap" instead of bouncing - when it hits the right
# edge of the window, it should reappear at the left side and continue moving
# to the right. 

from Tkinter import *
import random
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)

colors = ["green","red","blue","purple","orange","yellow"]

# Create the oval
circle = drawpad.create_oval(10, 10, 50, 50, fill='green')
direction = 1
# Create our animation function
def seizure():
    drawpad.itemconfig(circle,fill=colors[random.randint(0,5)])
    drawpad.config(bg=colors[random.randint(0,5)])
    drawpad.after(150,seizure)

def animate():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    if x2 > drawpad.winfo_width() + 50: 
        drawpad.move(circle,-drawpad.winfo_width(),0)
    elif x1 < 0:
        direction = 1
    #Move our oval object by the value of direction
    drawpad.move(circle,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(1, animate)

# Kick off our animation
animate()
seizure()
root.mainloop()
