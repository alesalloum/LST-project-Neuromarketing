#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Neuromarketing - keyboard record
Leifu Chen
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

# Number of responses:
responses = 120


file_en = str(ID) + '_test1.csv'
file_fin = str(ID) + '_test2.csv'

file_key = str(ID) + '_keyboard.csv'


# Read csv to dataframe and combine EN and FIN dataframes
df1 = pd.read_csv(file_en)
df2 = pd.read_csv(file_fin)
df = pd.concat([df1,df2],ignore_index=True)

# Randomize the order
df= df.sample(frac=1).reset_index(drop=True)


# Define the shutdown function
def shutdown():
    dataFile.close()
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
    
        
# Define the port
#port = parallel.ParallelPort(address=0x00378)

# color
x = -0.25

# Create a visual window:
win = visual.Window([1200, 600], color=(x, x, x), pos=(0, 5))


stim = 0.01            # length of one stimulus in seconds
pause = 0.01             # length of the pause between stimuli
long_pause = 5

# Keyboard instruction
control = visual.TextStim(win, text='Press z (agree), x (disagree) or c (no opinion) to continue', pos=(
    0, -0.5), height=0.08, wrapWidth=1000) 
exit = visual.TextStim(win, text='Press q to exit the program and p to pause the presentation', pos=(0, -0.65), height=0.08, wrapWidth=1000) 
cont = visual.TextStim(win, text='Press any key to continue...', pos=(0, -0.65), height=0.08, wrapWidth=1000) 
ready = visual.TextStim(win, text='Let\'s get started!', pos=(0, 0), height=0.2, wrapWidth=1000)
start = visual.TextStim(win, text='\nPress g to continue...', pos=(-0, -0.5), height=0.08, wrapWidth=1000)

exit.setAutoDraw(True)


# Part II, presentaiton with keyboard
# open data file to store record
dataFile = open(file_key, 'w')  # a simple text file with 'comma-separated-values'
dataFile.write('no, stimuli, opinion\n')

# Tell the subject to focus on the screen again
win.color = [x, x, x]

# Draw the text to the hidden visual buffer:
ready.draw()
start.draw()

win.flip()
while True:
    key = event.waitKeys()[0]
    if key == "q":
        shutdown()
    elif key == "g":
        break

control.setAutoDraw(True)     
for j in range(responses):
    # key listener for exit or pause
    exit_or_pause(get_keypress())
    
    # continue the presentation
    continue_screen()
    
    stimuli = df['stimuli'][j]
    stimuli_no = int(df['no'][j])
    # Create (but not yet display) some text:
    msg = visual.TextStim(win, text=stimuli, pos=(
        0, 0), height=0.2, wrapWidth=1000)  # default position = centered

    # Draw the text to the hidden visual buffer:     
    msg.draw()

    # Send data
#    port.setData(stimuli_no)

    # Show the hidden buffer--everything that has been drawn since the last win.flip():
    win.flip()
    
    # Wait for subject to response the stimuli:
    opinion = "undefined"       
    while (opinion == 'undefined'):
        allKeys = event.waitKeys()[0]
        for thisKey in allKeys:
            if thisKey == 'z':
                opinion = 'agree'
            elif thisKey == 'x':
                opinion = 'disagree'
            elif thisKey == 'c':
                opinion = 'neutral'
            elif thisKey == 'q':
                shutdown()
            elif thisKey == 'p':
                pause_screen()
                event.waitKeys()
            
            msg.draw()    
            # continue the presentation
            continue_screen()
            win.flip()

        event.clearEvents()
          
    # Record the response
    dataFile.write('%i, %s, %s\n' %(stimuli_no, stimuli, opinion))

       
        
# exit the experiments
shutdown()
