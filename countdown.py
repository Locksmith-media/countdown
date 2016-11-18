#!/usr/bin/python3

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
from time import sleep
import os
import sys

from subprocess import Popen

x = 1

def count_down():
    # start with 2 minutes --> 120 seconds
    for t in range(10, -1, -1):
        # format as 2 digit integers, fills with zero to the left
        # divmod() gives minutes, seconds
        sf = "{:02d}:{:02d}".format(*divmod(t, 60))
        #print(sf)  # test
        time_str.set(sf)
        root.update()
        # delay one second
        sleep(x)
        if t == 0:
            print("Yeah!")
 #          omxc = Popen(['omxplayer', '-b', movie1])
#           player = True

def count_stop():
    print("sop!")
    root.destroy
#    omxc = Popen(['omxplayer', '-b', movie2)
    

# now this is the movie part

movie1=("/home/pi/Videos/GAMEOVER.mov")
movie2=("/home/pi/Videos/CONGRATULATIONS.mov")
        
# create root/main window
root = tk.Tk()
time_str = tk.StringVar()
root.configure(background='black')
root.attributes("-fullscreen", True)
root.title = "LOCKSMITH"
root.bind('<Return>', count_down)

# create the time display label, give it a large font
# label auto-adjusts to the font
label_font = ('helvetica', 200)
tk.Label(root, textvariable=time_str, font=label_font, bg='black', 
         fg='white', relief='raised', bd=0).pack(fill='x', padx=5, pady=200)
# create start and stop buttons
# pack() positions the buttons below the label
tk.Button(root, text='Start', command=count_down).pack()
# stop simply exits root window
tk.Button(root, text='Stop', command=count_stop).pack()
# start the GUI event loop
root.mainloop()
