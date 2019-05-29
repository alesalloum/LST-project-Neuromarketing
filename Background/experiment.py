#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Neuromarketing experiment code
Juho Aaltonen & Leifu Chen
"""

from __future__ import absolute_import, division, print_function
import pandas as pd

# Import key parts of the PsychoPy library:
from psychopy import visual, core, event#, parallel


# VARIABLES ARE HERE

# Research ID:
ID = 928376
# ID = 382733
# ID = 990291
# ID = 884723
# ID = 554432
# ID = 477819

file_en = str(ID) + '_test1.csv'
file_fin = str(ID) + '_test2.csv'
print(file_en)

# Experiment
english = True # Change to False in Finnish part

stim = 1.5            # length of one stimulus in seconds
pause = 2             # length of the pause between stimuli
long_pause = 60


# ACTUAL CODE BEGINS

# Define the shutdown function
def shutdown():
    win.close()
    core.quit()

# Define the key listener
def get_keypress():
    keys = event.getKeys()
    if keys:
        event.clearEvents()
        return keys[0]
    else:
        return None

def pause_screen():
    control.setAutoDraw(False) 
    exit.setAutoDraw(False)
    cont.setAutoDraw(True)
    win.flip()

def continue_screen():
    # continue the presentation
    exit.setAutoDraw(True)
    cont.setAutoDraw(False)
    control.setAutoDraw(True) 
    win.flip()

def exit_or_pause(key):
    # check if the ESC was pressed
    if key and key == 'q':
        print(key)
        shutdown()
    # check if the p was pressed
    elif key and key == 'p':
        print(key)
        pause_screen()
        event.waitKeys()


def pause_function(long_pause):
    for p in range(long_pause):
        # default position = centered
        msg = visual.TextStim(win, text='Take a break. Seconds left: %i' % (
            long_pause-p), pos=(0, 0), height=0.2, wrapWidth=1000)
            
        # Draw the text to the hidden visual buffer:
        msg.draw()
        win.flip()
        
        # key listener for exit or pause
        key = event.waitKeys(1)
        # check if the ESC was pressed
        if key and key[0] == 'q':
            print(key)
            shutdown()
        # check if the p was pressed
        elif key and key[0] == 'p':
            print(key)
            pause_screen()
            event.waitKeys()
        event.clearEvents()


# Define the port
#port = parallel.ParallelPort(address=0x00378)

# color
x = -0.25

# Create a visual window:
win = visual.Window([1200, 600], color=(x, x, x), pos=(0, 5))

# Read correct stimuli 
if english == True:
    df = pd.read_csv(file_en)
else:
    df = pd.read_csv(file_fin)

key = "r"
# Press s to begin
while key != "s":
    key = event.waitKeys()[0]
    msg = visual.TextStim(win, text='+', pos=(
            0, 0), height=0.2, wrapWidth=1000, color = (1,0,0))  # default position = centered
    msg.draw()
    win.flip()
    exit_or_pause(get_keypress())
    core.wait(0.5)



# Iterate the word list
for i in range(6):
    # Tell the subject to focus on the screen again
    win.flip()
    core.wait(5)
    for j in range(3):
        # key listener for exit or pause
        exit_or_pause(get_keypress())
        
        k = j + 20 * i
        stimuli = df['stimuli'][k]
        stimuli_no = int(df['no'][k])
        # Create (but not yet display) some text:
        msg = visual.TextStim(win, text=stimuli, pos=(
            0, 0), height=0.2, wrapWidth=1000)  # default position = centered

        # Draw the text to the hidden visual buffer:     
        msg.draw()

        # Send data
        #port.setData(stimuli_no)

        # Show the hidden buffer--everything that has been drawn since the last win.flip():
        win.flip()
        # Wait 2 seconds so people can see the message, then exit gracefully:
        core.wait(stim)
        win.flip()
        core.wait(pause)
    
    if i != 5:
        win.color = [0, 0, 1]
        win.flip()
        pause_function(long_pause)
        win.color = [x, x, x]
        win.flip()
        core.wait(2)
# exit the experiments
shutdown()
