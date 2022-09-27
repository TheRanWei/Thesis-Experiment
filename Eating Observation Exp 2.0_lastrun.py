#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on November 10, 2021, at 17:49
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\ranwei\\Desktop\\Eating Observation Exp 2.0\\Eating Observation Exp 2.0_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction__screen"
Instruction__screenClock = core.Clock()
backGroud1 = visual.Rect(
    win=win, name='backGroud1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
#resources
#word
food = ["cake","sugar","doughnut","hamburger","chips","caramel","crisps","kebab","pizza","cream"]

neutral = ["desk","ruler","scissors","envelops","files","monitor","blinds","memos","table","books"]

all_list=[[['cake'], ['red', 'green', 'deepskyblue', 'gold']],
[['sugar'], ['red', 'green', 'deepskyblue', 'gold']],
[['doughnut'], ['red', 'green', 'deepskyblue', 'gold']],
[['hamburger'], ['red', 'green', 'deepskyblue', 'gold']],
[['chips'], ['red', 'green', 'deepskyblue', 'gold']],
[['caramel'], ['red', 'green', 'deepskyblue', 'gold']],
[['crisps'], ['red', 'green', 'deepskyblue', 'gold']],
[['kebab'], ['red', 'green', 'deepskyblue', 'gold']],
[['pizza'], ['red', 'green', 'deepskyblue', 'gold']],
[['cream'], ['red', 'green', 'deepskyblue', 'gold']],
[['desk'], ['red', 'green', 'deepskyblue', 'gold']],
[['ruler'], ['red', 'green', 'deepskyblue', 'gold']],
[['scissors'], ['red', 'green', 'deepskyblue', 'gold']],
[['envelops'], ['red', 'green', 'deepskyblue', 'gold']],
[['files'], ['red', 'green', 'deepskyblue', 'gold']],
[['monitor'], ['red', 'green', 'deepskyblue', 'gold']],
[['blinds'], ['red', 'green', 'deepskyblue', 'gold']],
[['memos'], ['red', 'green', 'deepskyblue', 'gold']],
[['table'], ['red', 'green', 'deepskyblue', 'gold']],
[['books'], ['red', 'green', 'deepskyblue', 'gold']]]

color = ["red","deepskyblue", "green", "gold" ]

nTrial1=80

#video
videoA = ["resources/ECE_01.mp4", "resources/ECE_02.mp4", "resources/ECE_03.mp4", "resources/ECE_05.mp4", "resources/ECE_06.mp4", 
"resources/ECE_07.mp4", "resources/ECE_08.mp4", "resources/ECE_10.mp4", "resources/ECE_11.mp4", "resources/ECE_12.mp4", 
"resources/ECE_13.mp4", "resources/ECE_14.mp4", "resources/ECE_15.mp4", "resources/HCE_01.mp4", "resources/HCE_02.mp4", 
"resources/HCE_03.mp4", "resources/HCE_04.mp4", "resources/HCE_05.mp4", "resources/HCE_06.mp4", "resources/HCE_07.mp4", 
"resources/HCE_10.mp4", "resources/HCE_11.mp4", "resources/HCE_12.mp4", "resources/HCE_13.mp4", "resources/HCE_14.mp4", 
"resources/HCE_15.mp4", "resources/KCE_02.mp4", "resources/KCE_03.mp4", "resources/KCE_04.mp4", "resources/KCE_05.mp4", 
"resources/KCE_06.mp4", "resources/KCE_07.mp4", "resources/KCE_08.mp4", "resources/KCE_09.mp4", "resources/KCE_10.mp4", 
"resources/KCE_11.mp4", "resources/KCE_12.mp4", "resources/KCE_13.mp4", "resources/KCE_14.mp4", "resources/KCE_15.mp4"];

videoB = ["resources/ECC_01.mp4", "resources/ECC_02.mp4", "resources/ECC_03.mp4", "resources/ECC_04.mp4", "resources/ECC_05.mp4", 
"resources/ECC_06.mp4", "resources/ECC_07.mp4", "resources/ECC_08.mp4", "resources/ECC_09.mp4", "resources/ECC_10.mp4", 
"resources/ECC_12.mp4", "resources/ECC_13.mp4", "resources/ECC_14.mp4", "resources/ECC_15.mp4", "resources/HCC_01.mp4", 
"resources/HCC_02.mp4", "resources/HCC_03.mp4", "resources/HCC_04.mp4", "resources/HCC_05.mp4", "resources/HCC_06.mp4", 
"resources/HCC_07.mp4", "resources/HCC_08.mp4", "resources/HCC_09.mp4", "resources/HCC_10.mp4", "resources/HCC_12.mp4", 
"resources/HCC_13.mp4", "resources/HCC_14.mp4", "resources/KCC_01.mp4", "resources/KCC_02.mp4", "resources/KCC_03.mp4", 
"resources/KCC_04.mp4", "resources/KCC_05.mp4", "resources/KCC_06.mp4", "resources/KCC_07.mp4", "resources/KCC_08.mp4", 
"resources/KCC_10.mp4", "resources/KCC_11.mp4", "resources/KCC_13.mp4", "resources/KCC_14.mp4", "resources/KCC_15.mp4",];

videoC = ["resources/EBC_01.mp4", "resources/EBC_02.mp4", "resources/EBC_03.mp4", "resources/EBC_04.mp4", "resources/EBC_05.mp4", 
"resources/EBC_06.mp4", "resources/EBC_07.mp4", "resources/EBC_08.mp4", "resources/EBC_09.mp4", "resources/EBC_12.mp4", 
"resources/EBC_13.mp4", "resources/EBC_14.mp4", "resources/EBC_15.mp4", "resources/HBC_01.mp4", "resources/HBC_02.mp4", 
"resources/HBC_03.mp4", "resources/HBC_04.mp4", "resources/HBC_05.mp4", "resources/HBC_08.mp4", "resources/HBC_09.mp4", 
"resources/HBC_10.mp4", "resources/HBC_11.mp4", "resources/HBC_12.mp4", "resources/HBC_13.mp4", "resources/HBC_14.mp4", 
"resources/HBC_15.mp4", "resources/KBC_02.mp4", "resources/KBC_03.mp4", "resources/KBC_04.mp4", "resources/KBC_05.mp4", 
"resources/KBC_06.mp4", "resources/KBC_07.mp4", "resources/KBC_08.mp4", "resources/KBC_09.mp4", "resources/KBC_10.mp4", 
"resources/KBC_11.mp4", "resources/KBC_12.mp4", "resources/KBC_13.mp4", "resources/KBC_14.mp4", "resources/KBC_15.mp4"];

import random
random.seed

random.shuffle(videoA)
random.shuffle(videoB)
random.shuffle(videoC)

#extract number from list
def lst_to_num(col_index):
    for num in col_index:
        return num

def create_word_lst(word_color_lst):
    word_lst=[]
    for i in range(len(word_color_lst)):
        word_lst.append(word_color_lst[i][0][0])
    return word_lst

def create_color_lst(word_color_lst):
    color_lst=[]
    for wordIndex in range(len(word_color_lst)):
        #choose a random color
        colorIndex=(random.choices(range(len(word_color_lst[wordIndex][1]))))#randomly choose from 1:len(color)
        color=word_color_lst[wordIndex][1].pop(lst_to_num(colorIndex))#Store the color and remove the selected color from future color pool
        color_lst.append(color)
    return color_lst

def create_condition_wd_clr_lst(lst1):
    random.shuffle(lst1)
    #Create 1st wordlist and color_lst in eo condition
    word_lst1=create_word_lst(lst1)
    color_lst1=create_color_lst(lst1)

    #shuffle the word_color_lst
    lst2=lst1.copy()
    random.shuffle(lst2)

    #Create 2nd wordlist and color_lst in eo condition
    word_lst2=create_word_lst(lst2)
    color_lst2=create_color_lst(lst2)

    word_lst=word_lst1+word_lst2
    color_lst=color_lst1+color_lst2
    
    return (word_lst, color_lst)

#resources for conditions
eo_wd_clr_lst1=[[['cake'], ['red', 'green', 'deepskyblue', 'gold']],
[['sugar'], ['red', 'green', 'deepskyblue', 'gold']],
[['doughnut'], ['red', 'green', 'deepskyblue', 'gold']],
[['hamburger'], ['red', 'green', 'deepskyblue', 'gold']],
[['chips'], ['red', 'green', 'deepskyblue', 'gold']],
[['caramel'], ['red', 'green', 'deepskyblue', 'gold']],
[['crisps'], ['red', 'green', 'deepskyblue', 'gold']],
[['kebab'], ['red', 'green', 'deepskyblue', 'gold']],
[['pizza'], ['red', 'green', 'deepskyblue', 'gold']],
[['cream'], ['red', 'green', 'deepskyblue', 'gold']],
[['desk'], ['red', 'green', 'deepskyblue', 'gold']],
[['ruler'], ['red', 'green', 'deepskyblue', 'gold']],
[['scissors'], ['red', 'green', 'deepskyblue', 'gold']],
[['envelops'], ['red', 'green', 'deepskyblue', 'gold']],
[['files'], ['red', 'green', 'deepskyblue', 'gold']],
[['monitor'], ['red', 'green', 'deepskyblue', 'gold']],
[['blinds'], ['red', 'green', 'deepskyblue', 'gold']],
[['memos'], ['red', 'green', 'deepskyblue', 'gold']],
[['table'], ['red', 'green', 'deepskyblue', 'gold']],
[['books'], ['red', 'green', 'deepskyblue', 'gold']]]


fo_wd_clr_lst1=[[['cake'], ['red', 'green', 'deepskyblue', 'gold']],
[['sugar'], ['red', 'green', 'deepskyblue', 'gold']],
[['doughnut'], ['red', 'green', 'deepskyblue', 'gold']],
[['hamburger'], ['red', 'green', 'deepskyblue', 'gold']],
[['chips'], ['red', 'green', 'deepskyblue', 'gold']],
[['caramel'], ['red', 'green', 'deepskyblue', 'gold']],
[['crisps'], ['red', 'green', 'deepskyblue', 'gold']],
[['kebab'], ['red', 'green', 'deepskyblue', 'gold']],
[['pizza'], ['red', 'green', 'deepskyblue', 'gold']],
[['cream'], ['red', 'green', 'deepskyblue', 'gold']],
[['desk'], ['red', 'green', 'deepskyblue', 'gold']],
[['ruler'], ['red', 'green', 'deepskyblue', 'gold']],
[['scissors'], ['red', 'green', 'deepskyblue', 'gold']],
[['envelops'], ['red', 'green', 'deepskyblue', 'gold']],
[['files'], ['red', 'green', 'deepskyblue', 'gold']],
[['monitor'], ['red', 'green', 'deepskyblue', 'gold']],
[['blinds'], ['red', 'green', 'deepskyblue', 'gold']],
[['memos'], ['red', 'green', 'deepskyblue', 'gold']],
[['table'], ['red', 'green', 'deepskyblue', 'gold']],
[['books'], ['red', 'green', 'deepskyblue', 'gold']]]


nf_wd_clr_lst1=[[['cake'], ['red', 'green', 'deepskyblue', 'gold']],
[['sugar'], ['red', 'green', 'deepskyblue', 'gold']],
[['doughnut'], ['red', 'green', 'deepskyblue', 'gold']],
[['hamburger'], ['red', 'green', 'deepskyblue', 'gold']],
[['chips'], ['red', 'green', 'deepskyblue', 'gold']],
[['caramel'], ['red', 'green', 'deepskyblue', 'gold']],
[['crisps'], ['red', 'green', 'deepskyblue', 'gold']],
[['kebab'], ['red', 'green', 'deepskyblue', 'gold']],
[['pizza'], ['red', 'green', 'deepskyblue', 'gold']],
[['cream'], ['red', 'green', 'deepskyblue', 'gold']],
[['desk'], ['red', 'green', 'deepskyblue', 'gold']],
[['ruler'], ['red', 'green', 'deepskyblue', 'gold']],
[['scissors'], ['red', 'green', 'deepskyblue', 'gold']],
[['envelops'], ['red', 'green', 'deepskyblue', 'gold']],
[['files'], ['red', 'green', 'deepskyblue', 'gold']],
[['monitor'], ['red', 'green', 'deepskyblue', 'gold']],
[['blinds'], ['red', 'green', 'deepskyblue', 'gold']],
[['memos'], ['red', 'green', 'deepskyblue', 'gold']],
[['table'], ['red', 'green', 'deepskyblue', 'gold']],
[['books'], ['red', 'green', 'deepskyblue', 'gold']]]


random.shuffle(eo_wd_clr_lst1)
random.shuffle(fo_wd_clr_lst1)
random.shuffle(nf_wd_clr_lst1)

#Randomize order for all conditions

word_color_lst1=all_list
random.shuffle(word_color_lst1)

#Generate the first word list
word_lst1=create_word_lst(word_color_lst1)
#generate the first color list
color_lst1=create_color_lst(word_color_lst1)
word_color_lst2=word_color_lst1
random.shuffle(word_color_lst2)

#Generate the second wordlist & colorlist
word_lst2=create_word_lst(word_color_lst2)
color_lst2=create_color_lst(word_color_lst2)

#Randomize the list
word_color_lst3=word_color_lst2
random.shuffle(word_color_lst3)

#generate the 3rd word and color lst
word_lst3=create_word_lst(word_color_lst3)
color_lst3=create_color_lst(word_color_lst3)

#Randomize the list
word_color_lst4=word_color_lst3
random.shuffle(word_color_lst4)

#generate the 4th word and color lst
word_lst4=create_word_lst(word_color_lst4)
color_lst4=create_color_lst(word_color_lst4)

#word_color_lst4

all_word_lst=word_lst1+word_lst2+word_lst3+word_lst4
all_color_lst=color_lst1+color_lst2+color_lst3+color_lst4

word_color_lst_all=[[]]*nTrial1

for i in range(nTrial1):
    word_color_lst_all[i]=[all_word_lst[i], all_color_lst[i]]

#print(word_color_lst_all)#for debug

#For each condition
eo_word_lst, eo_color_lst=create_condition_wd_clr_lst(eo_wd_clr_lst1)
fo_word_lst, fo_color_lst=create_condition_wd_clr_lst(fo_wd_clr_lst1)
nf_word_lst, nf_color_lst=create_condition_wd_clr_lst(nf_wd_clr_lst1)
Instruction = visual.TextStim(win=win, name='Instruction',
    text="There are two sections in this part of the experiment:\n\nIn the first section, you will complete some color-naming tasks, in which you will name the color of the word presented in the center of the screen by pressing corresponding keyboard keys :\n\nPress 'd' for red; \nPress 'f' for green,\nPress 'j' for blue,\nPress 'k' fpr black\n\nIn the second section, you will watch some short video clips. After each video clip, you will complete a color-naming task, which will be similar to what you will do in the first section(Press 'd' for red; press 'f' for green, press 'j' for blue, press 'k' for black).\n\nTo familiarize you with the task, there will be 15 practice trials for the color-naming task at the begining of this section. No video clips will be included in practice trials.\n\nPress the 'right arrow' key if you are ready to proceed.",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
begin_exp = keyboard.Keyboard()

# Initialize components for Routine "vasInstruction"
vasInstructionClock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
vasIns = visual.TextStim(win=win, name='vasIns',
    text="For the following five questions, please indicate your feelings by marking on the continuum with your mouse.\n\nPress the 'right arrow' key to proceed.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
proceed_VAS = keyboard.Keyboard()

# Initialize components for Routine "VAS"
VASClock = core.Clock()
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
VAStext1 = visual.TextStim(win=win, name='VAStext1',
    text='How much food do you think you could eat?',
    font='Open Sans',
    pos=(0, 0.4), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
VAS1 = visual.Slider(win=win, name='VAS1',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.34), units=None,
    labels=('No food at all', 'A large amount of food'), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-2, readOnly=False)
VAStext2 = visual.TextStim(win=win, name='VAStext2',
    text='How strong is your desire to eat?',
    font='Open Sans',
    pos=(0, 0.25), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
VAS2 = visual.Slider(win=win, name='VAS2',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.19), units=None,
    labels=('Very weak','Very strong'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-4, readOnly=False)
VAStext3 = visual.TextStim(win=win, name='VAStext3',
    text='How hungry do you feel?',
    font='Open Sans',
    pos=(0, 0.1), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
VAS3 = visual.Slider(win=win, name='VAS3',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.04), units=None,
    labels=('Not at all','As hungery as I have ever felt'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-6, readOnly=False)
VAStext4 = visual.TextStim(win=win, name='VAStext4',
    text='What is your level of satiety?',
    font='Open Sans',
    pos=(0, -0.05), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
VAS4 = visual.Slider(win=win, name='VAS4',
    startValue=None, size=(1.0, 0.025), pos=(0, -0.11), units=None,
    labels=('Not satiated at all','Very high'), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-8, readOnly=False)
VAStext5 = visual.TextStim(win=win, name='VAStext5',
    text='How full do you feel?',
    font='Open Sans',
    pos=(0, -0.2), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
VAS5 = visual.Slider(win=win, name='VAS5',
    startValue=None, size=(1.0, 0.025), pos=(0, -0.26), units=None,
    labels=('Not at all full','Very full'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-10, readOnly=False)
proceed = visual.TextStim(win=win, name='proceed',
    text="Press the 'right arrow' key to proceed. Your answer on this page cannot be changed after you move on to next section.",
    font='Open Sans',
    pos=(0, -0.4), height=0.026, wrapWidth=1.8, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "practice_ins"
practice_insClock = core.Clock()
backgroud2 = visual.Rect(
    win=win, name='backgroud2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
prac_inst = visual.TextStim(win=win, name='prac_inst',
    text="You will first complete 15 practice Trail.\n\nPlease determine the color of the word presented in the center of the screen by pressing corresponding keyboard keys :\n\nPress 'd' for red; \nPress 'f' for green,\nPress 'j' for blue,\nPress 'k' fpr black\n\nPress 'right arrow' key to proceed to practice trials.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practiceTrial_key = keyboard.Keyboard()

# Initialize components for Routine "PracticeTrials"
PracticeTrialsClock = core.Clock()
background3 = visual.Rect(
    win=win, name='background3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
practiceFixation = visual.TextStim(win=win, name='practiceFixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practice_word = visual.TextStim(win=win, name='practice_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
practice_key = keyboard.Keyboard()

# Initialize components for Routine "BeginBaseline"
BeginBaselineClock = core.Clock()
background4 = visual.Rect(
    win=win, name='background4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
beginexp = visual.TextStim(win=win, name='beginexp',
    text="Now you have completed the practice trials and can proceed to experimental trials.\n\nIn the following section, you will complete some color-naming tasks, in which you will name the color of the word presented in the center of the screen by pressing corresponding keyboard keys :\n\nPress 'd' for red; \nPress 'f' for green,\nPress 'j' for blue,\nPress 'k' fpr black\n\nPress 'right arrow' to proceed to section 1",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
begin_key = keyboard.Keyboard()

# Initialize components for Routine "Baseline_code"
Baseline_codeClock = core.Clock()
baseline_trial=0

# Initialize components for Routine "Baseline_Stroop"
Baseline_StroopClock = core.Clock()
background5 = visual.Rect(
    win=win, name='background5',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
baseline_stroop_word = visual.TextStim(win=win, name='baseline_stroop_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
baseline_fixation = visual.TextStim(win=win, name='baseline_fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "vasInstruction"
vasInstructionClock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
vasIns = visual.TextStim(win=win, name='vasIns',
    text="For the following five questions, please indicate your feelings by marking on the continuum with your mouse.\n\nPress the 'right arrow' key to proceed.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
proceed_VAS = keyboard.Keyboard()

# Initialize components for Routine "VAS"
VASClock = core.Clock()
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
VAStext1 = visual.TextStim(win=win, name='VAStext1',
    text='How much food do you think you could eat?',
    font='Open Sans',
    pos=(0, 0.4), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
VAS1 = visual.Slider(win=win, name='VAS1',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.34), units=None,
    labels=('No food at all', 'A large amount of food'), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-2, readOnly=False)
VAStext2 = visual.TextStim(win=win, name='VAStext2',
    text='How strong is your desire to eat?',
    font='Open Sans',
    pos=(0, 0.25), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
VAS2 = visual.Slider(win=win, name='VAS2',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.19), units=None,
    labels=('Very weak','Very strong'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-4, readOnly=False)
VAStext3 = visual.TextStim(win=win, name='VAStext3',
    text='How hungry do you feel?',
    font='Open Sans',
    pos=(0, 0.1), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
VAS3 = visual.Slider(win=win, name='VAS3',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.04), units=None,
    labels=('Not at all','As hungery as I have ever felt'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-6, readOnly=False)
VAStext4 = visual.TextStim(win=win, name='VAStext4',
    text='What is your level of satiety?',
    font='Open Sans',
    pos=(0, -0.05), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
VAS4 = visual.Slider(win=win, name='VAS4',
    startValue=None, size=(1.0, 0.025), pos=(0, -0.11), units=None,
    labels=('Not satiated at all','Very high'), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-8, readOnly=False)
VAStext5 = visual.TextStim(win=win, name='VAStext5',
    text='How full do you feel?',
    font='Open Sans',
    pos=(0, -0.2), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
VAS5 = visual.Slider(win=win, name='VAS5',
    startValue=None, size=(1.0, 0.025), pos=(0, -0.26), units=None,
    labels=('Not at all full','Very full'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-10, readOnly=False)
proceed = visual.TextStim(win=win, name='proceed',
    text="Press the 'right arrow' key to proceed. Your answer on this page cannot be changed after you move on to next section.",
    font='Open Sans',
    pos=(0, -0.4), height=0.026, wrapWidth=1.8, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Begin_Video_obs_task"
Begin_Video_obs_taskClock = core.Clock()
background6 = visual.Rect(
    win=win, name='background6',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
begin_video_obs = visual.TextStim(win=win, name='begin_video_obs',
    text="In the following section, you will watch some short video clips. After each video clip, you will complete a color-naming task, which will be similar to what you will do in previous section.\n\nFor the color naming task after each video clip:\nPress 'd' for red;\nPress 'f' for green;\nPress 'j' for blue;\nPress 'k' for black.\n\nPress the 'right arrow' key to proceed.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
proceed_to_conditions = keyboard.Keyboard()

# Initialize components for Routine "Counter_balance_code"
Counter_balance_codeClock = core.Clock()
#order of the conditions. Latin square counterbalance 
order_lst=[[1,2,3],[3,1,2],[2,3,1]]
#whether a condition appears
eo_presence=[[1,0,0],[0,1,0], [0,0,1]]
fo_presence=[[0,1,0],[0,0,1], [1,0,0]]
nf_presence=[[0,0,1],[1,0,0], [0,1,0]]

#choose which order to use
#{0:[eo,fo,nf],1:[nf,eo,fo],2:[fo,nf,eo]}
cdt_order=random.choice([0,1,2])
thisExp.addData('cdt_order', cdt_order)

#Initialize the amount of condition that has been shown
cdt_num=0

#Trial number for each condition
nTrial=40

# Initialize components for Routine "EO_CODE"
EO_CODEClock = core.Clock()
#Initiate trial number
eo_trial=0

#for debug
print(eo_word_lst)
print(eo_color_lst)

# Initialize components for Routine "preloadVideo"
preloadVideoClock = core.Clock()
PreloadBackground = visual.Rect(
    win=win, name='PreloadBackground',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "EO_Condition"
EO_ConditionClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
eo_Stroop_word = visual.TextStim(win=win, name='eo_Stroop_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eo_fixation_cross = visual.TextStim(win=win, name='eo_fixation_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "FO_CODE"
FO_CODEClock = core.Clock()
fo_trial=0

#Debug purpose
print(fo_word_lst)
print(fo_color_lst)

# Initialize components for Routine "preloadVideo"
preloadVideoClock = core.Clock()
PreloadBackground = visual.Rect(
    win=win, name='PreloadBackground',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FO_Condition"
FO_ConditionClock = core.Clock()
background7 = visual.Rect(
    win=win, name='background7',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
fo_fixation_cross = visual.TextStim(win=win, name='fo_fixation_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fo_word = visual.TextStim(win=win, name='fo_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "NF_CODE"
NF_CODEClock = core.Clock()
nf_trial=0

#Debug
print(nf_word_lst)
print(nf_color_lst)

# Initialize components for Routine "preloadVideo"
preloadVideoClock = core.Clock()
PreloadBackground = visual.Rect(
    win=win, name='PreloadBackground',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "NF_Condition"
NF_ConditionClock = core.Clock()
background8 = visual.Rect(
    win=win, name='background8',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
nf_fixation_cross = visual.TextStim(win=win, name='nf_fixation_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
nf_word = visual.TextStim(win=win, name='nf_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "cdt_num_plus_one"
cdt_num_plus_oneClock = core.Clock()

# Initialize components for Routine "BreakCode"
BreakCodeClock = core.Clock()

# Initialize components for Routine "vasInstruction"
vasInstructionClock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
vasIns = visual.TextStim(win=win, name='vasIns',
    text="For the following five questions, please indicate your feelings by marking on the continuum with your mouse.\n\nPress the 'right arrow' key to proceed.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
proceed_VAS = keyboard.Keyboard()

# Initialize components for Routine "VAS"
VASClock = core.Clock()
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
VAStext1 = visual.TextStim(win=win, name='VAStext1',
    text='How much food do you think you could eat?',
    font='Open Sans',
    pos=(0, 0.4), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
VAS1 = visual.Slider(win=win, name='VAS1',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.34), units=None,
    labels=('No food at all', 'A large amount of food'), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-2, readOnly=False)
VAStext2 = visual.TextStim(win=win, name='VAStext2',
    text='How strong is your desire to eat?',
    font='Open Sans',
    pos=(0, 0.25), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
VAS2 = visual.Slider(win=win, name='VAS2',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.19), units=None,
    labels=('Very weak','Very strong'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-4, readOnly=False)
VAStext3 = visual.TextStim(win=win, name='VAStext3',
    text='How hungry do you feel?',
    font='Open Sans',
    pos=(0, 0.1), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
VAS3 = visual.Slider(win=win, name='VAS3',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.04), units=None,
    labels=('Not at all','As hungery as I have ever felt'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-6, readOnly=False)
VAStext4 = visual.TextStim(win=win, name='VAStext4',
    text='What is your level of satiety?',
    font='Open Sans',
    pos=(0, -0.05), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
VAS4 = visual.Slider(win=win, name='VAS4',
    startValue=None, size=(1.0, 0.025), pos=(0, -0.11), units=None,
    labels=('Not satiated at all','Very high'), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-8, readOnly=False)
VAStext5 = visual.TextStim(win=win, name='VAStext5',
    text='How full do you feel?',
    font='Open Sans',
    pos=(0, -0.2), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
VAS5 = visual.Slider(win=win, name='VAS5',
    startValue=None, size=(1.0, 0.025), pos=(0, -0.26), units=None,
    labels=('Not at all full','Very full'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-10, readOnly=False)
proceed = visual.TextStim(win=win, name='proceed',
    text="Press the 'right arrow' key to proceed. Your answer on this page cannot be changed after you move on to next section.",
    font='Open Sans',
    pos=(0, -0.4), height=0.026, wrapWidth=1.8, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Break"
BreakClock = core.Clock()
background9 = visual.Rect(
    win=win, name='background9',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
Break_text = visual.TextStim(win=win, name='Break_text',
    text="Now, you can take a break for up to 10 minutes. The experiment will proceed after 10 minutes, but you can end the break early by pressing 'right arrow' key.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_break = keyboard.Keyboard()

# Initialize components for Routine "Remainder"
RemainderClock = core.Clock()
background10 = visual.Rect(
    win=win, name='background10',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
stroop_remainder = visual.TextStim(win=win, name='stroop_remainder',
    text="Please determine the color of the word presented in the center of the screen after the video by pressing corresponding keyboard keys:\n\nPress 'd' for red,\nPress 'f' for green,\nPress 'j' for blue,\nPress 'k' fpr black\n\nPress the 'right arrow' key to proceed.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
proceed_to_next_condition = keyboard.Keyboard()

# Initialize components for Routine "vasInstruction"
vasInstructionClock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
vasIns = visual.TextStim(win=win, name='vasIns',
    text="For the following five questions, please indicate your feelings by marking on the continuum with your mouse.\n\nPress the 'right arrow' key to proceed.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
proceed_VAS = keyboard.Keyboard()

# Initialize components for Routine "VAS"
VASClock = core.Clock()
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
VAStext1 = visual.TextStim(win=win, name='VAStext1',
    text='How much food do you think you could eat?',
    font='Open Sans',
    pos=(0, 0.4), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
VAS1 = visual.Slider(win=win, name='VAS1',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.34), units=None,
    labels=('No food at all', 'A large amount of food'), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-2, readOnly=False)
VAStext2 = visual.TextStim(win=win, name='VAStext2',
    text='How strong is your desire to eat?',
    font='Open Sans',
    pos=(0, 0.25), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
VAS2 = visual.Slider(win=win, name='VAS2',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.19), units=None,
    labels=('Very weak','Very strong'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-4, readOnly=False)
VAStext3 = visual.TextStim(win=win, name='VAStext3',
    text='How hungry do you feel?',
    font='Open Sans',
    pos=(0, 0.1), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
VAS3 = visual.Slider(win=win, name='VAS3',
    startValue=None, size=(1.0, 0.025), pos=(0, 0.04), units=None,
    labels=('Not at all','As hungery as I have ever felt'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-6, readOnly=False)
VAStext4 = visual.TextStim(win=win, name='VAStext4',
    text='What is your level of satiety?',
    font='Open Sans',
    pos=(0, -0.05), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
VAS4 = visual.Slider(win=win, name='VAS4',
    startValue=None, size=(1.0, 0.025), pos=(0, -0.11), units=None,
    labels=('Not satiated at all','Very high'), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-8, readOnly=False)
VAStext5 = visual.TextStim(win=win, name='VAStext5',
    text='How full do you feel?',
    font='Open Sans',
    pos=(0, -0.2), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
VAS5 = visual.Slider(win=win, name='VAS5',
    startValue=None, size=(1.0, 0.025), pos=(0, -0.26), units=None,
    labels=('Not at all full','Very full'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='black', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-10, readOnly=False)
proceed = visual.TextStim(win=win, name='proceed',
    text="Press the 'right arrow' key to proceed. Your answer on this page cannot be changed after you move on to next section.",
    font='Open Sans',
    pos=(0, -0.4), height=0.026, wrapWidth=1.8, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "completionScreen"
completionScreenClock = core.Clock()
background11 = visual.Rect(
    win=win, name='background11',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='You have completed this section of the study!\nPlease inform the researcher.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction__screen"-------
continueRoutine = True
# update component parameters for each repeat
begin_exp.keys = []
begin_exp.rt = []
_begin_exp_allKeys = []
# keep track of which components have finished
Instruction__screenComponents = [backGroud1, Instruction, begin_exp]
for thisComponent in Instruction__screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction__screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction__screen"-------
while continueRoutine:
    # get current time
    t = Instruction__screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction__screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backGroud1* updates
    if backGroud1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        backGroud1.frameNStart = frameN  # exact frame index
        backGroud1.tStart = t  # local t and not account for scr refresh
        backGroud1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(backGroud1, 'tStartRefresh')  # time at next scr refresh
        backGroud1.setAutoDraw(True)
    
    # *Instruction* updates
    if Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction.frameNStart = frameN  # exact frame index
        Instruction.tStart = t  # local t and not account for scr refresh
        Instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction, 'tStartRefresh')  # time at next scr refresh
        Instruction.setAutoDraw(True)
    
    # *begin_exp* updates
    waitOnFlip = False
    if begin_exp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        begin_exp.frameNStart = frameN  # exact frame index
        begin_exp.tStart = t  # local t and not account for scr refresh
        begin_exp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_exp, 'tStartRefresh')  # time at next scr refresh
        begin_exp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_exp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_exp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_exp.status == STARTED and not waitOnFlip:
        theseKeys = begin_exp.getKeys(keyList=['right'], waitRelease=False)
        _begin_exp_allKeys.extend(theseKeys)
        if len(_begin_exp_allKeys):
            begin_exp.keys = _begin_exp_allKeys[-1].name  # just the last key pressed
            begin_exp.rt = _begin_exp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction__screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction__screen"-------
for thisComponent in Instruction__screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('backGroud1.started', backGroud1.tStartRefresh)
thisExp.addData('backGroud1.stopped', backGroud1.tStopRefresh)
thisExp.addData('Instruction.started', Instruction.tStartRefresh)
thisExp.addData('Instruction.stopped', Instruction.tStopRefresh)
# check responses
if begin_exp.keys in ['', [], None]:  # No response was made
    begin_exp.keys = None
thisExp.addData('begin_exp.keys',begin_exp.keys)
if begin_exp.keys != None:  # we had a response
    thisExp.addData('begin_exp.rt', begin_exp.rt)
thisExp.addData('begin_exp.started', begin_exp.tStartRefresh)
thisExp.addData('begin_exp.stopped', begin_exp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction__screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "vasInstruction"-------
continueRoutine = True
# update component parameters for each repeat
proceed_VAS.keys = []
proceed_VAS.rt = []
_proceed_VAS_allKeys = []
# keep track of which components have finished
vasInstructionComponents = [polygon_3, vasIns, proceed_VAS]
for thisComponent in vasInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
vasInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "vasInstruction"-------
while continueRoutine:
    # get current time
    t = vasInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=vasInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *vasIns* updates
    if vasIns.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vasIns.frameNStart = frameN  # exact frame index
        vasIns.tStart = t  # local t and not account for scr refresh
        vasIns.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vasIns, 'tStartRefresh')  # time at next scr refresh
        vasIns.setAutoDraw(True)
    
    # *proceed_VAS* updates
    waitOnFlip = False
    if proceed_VAS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceed_VAS.frameNStart = frameN  # exact frame index
        proceed_VAS.tStart = t  # local t and not account for scr refresh
        proceed_VAS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed_VAS, 'tStartRefresh')  # time at next scr refresh
        proceed_VAS.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed_VAS.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed_VAS.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed_VAS.status == STARTED and not waitOnFlip:
        theseKeys = proceed_VAS.getKeys(keyList=['right'], waitRelease=False)
        _proceed_VAS_allKeys.extend(theseKeys)
        if len(_proceed_VAS_allKeys):
            proceed_VAS.keys = _proceed_VAS_allKeys[-1].name  # just the last key pressed
            proceed_VAS.rt = _proceed_VAS_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vasInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "vasInstruction"-------
for thisComponent in vasInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('vasIns.started', vasIns.tStartRefresh)
thisExp.addData('vasIns.stopped', vasIns.tStopRefresh)
# check responses
if proceed_VAS.keys in ['', [], None]:  # No response was made
    proceed_VAS.keys = None
thisExp.addData('proceed_VAS.keys',proceed_VAS.keys)
if proceed_VAS.keys != None:  # we had a response
    thisExp.addData('proceed_VAS.rt', proceed_VAS.rt)
thisExp.addData('proceed_VAS.started', proceed_VAS.tStartRefresh)
thisExp.addData('proceed_VAS.stopped', proceed_VAS.tStopRefresh)
thisExp.nextEntry()
# the Routine "vasInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VAS"-------
continueRoutine = True
# update component parameters for each repeat
VAS1.reset()
VAS2.reset()
VAS3.reset()
VAS4.reset()
VAS5.reset()
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
VASComponents = [polygon_2, VAStext1, VAS1, VAStext2, VAS2, VAStext3, VAS3, VAStext4, VAS4, VAStext5, VAS5, proceed, key_resp_5]
for thisComponent in VASComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VASClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VAS"-------
while continueRoutine:
    # get current time
    t = VASClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VASClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    
    # *VAStext1* updates
    if VAStext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext1.frameNStart = frameN  # exact frame index
        VAStext1.tStart = t  # local t and not account for scr refresh
        VAStext1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext1, 'tStartRefresh')  # time at next scr refresh
        VAStext1.setAutoDraw(True)
    
    # *VAS1* updates
    if VAS1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS1.frameNStart = frameN  # exact frame index
        VAS1.tStart = t  # local t and not account for scr refresh
        VAS1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS1, 'tStartRefresh')  # time at next scr refresh
        VAS1.setAutoDraw(True)
    
    # *VAStext2* updates
    if VAStext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext2.frameNStart = frameN  # exact frame index
        VAStext2.tStart = t  # local t and not account for scr refresh
        VAStext2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext2, 'tStartRefresh')  # time at next scr refresh
        VAStext2.setAutoDraw(True)
    
    # *VAS2* updates
    if VAS2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS2.frameNStart = frameN  # exact frame index
        VAS2.tStart = t  # local t and not account for scr refresh
        VAS2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS2, 'tStartRefresh')  # time at next scr refresh
        VAS2.setAutoDraw(True)
    
    # *VAStext3* updates
    if VAStext3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext3.frameNStart = frameN  # exact frame index
        VAStext3.tStart = t  # local t and not account for scr refresh
        VAStext3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext3, 'tStartRefresh')  # time at next scr refresh
        VAStext3.setAutoDraw(True)
    
    # *VAS3* updates
    if VAS3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS3.frameNStart = frameN  # exact frame index
        VAS3.tStart = t  # local t and not account for scr refresh
        VAS3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS3, 'tStartRefresh')  # time at next scr refresh
        VAS3.setAutoDraw(True)
    
    # *VAStext4* updates
    if VAStext4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext4.frameNStart = frameN  # exact frame index
        VAStext4.tStart = t  # local t and not account for scr refresh
        VAStext4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext4, 'tStartRefresh')  # time at next scr refresh
        VAStext4.setAutoDraw(True)
    
    # *VAS4* updates
    if VAS4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS4.frameNStart = frameN  # exact frame index
        VAS4.tStart = t  # local t and not account for scr refresh
        VAS4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS4, 'tStartRefresh')  # time at next scr refresh
        VAS4.setAutoDraw(True)
    
    # *VAStext5* updates
    if VAStext5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext5.frameNStart = frameN  # exact frame index
        VAStext5.tStart = t  # local t and not account for scr refresh
        VAStext5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext5, 'tStartRefresh')  # time at next scr refresh
        VAStext5.setAutoDraw(True)
    
    # *VAS5* updates
    if VAS5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS5.frameNStart = frameN  # exact frame index
        VAS5.tStart = t  # local t and not account for scr refresh
        VAS5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS5, 'tStartRefresh')  # time at next scr refresh
        VAS5.setAutoDraw(True)
    
    # *proceed* updates
    if proceed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceed.frameNStart = frameN  # exact frame index
        proceed.tStart = t  # local t and not account for scr refresh
        proceed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed, 'tStartRefresh')  # time at next scr refresh
        proceed.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VASComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VAS"-------
for thisComponent in VASComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('VAStext1.started', VAStext1.tStartRefresh)
thisExp.addData('VAStext1.stopped', VAStext1.tStopRefresh)
thisExp.addData('VAS1.response', VAS1.getRating())
thisExp.addData('VAS1.started', VAS1.tStartRefresh)
thisExp.addData('VAS1.stopped', VAS1.tStopRefresh)
thisExp.addData('VAStext2.started', VAStext2.tStartRefresh)
thisExp.addData('VAStext2.stopped', VAStext2.tStopRefresh)
thisExp.addData('VAS2.response', VAS2.getRating())
thisExp.addData('VAS2.rt', VAS2.getRT())
thisExp.addData('VAS2.started', VAS2.tStartRefresh)
thisExp.addData('VAS2.stopped', VAS2.tStopRefresh)
thisExp.addData('VAStext3.started', VAStext3.tStartRefresh)
thisExp.addData('VAStext3.stopped', VAStext3.tStopRefresh)
thisExp.addData('VAS3.response', VAS3.getRating())
thisExp.addData('VAS3.rt', VAS3.getRT())
thisExp.addData('VAS3.started', VAS3.tStartRefresh)
thisExp.addData('VAS3.stopped', VAS3.tStopRefresh)
thisExp.addData('VAStext4.started', VAStext4.tStartRefresh)
thisExp.addData('VAStext4.stopped', VAStext4.tStopRefresh)
thisExp.addData('VAS4.response', VAS4.getRating())
thisExp.addData('VAS4.rt', VAS4.getRT())
thisExp.addData('VAS4.started', VAS4.tStartRefresh)
thisExp.addData('VAS4.stopped', VAS4.tStopRefresh)
thisExp.addData('VAStext5.started', VAStext5.tStartRefresh)
thisExp.addData('VAStext5.stopped', VAStext5.tStopRefresh)
thisExp.addData('VAS5.response', VAS5.getRating())
thisExp.addData('VAS5.rt', VAS5.getRT())
thisExp.addData('VAS5.started', VAS5.tStartRefresh)
thisExp.addData('VAS5.stopped', VAS5.tStopRefresh)
thisExp.addData('proceed.started', proceed.tStartRefresh)
thisExp.addData('proceed.stopped', proceed.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "VAS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_ins"-------
continueRoutine = True
# update component parameters for each repeat
practiceTrial_key.keys = []
practiceTrial_key.rt = []
_practiceTrial_key_allKeys = []
# keep track of which components have finished
practice_insComponents = [backgroud2, prac_inst, practiceTrial_key]
for thisComponent in practice_insComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_insClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_ins"-------
while continueRoutine:
    # get current time
    t = practice_insClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_insClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *backgroud2* updates
    if backgroud2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        backgroud2.frameNStart = frameN  # exact frame index
        backgroud2.tStart = t  # local t and not account for scr refresh
        backgroud2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(backgroud2, 'tStartRefresh')  # time at next scr refresh
        backgroud2.setAutoDraw(True)
    
    # *prac_inst* updates
    if prac_inst.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        prac_inst.frameNStart = frameN  # exact frame index
        prac_inst.tStart = t  # local t and not account for scr refresh
        prac_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_inst, 'tStartRefresh')  # time at next scr refresh
        prac_inst.setAutoDraw(True)
    
    # *practiceTrial_key* updates
    waitOnFlip = False
    if practiceTrial_key.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        practiceTrial_key.frameNStart = frameN  # exact frame index
        practiceTrial_key.tStart = t  # local t and not account for scr refresh
        practiceTrial_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceTrial_key, 'tStartRefresh')  # time at next scr refresh
        practiceTrial_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceTrial_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceTrial_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceTrial_key.status == STARTED and not waitOnFlip:
        theseKeys = practiceTrial_key.getKeys(keyList=['right'], waitRelease=False)
        _practiceTrial_key_allKeys.extend(theseKeys)
        if len(_practiceTrial_key_allKeys):
            practiceTrial_key.keys = _practiceTrial_key_allKeys[-1].name  # just the last key pressed
            practiceTrial_key.rt = _practiceTrial_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_ins"-------
for thisComponent in practice_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('backgroud2.started', backgroud2.tStartRefresh)
thisExp.addData('backgroud2.stopped', backgroud2.tStopRefresh)
thisExp.addData('prac_inst.started', prac_inst.tStartRefresh)
thisExp.addData('prac_inst.stopped', prac_inst.tStopRefresh)
# check responses
if practiceTrial_key.keys in ['', [], None]:  # No response was made
    practiceTrial_key.keys = None
thisExp.addData('practiceTrial_key.keys',practiceTrial_key.keys)
if practiceTrial_key.keys != None:  # we had a response
    thisExp.addData('practiceTrial_key.rt', practiceTrial_key.rt)
thisExp.addData('practiceTrial_key.started', practiceTrial_key.tStartRefresh)
thisExp.addData('practiceTrial_key.stopped', practiceTrial_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Practice Trial.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PracticeTrials"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    practice_word.setColor(prt_color, colorSpace='rgb')
    practice_word.setText(prt_word)
    practice_key.keys = []
    practice_key.rt = []
    _practice_key_allKeys = []
    # keep track of which components have finished
    PracticeTrialsComponents = [background3, practiceFixation, practice_word, practice_key]
    for thisComponent in PracticeTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PracticeTrials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background3* updates
        if background3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background3.frameNStart = frameN  # exact frame index
            background3.tStart = t  # local t and not account for scr refresh
            background3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background3, 'tStartRefresh')  # time at next scr refresh
            background3.setAutoDraw(True)
        if background3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background3.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                background3.tStop = t  # not accounting for scr refresh
                background3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(background3, 'tStopRefresh')  # time at next scr refresh
                background3.setAutoDraw(False)
        
        # *practiceFixation* updates
        if practiceFixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            practiceFixation.frameNStart = frameN  # exact frame index
            practiceFixation.tStart = t  # local t and not account for scr refresh
            practiceFixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceFixation, 'tStartRefresh')  # time at next scr refresh
            practiceFixation.setAutoDraw(True)
        if practiceFixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practiceFixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                practiceFixation.tStop = t  # not accounting for scr refresh
                practiceFixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practiceFixation, 'tStopRefresh')  # time at next scr refresh
                practiceFixation.setAutoDraw(False)
        
        # *practice_word* updates
        if practice_word.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            practice_word.frameNStart = frameN  # exact frame index
            practice_word.tStart = t  # local t and not account for scr refresh
            practice_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_word, 'tStartRefresh')  # time at next scr refresh
            practice_word.setAutoDraw(True)
        if practice_word.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_word.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                practice_word.tStop = t  # not accounting for scr refresh
                practice_word.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_word, 'tStopRefresh')  # time at next scr refresh
                practice_word.setAutoDraw(False)
        
        # *practice_key* updates
        waitOnFlip = False
        if practice_key.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            practice_key.frameNStart = frameN  # exact frame index
            practice_key.tStart = t  # local t and not account for scr refresh
            practice_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_key, 'tStartRefresh')  # time at next scr refresh
            practice_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practice_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practice_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_key.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                practice_key.tStop = t  # not accounting for scr refresh
                practice_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_key, 'tStopRefresh')  # time at next scr refresh
                practice_key.status = FINISHED
        if practice_key.status == STARTED and not waitOnFlip:
            theseKeys = practice_key.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
            _practice_key_allKeys.extend(theseKeys)
            if len(_practice_key_allKeys):
                practice_key.keys = _practice_key_allKeys[-1].name  # just the last key pressed
                practice_key.rt = _practice_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeTrials"-------
    for thisComponent in PracticeTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('background3.started', background3.tStartRefresh)
    practice.addData('background3.stopped', background3.tStopRefresh)
    practice.addData('practiceFixation.started', practiceFixation.tStartRefresh)
    practice.addData('practiceFixation.stopped', practiceFixation.tStopRefresh)
    practice.addData('practice_word.started', practice_word.tStartRefresh)
    practice.addData('practice_word.stopped', practice_word.tStopRefresh)
    # check responses
    if practice_key.keys in ['', [], None]:  # No response was made
        practice_key.keys = None
    practice.addData('practice_key.keys',practice_key.keys)
    if practice_key.keys != None:  # we had a response
        practice.addData('practice_key.rt', practice_key.rt)
    practice.addData('practice_key.started', practice_key.tStartRefresh)
    practice.addData('practice_key.stopped', practice_key.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'practice'


# ------Prepare to start Routine "BeginBaseline"-------
continueRoutine = True
# update component parameters for each repeat
begin_key.keys = []
begin_key.rt = []
_begin_key_allKeys = []
# keep track of which components have finished
BeginBaselineComponents = [background4, beginexp, begin_key]
for thisComponent in BeginBaselineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginBaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BeginBaseline"-------
while continueRoutine:
    # get current time
    t = BeginBaselineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginBaselineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background4* updates
    if background4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background4.frameNStart = frameN  # exact frame index
        background4.tStart = t  # local t and not account for scr refresh
        background4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background4, 'tStartRefresh')  # time at next scr refresh
        background4.setAutoDraw(True)
    
    # *beginexp* updates
    if beginexp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        beginexp.frameNStart = frameN  # exact frame index
        beginexp.tStart = t  # local t and not account for scr refresh
        beginexp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beginexp, 'tStartRefresh')  # time at next scr refresh
        beginexp.setAutoDraw(True)
    
    # *begin_key* updates
    waitOnFlip = False
    if begin_key.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        begin_key.frameNStart = frameN  # exact frame index
        begin_key.tStart = t  # local t and not account for scr refresh
        begin_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_key, 'tStartRefresh')  # time at next scr refresh
        begin_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_key.status == STARTED and not waitOnFlip:
        theseKeys = begin_key.getKeys(keyList=['right'], waitRelease=False)
        _begin_key_allKeys.extend(theseKeys)
        if len(_begin_key_allKeys):
            begin_key.keys = _begin_key_allKeys[-1].name  # just the last key pressed
            begin_key.rt = _begin_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginBaselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BeginBaseline"-------
for thisComponent in BeginBaselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('background4.started', background4.tStartRefresh)
thisExp.addData('background4.stopped', background4.tStopRefresh)
thisExp.addData('beginexp.started', beginexp.tStartRefresh)
thisExp.addData('beginexp.stopped', beginexp.tStopRefresh)
# check responses
if begin_key.keys in ['', [], None]:  # No response was made
    begin_key.keys = None
thisExp.addData('begin_key.keys',begin_key.keys)
if begin_key.keys != None:  # we had a response
    thisExp.addData('begin_key.rt', begin_key.rt)
thisExp.addData('begin_key.started', begin_key.tStartRefresh)
thisExp.addData('begin_key.stopped', begin_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "BeginBaseline" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Baseline_trials = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Baseline_trials')
thisExp.addLoop(Baseline_trials)  # add the loop to the experiment
thisBaseline_trial = Baseline_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBaseline_trial.rgb)
if thisBaseline_trial != None:
    for paramName in thisBaseline_trial:
        exec('{} = thisBaseline_trial[paramName]'.format(paramName))

for thisBaseline_trial in Baseline_trials:
    currentLoop = Baseline_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBaseline_trial.rgb)
    if thisBaseline_trial != None:
        for paramName in thisBaseline_trial:
            exec('{} = thisBaseline_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Baseline_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    #assigning baseline word
    WordItem=all_word_lst[baseline_trial]
    WordColor=all_color_lst[baseline_trial]
    
    WordType = "undefined"
    if WordItem in food:
        WordType = "food"
    if WordItem in neutral:
        WordType = "neutral"
    
    #Record variables
    thisExp.addData('wordContent', WordItem)
    thisExp.addData('wordColor', WordColor)
    thisExp.addData('wordType', WordType)
    
    #update trial num
    baseline_trial+=1
    # keep track of which components have finished
    Baseline_codeComponents = []
    for thisComponent in Baseline_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Baseline_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Baseline_code"-------
    while continueRoutine:
        # get current time
        t = Baseline_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Baseline_codeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Baseline_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Baseline_code"-------
    for thisComponent in Baseline_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Baseline_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Baseline_Stroop"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    baseline_stroop_word.setColor(WordColor, colorSpace='rgb')
    baseline_stroop_word.setText(WordItem)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    Baseline_StroopComponents = [background5, baseline_stroop_word, baseline_fixation, key_resp]
    for thisComponent in Baseline_StroopComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Baseline_StroopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Baseline_Stroop"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Baseline_StroopClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Baseline_StroopClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background5* updates
        if background5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background5.frameNStart = frameN  # exact frame index
            background5.tStart = t  # local t and not account for scr refresh
            background5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background5, 'tStartRefresh')  # time at next scr refresh
            background5.setAutoDraw(True)
        if background5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background5.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                background5.tStop = t  # not accounting for scr refresh
                background5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(background5, 'tStopRefresh')  # time at next scr refresh
                background5.setAutoDraw(False)
        
        # *baseline_stroop_word* updates
        if baseline_stroop_word.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            baseline_stroop_word.frameNStart = frameN  # exact frame index
            baseline_stroop_word.tStart = t  # local t and not account for scr refresh
            baseline_stroop_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_stroop_word, 'tStartRefresh')  # time at next scr refresh
            baseline_stroop_word.setAutoDraw(True)
        if baseline_stroop_word.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_stroop_word.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                baseline_stroop_word.tStop = t  # not accounting for scr refresh
                baseline_stroop_word.frameNStop = frameN  # exact frame index
                win.timeOnFlip(baseline_stroop_word, 'tStopRefresh')  # time at next scr refresh
                baseline_stroop_word.setAutoDraw(False)
        
        # *baseline_fixation* updates
        if baseline_fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            baseline_fixation.frameNStart = frameN  # exact frame index
            baseline_fixation.tStart = t  # local t and not account for scr refresh
            baseline_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_fixation, 'tStartRefresh')  # time at next scr refresh
            baseline_fixation.setAutoDraw(True)
        if baseline_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                baseline_fixation.tStop = t  # not accounting for scr refresh
                baseline_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(baseline_fixation, 'tStopRefresh')  # time at next scr refresh
                baseline_fixation.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Baseline_StroopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Baseline_Stroop"-------
    for thisComponent in Baseline_StroopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Baseline_trials.addData('background5.started', background5.tStartRefresh)
    Baseline_trials.addData('background5.stopped', background5.tStopRefresh)
    Baseline_trials.addData('baseline_stroop_word.started', baseline_stroop_word.tStartRefresh)
    Baseline_trials.addData('baseline_stroop_word.stopped', baseline_stroop_word.tStopRefresh)
    Baseline_trials.addData('baseline_fixation.started', baseline_fixation.tStartRefresh)
    Baseline_trials.addData('baseline_fixation.stopped', baseline_fixation.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    Baseline_trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        Baseline_trials.addData('key_resp.rt', key_resp.rt)
    Baseline_trials.addData('key_resp.started', key_resp.tStartRefresh)
    Baseline_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'Baseline_trials'


# ------Prepare to start Routine "vasInstruction"-------
continueRoutine = True
# update component parameters for each repeat
proceed_VAS.keys = []
proceed_VAS.rt = []
_proceed_VAS_allKeys = []
# keep track of which components have finished
vasInstructionComponents = [polygon_3, vasIns, proceed_VAS]
for thisComponent in vasInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
vasInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "vasInstruction"-------
while continueRoutine:
    # get current time
    t = vasInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=vasInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *vasIns* updates
    if vasIns.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vasIns.frameNStart = frameN  # exact frame index
        vasIns.tStart = t  # local t and not account for scr refresh
        vasIns.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vasIns, 'tStartRefresh')  # time at next scr refresh
        vasIns.setAutoDraw(True)
    
    # *proceed_VAS* updates
    waitOnFlip = False
    if proceed_VAS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceed_VAS.frameNStart = frameN  # exact frame index
        proceed_VAS.tStart = t  # local t and not account for scr refresh
        proceed_VAS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed_VAS, 'tStartRefresh')  # time at next scr refresh
        proceed_VAS.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed_VAS.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed_VAS.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed_VAS.status == STARTED and not waitOnFlip:
        theseKeys = proceed_VAS.getKeys(keyList=['right'], waitRelease=False)
        _proceed_VAS_allKeys.extend(theseKeys)
        if len(_proceed_VAS_allKeys):
            proceed_VAS.keys = _proceed_VAS_allKeys[-1].name  # just the last key pressed
            proceed_VAS.rt = _proceed_VAS_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vasInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "vasInstruction"-------
for thisComponent in vasInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('vasIns.started', vasIns.tStartRefresh)
thisExp.addData('vasIns.stopped', vasIns.tStopRefresh)
# check responses
if proceed_VAS.keys in ['', [], None]:  # No response was made
    proceed_VAS.keys = None
thisExp.addData('proceed_VAS.keys',proceed_VAS.keys)
if proceed_VAS.keys != None:  # we had a response
    thisExp.addData('proceed_VAS.rt', proceed_VAS.rt)
thisExp.addData('proceed_VAS.started', proceed_VAS.tStartRefresh)
thisExp.addData('proceed_VAS.stopped', proceed_VAS.tStopRefresh)
thisExp.nextEntry()
# the Routine "vasInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VAS"-------
continueRoutine = True
# update component parameters for each repeat
VAS1.reset()
VAS2.reset()
VAS3.reset()
VAS4.reset()
VAS5.reset()
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
VASComponents = [polygon_2, VAStext1, VAS1, VAStext2, VAS2, VAStext3, VAS3, VAStext4, VAS4, VAStext5, VAS5, proceed, key_resp_5]
for thisComponent in VASComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VASClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VAS"-------
while continueRoutine:
    # get current time
    t = VASClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VASClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    
    # *VAStext1* updates
    if VAStext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext1.frameNStart = frameN  # exact frame index
        VAStext1.tStart = t  # local t and not account for scr refresh
        VAStext1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext1, 'tStartRefresh')  # time at next scr refresh
        VAStext1.setAutoDraw(True)
    
    # *VAS1* updates
    if VAS1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS1.frameNStart = frameN  # exact frame index
        VAS1.tStart = t  # local t and not account for scr refresh
        VAS1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS1, 'tStartRefresh')  # time at next scr refresh
        VAS1.setAutoDraw(True)
    
    # *VAStext2* updates
    if VAStext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext2.frameNStart = frameN  # exact frame index
        VAStext2.tStart = t  # local t and not account for scr refresh
        VAStext2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext2, 'tStartRefresh')  # time at next scr refresh
        VAStext2.setAutoDraw(True)
    
    # *VAS2* updates
    if VAS2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS2.frameNStart = frameN  # exact frame index
        VAS2.tStart = t  # local t and not account for scr refresh
        VAS2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS2, 'tStartRefresh')  # time at next scr refresh
        VAS2.setAutoDraw(True)
    
    # *VAStext3* updates
    if VAStext3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext3.frameNStart = frameN  # exact frame index
        VAStext3.tStart = t  # local t and not account for scr refresh
        VAStext3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext3, 'tStartRefresh')  # time at next scr refresh
        VAStext3.setAutoDraw(True)
    
    # *VAS3* updates
    if VAS3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS3.frameNStart = frameN  # exact frame index
        VAS3.tStart = t  # local t and not account for scr refresh
        VAS3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS3, 'tStartRefresh')  # time at next scr refresh
        VAS3.setAutoDraw(True)
    
    # *VAStext4* updates
    if VAStext4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext4.frameNStart = frameN  # exact frame index
        VAStext4.tStart = t  # local t and not account for scr refresh
        VAStext4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext4, 'tStartRefresh')  # time at next scr refresh
        VAStext4.setAutoDraw(True)
    
    # *VAS4* updates
    if VAS4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS4.frameNStart = frameN  # exact frame index
        VAS4.tStart = t  # local t and not account for scr refresh
        VAS4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS4, 'tStartRefresh')  # time at next scr refresh
        VAS4.setAutoDraw(True)
    
    # *VAStext5* updates
    if VAStext5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext5.frameNStart = frameN  # exact frame index
        VAStext5.tStart = t  # local t and not account for scr refresh
        VAStext5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext5, 'tStartRefresh')  # time at next scr refresh
        VAStext5.setAutoDraw(True)
    
    # *VAS5* updates
    if VAS5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS5.frameNStart = frameN  # exact frame index
        VAS5.tStart = t  # local t and not account for scr refresh
        VAS5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS5, 'tStartRefresh')  # time at next scr refresh
        VAS5.setAutoDraw(True)
    
    # *proceed* updates
    if proceed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceed.frameNStart = frameN  # exact frame index
        proceed.tStart = t  # local t and not account for scr refresh
        proceed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed, 'tStartRefresh')  # time at next scr refresh
        proceed.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VASComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VAS"-------
for thisComponent in VASComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('VAStext1.started', VAStext1.tStartRefresh)
thisExp.addData('VAStext1.stopped', VAStext1.tStopRefresh)
thisExp.addData('VAS1.response', VAS1.getRating())
thisExp.addData('VAS1.started', VAS1.tStartRefresh)
thisExp.addData('VAS1.stopped', VAS1.tStopRefresh)
thisExp.addData('VAStext2.started', VAStext2.tStartRefresh)
thisExp.addData('VAStext2.stopped', VAStext2.tStopRefresh)
thisExp.addData('VAS2.response', VAS2.getRating())
thisExp.addData('VAS2.rt', VAS2.getRT())
thisExp.addData('VAS2.started', VAS2.tStartRefresh)
thisExp.addData('VAS2.stopped', VAS2.tStopRefresh)
thisExp.addData('VAStext3.started', VAStext3.tStartRefresh)
thisExp.addData('VAStext3.stopped', VAStext3.tStopRefresh)
thisExp.addData('VAS3.response', VAS3.getRating())
thisExp.addData('VAS3.rt', VAS3.getRT())
thisExp.addData('VAS3.started', VAS3.tStartRefresh)
thisExp.addData('VAS3.stopped', VAS3.tStopRefresh)
thisExp.addData('VAStext4.started', VAStext4.tStartRefresh)
thisExp.addData('VAStext4.stopped', VAStext4.tStopRefresh)
thisExp.addData('VAS4.response', VAS4.getRating())
thisExp.addData('VAS4.rt', VAS4.getRT())
thisExp.addData('VAS4.started', VAS4.tStartRefresh)
thisExp.addData('VAS4.stopped', VAS4.tStopRefresh)
thisExp.addData('VAStext5.started', VAStext5.tStartRefresh)
thisExp.addData('VAStext5.stopped', VAStext5.tStopRefresh)
thisExp.addData('VAS5.response', VAS5.getRating())
thisExp.addData('VAS5.rt', VAS5.getRT())
thisExp.addData('VAS5.started', VAS5.tStartRefresh)
thisExp.addData('VAS5.stopped', VAS5.tStopRefresh)
thisExp.addData('proceed.started', proceed.tStartRefresh)
thisExp.addData('proceed.stopped', proceed.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "VAS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Begin_Video_obs_task"-------
continueRoutine = True
# update component parameters for each repeat
proceed_to_conditions.keys = []
proceed_to_conditions.rt = []
_proceed_to_conditions_allKeys = []
# keep track of which components have finished
Begin_Video_obs_taskComponents = [background6, begin_video_obs, proceed_to_conditions]
for thisComponent in Begin_Video_obs_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Begin_Video_obs_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Begin_Video_obs_task"-------
while continueRoutine:
    # get current time
    t = Begin_Video_obs_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Begin_Video_obs_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background6* updates
    if background6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background6.frameNStart = frameN  # exact frame index
        background6.tStart = t  # local t and not account for scr refresh
        background6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background6, 'tStartRefresh')  # time at next scr refresh
        background6.setAutoDraw(True)
    
    # *begin_video_obs* updates
    if begin_video_obs.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        begin_video_obs.frameNStart = frameN  # exact frame index
        begin_video_obs.tStart = t  # local t and not account for scr refresh
        begin_video_obs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_video_obs, 'tStartRefresh')  # time at next scr refresh
        begin_video_obs.setAutoDraw(True)
    
    # *proceed_to_conditions* updates
    waitOnFlip = False
    if proceed_to_conditions.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        proceed_to_conditions.frameNStart = frameN  # exact frame index
        proceed_to_conditions.tStart = t  # local t and not account for scr refresh
        proceed_to_conditions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed_to_conditions, 'tStartRefresh')  # time at next scr refresh
        proceed_to_conditions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed_to_conditions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed_to_conditions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed_to_conditions.status == STARTED and not waitOnFlip:
        theseKeys = proceed_to_conditions.getKeys(keyList=['right'], waitRelease=False)
        _proceed_to_conditions_allKeys.extend(theseKeys)
        if len(_proceed_to_conditions_allKeys):
            proceed_to_conditions.keys = _proceed_to_conditions_allKeys[-1].name  # just the last key pressed
            proceed_to_conditions.rt = _proceed_to_conditions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Begin_Video_obs_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Begin_Video_obs_task"-------
for thisComponent in Begin_Video_obs_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('background6.started', background6.tStartRefresh)
thisExp.addData('background6.stopped', background6.tStopRefresh)
thisExp.addData('begin_video_obs.started', begin_video_obs.tStartRefresh)
thisExp.addData('begin_video_obs.stopped', begin_video_obs.tStopRefresh)
# check responses
if proceed_to_conditions.keys in ['', [], None]:  # No response was made
    proceed_to_conditions.keys = None
thisExp.addData('proceed_to_conditions.keys',proceed_to_conditions.keys)
if proceed_to_conditions.keys != None:  # we had a response
    thisExp.addData('proceed_to_conditions.rt', proceed_to_conditions.rt)
thisExp.addData('proceed_to_conditions.started', proceed_to_conditions.tStartRefresh)
thisExp.addData('proceed_to_conditions.stopped', proceed_to_conditions.tStopRefresh)
thisExp.nextEntry()
# the Routine "Begin_Video_obs_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_for_ct_balance = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_for_ct_balance')
thisExp.addLoop(loop_for_ct_balance)  # add the loop to the experiment
thisLoop_for_ct_balance = loop_for_ct_balance.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_for_ct_balance.rgb)
if thisLoop_for_ct_balance != None:
    for paramName in thisLoop_for_ct_balance:
        exec('{} = thisLoop_for_ct_balance[paramName]'.format(paramName))

for thisLoop_for_ct_balance in loop_for_ct_balance:
    currentLoop = loop_for_ct_balance
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_for_ct_balance.rgb)
    if thisLoop_for_ct_balance != None:
        for paramName in thisLoop_for_ct_balance:
            exec('{} = thisLoop_for_ct_balance[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Counter_balance_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    #Loop 3 times overall
    #Decide whether a condition appear and loops at the begining of the current loop
    nRepA=eo_presence[cdt_order][cdt_num]*nTrial
    nRepB=fo_presence[cdt_order][cdt_num]*nTrial
    nRepC=nf_presence[cdt_order][cdt_num]*nTrial
    # keep track of which components have finished
    Counter_balance_codeComponents = []
    for thisComponent in Counter_balance_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Counter_balance_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Counter_balance_code"-------
    while continueRoutine:
        # get current time
        t = Counter_balance_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Counter_balance_codeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Counter_balance_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Counter_balance_code"-------
    for thisComponent in Counter_balance_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Counter_balance_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    eo_trials = data.TrialHandler(nReps=nRepA, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='eo_trials')
    thisExp.addLoop(eo_trials)  # add the loop to the experiment
    thisEo_trial = eo_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEo_trial.rgb)
    if thisEo_trial != None:
        for paramName in thisEo_trial:
            exec('{} = thisEo_trial[paramName]'.format(paramName))
    
    for thisEo_trial in eo_trials:
        currentLoop = eo_trials
        # abbreviate parameter names if possible (e.g. rgb = thisEo_trial.rgb)
        if thisEo_trial != None:
            for paramName in thisEo_trial:
                exec('{} = thisEo_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "EO_CODE"-------
        continueRoutine = True
        # update component parameters for each repeat
        #assigning baseline word
        eo_WordItem=eo_word_lst[eo_trial]
        eo_WordColor=eo_color_lst[eo_trial]
        eo_video=videoA[eo_trial]
        
        eo_WordType = "undefined"
        if eo_WordItem in food:
            eo_WordType = "food"
        if eo_WordItem in neutral:
            eo_WordType = "neutral"
        
        eo_condition='EO'
        
        #Record variables
        thisExp.addData('wordContent', eo_WordItem)
        thisExp.addData('wordColor', eo_WordColor)
        thisExp.addData('wordType', eo_WordType)
        thisExp.addData('Condition', eo_condition)
        
        #update trial num
        eo_trial+=1
        # keep track of which components have finished
        EO_CODEComponents = []
        for thisComponent in EO_CODEComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EO_CODEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "EO_CODE"-------
        while continueRoutine:
            # get current time
            t = EO_CODEClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EO_CODEClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EO_CODEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "EO_CODE"-------
        for thisComponent in EO_CODEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "EO_CODE" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "preloadVideo"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        preloadVideoComponents = [PreloadBackground]
        for thisComponent in preloadVideoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        preloadVideoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "preloadVideo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = preloadVideoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=preloadVideoClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PreloadBackground* updates
            if PreloadBackground.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PreloadBackground.frameNStart = frameN  # exact frame index
                PreloadBackground.tStart = t  # local t and not account for scr refresh
                PreloadBackground.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PreloadBackground, 'tStartRefresh')  # time at next scr refresh
                PreloadBackground.setAutoDraw(True)
            if PreloadBackground.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PreloadBackground.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    PreloadBackground.tStop = t  # not accounting for scr refresh
                    PreloadBackground.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PreloadBackground, 'tStopRefresh')  # time at next scr refresh
                    PreloadBackground.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preloadVideoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "preloadVideo"-------
        for thisComponent in preloadVideoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        eo_trials.addData('PreloadBackground.started', PreloadBackground.tStartRefresh)
        eo_trials.addData('PreloadBackground.stopped', PreloadBackground.tStopRefresh)
        
        # ------Prepare to start Routine "EO_Condition"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        eo_Stroop_word.setColor(eo_WordColor, colorSpace='rgb')
        eo_Stroop_word.setText(eo_WordItem)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        eo_video = visual.MovieStim3(
            win=win, name='eo_video',units='cm', 
            noAudio = True,
            filename=eo_video,
            ori=0.0, pos=(0, 0), opacity=1.0,
            loop=False,
            size=[28.8,16.2],
            depth=-4.0,
            )
        # keep track of which components have finished
        EO_ConditionComponents = [polygon, eo_Stroop_word, eo_fixation_cross, key_resp_2, eo_video]
        for thisComponent in EO_ConditionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EO_ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "EO_Condition"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = EO_ConditionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EO_ConditionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # *eo_Stroop_word* updates
            if eo_Stroop_word.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                eo_Stroop_word.frameNStart = frameN  # exact frame index
                eo_Stroop_word.tStart = t  # local t and not account for scr refresh
                eo_Stroop_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eo_Stroop_word, 'tStartRefresh')  # time at next scr refresh
                eo_Stroop_word.setAutoDraw(True)
            if eo_Stroop_word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > eo_Stroop_word.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    eo_Stroop_word.tStop = t  # not accounting for scr refresh
                    eo_Stroop_word.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(eo_Stroop_word, 'tStopRefresh')  # time at next scr refresh
                    eo_Stroop_word.setAutoDraw(False)
            
            # *eo_fixation_cross* updates
            if eo_fixation_cross.status == NOT_STARTED and tThisFlip >= 2.75-frameTolerance:
                # keep track of start time/frame for later
                eo_fixation_cross.frameNStart = frameN  # exact frame index
                eo_fixation_cross.tStart = t  # local t and not account for scr refresh
                eo_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eo_fixation_cross, 'tStartRefresh')  # time at next scr refresh
                eo_fixation_cross.setAutoDraw(True)
            if eo_fixation_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > eo_fixation_cross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    eo_fixation_cross.tStop = t  # not accounting for scr refresh
                    eo_fixation_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(eo_fixation_cross, 'tStopRefresh')  # time at next scr refresh
                    eo_fixation_cross.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *eo_video* updates
            if eo_video.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                eo_video.frameNStart = frameN  # exact frame index
                eo_video.tStart = t  # local t and not account for scr refresh
                eo_video.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eo_video, 'tStartRefresh')  # time at next scr refresh
                eo_video.setAutoDraw(True)
            if eo_video.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > eo_video.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    eo_video.tStop = t  # not accounting for scr refresh
                    eo_video.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(eo_video, 'tStopRefresh')  # time at next scr refresh
                    eo_video.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EO_ConditionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "EO_Condition"-------
        for thisComponent in EO_ConditionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        eo_trials.addData('polygon.started', polygon.tStartRefresh)
        eo_trials.addData('polygon.stopped', polygon.tStopRefresh)
        eo_trials.addData('eo_Stroop_word.started', eo_Stroop_word.tStartRefresh)
        eo_trials.addData('eo_Stroop_word.stopped', eo_Stroop_word.tStopRefresh)
        eo_trials.addData('eo_fixation_cross.started', eo_fixation_cross.tStartRefresh)
        eo_trials.addData('eo_fixation_cross.stopped', eo_fixation_cross.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        eo_trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            eo_trials.addData('key_resp_2.rt', key_resp_2.rt)
        eo_trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        eo_trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        eo_video.stop()
        thisExp.nextEntry()
        
    # completed nRepA repeats of 'eo_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    fo_loop = data.TrialHandler(nReps=nRepB, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fo_loop')
    thisExp.addLoop(fo_loop)  # add the loop to the experiment
    thisFo_loop = fo_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFo_loop.rgb)
    if thisFo_loop != None:
        for paramName in thisFo_loop:
            exec('{} = thisFo_loop[paramName]'.format(paramName))
    
    for thisFo_loop in fo_loop:
        currentLoop = fo_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFo_loop.rgb)
        if thisFo_loop != None:
            for paramName in thisFo_loop:
                exec('{} = thisFo_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FO_CODE"-------
        continueRoutine = True
        # update component parameters for each repeat
        #assigning baseline word
        fo_WordItem=fo_word_lst[fo_trial]
        fo_WordColor=fo_color_lst[fo_trial]
        fo_video=videoB[fo_trial]
        
        fo_WordType = "undefined"
        if fo_WordItem in food:
            fo_WordType = "food"
        if fo_WordItem in neutral:
            fo_WordType = "neutral"
        
        fo_condition='FO'
        
        #Record variables
        thisExp.addData('wordContent', fo_WordItem)
        thisExp.addData('wordColor', fo_WordColor)
        thisExp.addData('wordType', fo_WordType)
        thisExp.addData('Condition', fo_condition)
        
        #update trial num
        fo_trial+=1
        # keep track of which components have finished
        FO_CODEComponents = []
        for thisComponent in FO_CODEComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FO_CODEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FO_CODE"-------
        while continueRoutine:
            # get current time
            t = FO_CODEClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FO_CODEClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FO_CODEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FO_CODE"-------
        for thisComponent in FO_CODEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "FO_CODE" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "preloadVideo"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        preloadVideoComponents = [PreloadBackground]
        for thisComponent in preloadVideoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        preloadVideoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "preloadVideo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = preloadVideoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=preloadVideoClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PreloadBackground* updates
            if PreloadBackground.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PreloadBackground.frameNStart = frameN  # exact frame index
                PreloadBackground.tStart = t  # local t and not account for scr refresh
                PreloadBackground.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PreloadBackground, 'tStartRefresh')  # time at next scr refresh
                PreloadBackground.setAutoDraw(True)
            if PreloadBackground.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PreloadBackground.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    PreloadBackground.tStop = t  # not accounting for scr refresh
                    PreloadBackground.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PreloadBackground, 'tStopRefresh')  # time at next scr refresh
                    PreloadBackground.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preloadVideoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "preloadVideo"-------
        for thisComponent in preloadVideoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fo_loop.addData('PreloadBackground.started', PreloadBackground.tStartRefresh)
        fo_loop.addData('PreloadBackground.stopped', PreloadBackground.tStopRefresh)
        
        # ------Prepare to start Routine "FO_Condition"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        fo_video = visual.MovieStim3(
            win=win, name='fo_video',units='cm', 
            noAudio = True,
            filename=fo_video,
            ori=0.0, pos=(0, 0), opacity=None,
            loop=False,
            size=[28.8,16.2],
            depth=-1.0,
            )
        fo_word.setColor(fo_WordColor, colorSpace='rgb')
        fo_word.setText(fo_WordItem)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        FO_ConditionComponents = [background7, fo_video, fo_fixation_cross, fo_word, key_resp_3]
        for thisComponent in FO_ConditionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FO_ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FO_Condition"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FO_ConditionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FO_ConditionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background7* updates
            if background7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background7.frameNStart = frameN  # exact frame index
                background7.tStart = t  # local t and not account for scr refresh
                background7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background7, 'tStartRefresh')  # time at next scr refresh
                background7.setAutoDraw(True)
            if background7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > background7.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    background7.tStop = t  # not accounting for scr refresh
                    background7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(background7, 'tStopRefresh')  # time at next scr refresh
                    background7.setAutoDraw(False)
            
            # *fo_video* updates
            if fo_video.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fo_video.frameNStart = frameN  # exact frame index
                fo_video.tStart = t  # local t and not account for scr refresh
                fo_video.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fo_video, 'tStartRefresh')  # time at next scr refresh
                fo_video.setAutoDraw(True)
            if fo_video.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fo_video.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fo_video.tStop = t  # not accounting for scr refresh
                    fo_video.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fo_video, 'tStopRefresh')  # time at next scr refresh
                    fo_video.setAutoDraw(False)
            
            # *fo_fixation_cross* updates
            if fo_fixation_cross.status == NOT_STARTED and tThisFlip >= 2.75-frameTolerance:
                # keep track of start time/frame for later
                fo_fixation_cross.frameNStart = frameN  # exact frame index
                fo_fixation_cross.tStart = t  # local t and not account for scr refresh
                fo_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fo_fixation_cross, 'tStartRefresh')  # time at next scr refresh
                fo_fixation_cross.setAutoDraw(True)
            if fo_fixation_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fo_fixation_cross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fo_fixation_cross.tStop = t  # not accounting for scr refresh
                    fo_fixation_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fo_fixation_cross, 'tStopRefresh')  # time at next scr refresh
                    fo_fixation_cross.setAutoDraw(False)
            
            # *fo_word* updates
            if fo_word.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                fo_word.frameNStart = frameN  # exact frame index
                fo_word.tStart = t  # local t and not account for scr refresh
                fo_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fo_word, 'tStartRefresh')  # time at next scr refresh
                fo_word.setAutoDraw(True)
            if fo_word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fo_word.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fo_word.tStop = t  # not accounting for scr refresh
                    fo_word.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fo_word, 'tStopRefresh')  # time at next scr refresh
                    fo_word.setAutoDraw(False)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_3.tStop = t  # not accounting for scr refresh
                    key_resp_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                    key_resp_3.status = FINISHED
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FO_ConditionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FO_Condition"-------
        for thisComponent in FO_ConditionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fo_loop.addData('background7.started', background7.tStartRefresh)
        fo_loop.addData('background7.stopped', background7.tStopRefresh)
        fo_video.stop()
        fo_loop.addData('fo_fixation_cross.started', fo_fixation_cross.tStartRefresh)
        fo_loop.addData('fo_fixation_cross.stopped', fo_fixation_cross.tStopRefresh)
        fo_loop.addData('fo_word.started', fo_word.tStartRefresh)
        fo_loop.addData('fo_word.stopped', fo_word.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        fo_loop.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            fo_loop.addData('key_resp_3.rt', key_resp_3.rt)
        fo_loop.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        fo_loop.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nRepB repeats of 'fo_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    nf_trials = data.TrialHandler(nReps=nRepC, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='nf_trials')
    thisExp.addLoop(nf_trials)  # add the loop to the experiment
    thisNf_trial = nf_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNf_trial.rgb)
    if thisNf_trial != None:
        for paramName in thisNf_trial:
            exec('{} = thisNf_trial[paramName]'.format(paramName))
    
    for thisNf_trial in nf_trials:
        currentLoop = nf_trials
        # abbreviate parameter names if possible (e.g. rgb = thisNf_trial.rgb)
        if thisNf_trial != None:
            for paramName in thisNf_trial:
                exec('{} = thisNf_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "NF_CODE"-------
        continueRoutine = True
        # update component parameters for each repeat
        #assigning baseline word
        nf_WordItem=nf_word_lst[nf_trial]
        nf_WordColor=nf_color_lst[nf_trial]
        nf_video=videoC[nf_trial]
        
        nf_WordType = "undefined"
        if nf_WordItem in food:
            nf_WordType = "food"
        if nf_WordItem in neutral:
            nf_WordType = "neutral"
        
        nf_condition='NF'
        
        #Record variables
        thisExp.addData('wordContent', nf_WordItem)
        thisExp.addData('wordColor', nf_WordColor)
        thisExp.addData('wordType', nf_WordType)
        thisExp.addData('Condition', nf_condition)
        
        #update trial num
        nf_trial+=1
        # keep track of which components have finished
        NF_CODEComponents = []
        for thisComponent in NF_CODEComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        NF_CODEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "NF_CODE"-------
        while continueRoutine:
            # get current time
            t = NF_CODEClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=NF_CODEClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NF_CODEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "NF_CODE"-------
        for thisComponent in NF_CODEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "NF_CODE" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "preloadVideo"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        preloadVideoComponents = [PreloadBackground]
        for thisComponent in preloadVideoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        preloadVideoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "preloadVideo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = preloadVideoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=preloadVideoClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PreloadBackground* updates
            if PreloadBackground.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PreloadBackground.frameNStart = frameN  # exact frame index
                PreloadBackground.tStart = t  # local t and not account for scr refresh
                PreloadBackground.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PreloadBackground, 'tStartRefresh')  # time at next scr refresh
                PreloadBackground.setAutoDraw(True)
            if PreloadBackground.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PreloadBackground.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    PreloadBackground.tStop = t  # not accounting for scr refresh
                    PreloadBackground.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PreloadBackground, 'tStopRefresh')  # time at next scr refresh
                    PreloadBackground.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preloadVideoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "preloadVideo"-------
        for thisComponent in preloadVideoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        nf_trials.addData('PreloadBackground.started', PreloadBackground.tStartRefresh)
        nf_trials.addData('PreloadBackground.stopped', PreloadBackground.tStopRefresh)
        
        # ------Prepare to start Routine "NF_Condition"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        nf_video = visual.MovieStim3(
            win=win, name='nf_video',units='cm', 
            noAudio = True,
            filename=nf_video,
            ori=0.0, pos=(0, 0), opacity=None,
            loop=False,
            size=[28.8,16.2],
            depth=-1.0,
            )
        nf_word.setColor(nf_WordColor, colorSpace='rgb')
        nf_word.setText(nf_WordItem)
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        NF_ConditionComponents = [background8, nf_video, nf_fixation_cross, nf_word, key_resp_4]
        for thisComponent in NF_ConditionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        NF_ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "NF_Condition"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = NF_ConditionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=NF_ConditionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background8* updates
            if background8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background8.frameNStart = frameN  # exact frame index
                background8.tStart = t  # local t and not account for scr refresh
                background8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background8, 'tStartRefresh')  # time at next scr refresh
                background8.setAutoDraw(True)
            if background8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > background8.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    background8.tStop = t  # not accounting for scr refresh
                    background8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(background8, 'tStopRefresh')  # time at next scr refresh
                    background8.setAutoDraw(False)
            
            # *nf_video* updates
            if nf_video.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                nf_video.frameNStart = frameN  # exact frame index
                nf_video.tStart = t  # local t and not account for scr refresh
                nf_video.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nf_video, 'tStartRefresh')  # time at next scr refresh
                nf_video.setAutoDraw(True)
            if nf_video.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > nf_video.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    nf_video.tStop = t  # not accounting for scr refresh
                    nf_video.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(nf_video, 'tStopRefresh')  # time at next scr refresh
                    nf_video.setAutoDraw(False)
            
            # *nf_fixation_cross* updates
            if nf_fixation_cross.status == NOT_STARTED and tThisFlip >= 2.75-frameTolerance:
                # keep track of start time/frame for later
                nf_fixation_cross.frameNStart = frameN  # exact frame index
                nf_fixation_cross.tStart = t  # local t and not account for scr refresh
                nf_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nf_fixation_cross, 'tStartRefresh')  # time at next scr refresh
                nf_fixation_cross.setAutoDraw(True)
            if nf_fixation_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > nf_fixation_cross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    nf_fixation_cross.tStop = t  # not accounting for scr refresh
                    nf_fixation_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(nf_fixation_cross, 'tStopRefresh')  # time at next scr refresh
                    nf_fixation_cross.setAutoDraw(False)
            
            # *nf_word* updates
            if nf_word.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                nf_word.frameNStart = frameN  # exact frame index
                nf_word.tStart = t  # local t and not account for scr refresh
                nf_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nf_word, 'tStartRefresh')  # time at next scr refresh
                nf_word.setAutoDraw(True)
            if nf_word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > nf_word.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    nf_word.tStop = t  # not accounting for scr refresh
                    nf_word.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(nf_word, 'tStopRefresh')  # time at next scr refresh
                    nf_word.setAutoDraw(False)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_4.tStop = t  # not accounting for scr refresh
                    key_resp_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                    key_resp_4.status = FINISHED
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NF_ConditionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "NF_Condition"-------
        for thisComponent in NF_ConditionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        nf_trials.addData('background8.started', background8.tStartRefresh)
        nf_trials.addData('background8.stopped', background8.tStopRefresh)
        nf_video.stop()
        nf_trials.addData('nf_fixation_cross.started', nf_fixation_cross.tStartRefresh)
        nf_trials.addData('nf_fixation_cross.stopped', nf_fixation_cross.tStopRefresh)
        nf_trials.addData('nf_word.started', nf_word.tStartRefresh)
        nf_trials.addData('nf_word.stopped', nf_word.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        nf_trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            nf_trials.addData('key_resp_4.rt', key_resp_4.rt)
        nf_trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        nf_trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nRepC repeats of 'nf_trials'
    
    
    # ------Prepare to start Routine "cdt_num_plus_one"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    cdt_num_plus_oneComponents = []
    for thisComponent in cdt_num_plus_oneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cdt_num_plus_oneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cdt_num_plus_one"-------
    while continueRoutine:
        # get current time
        t = cdt_num_plus_oneClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cdt_num_plus_oneClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cdt_num_plus_oneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cdt_num_plus_one"-------
    for thisComponent in cdt_num_plus_oneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    cdt_num+=1
    # the Routine "cdt_num_plus_one" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "BreakCode"-------
    continueRoutine = True
    # update component parameters for each repeat
    if cdt_num<=2:
        nRepBreak=1
    else:
        nRepBreak=0
    # keep track of which components have finished
    BreakCodeComponents = []
    for thisComponent in BreakCodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BreakCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BreakCode"-------
    while continueRoutine:
        # get current time
        t = BreakCodeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BreakCodeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakCodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BreakCode"-------
    for thisComponent in BreakCodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "BreakCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    whether_break = data.TrialHandler(nReps=nRepBreak, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='whether_break')
    thisExp.addLoop(whether_break)  # add the loop to the experiment
    thisWhether_break = whether_break.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWhether_break.rgb)
    if thisWhether_break != None:
        for paramName in thisWhether_break:
            exec('{} = thisWhether_break[paramName]'.format(paramName))
    
    for thisWhether_break in whether_break:
        currentLoop = whether_break
        # abbreviate parameter names if possible (e.g. rgb = thisWhether_break.rgb)
        if thisWhether_break != None:
            for paramName in thisWhether_break:
                exec('{} = thisWhether_break[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "vasInstruction"-------
        continueRoutine = True
        # update component parameters for each repeat
        proceed_VAS.keys = []
        proceed_VAS.rt = []
        _proceed_VAS_allKeys = []
        # keep track of which components have finished
        vasInstructionComponents = [polygon_3, vasIns, proceed_VAS]
        for thisComponent in vasInstructionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        vasInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "vasInstruction"-------
        while continueRoutine:
            # get current time
            t = vasInstructionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=vasInstructionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_3* updates
            if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_3.frameNStart = frameN  # exact frame index
                polygon_3.tStart = t  # local t and not account for scr refresh
                polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(True)
            
            # *vasIns* updates
            if vasIns.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vasIns.frameNStart = frameN  # exact frame index
                vasIns.tStart = t  # local t and not account for scr refresh
                vasIns.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vasIns, 'tStartRefresh')  # time at next scr refresh
                vasIns.setAutoDraw(True)
            
            # *proceed_VAS* updates
            waitOnFlip = False
            if proceed_VAS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                proceed_VAS.frameNStart = frameN  # exact frame index
                proceed_VAS.tStart = t  # local t and not account for scr refresh
                proceed_VAS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(proceed_VAS, 'tStartRefresh')  # time at next scr refresh
                proceed_VAS.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(proceed_VAS.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(proceed_VAS.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if proceed_VAS.status == STARTED and not waitOnFlip:
                theseKeys = proceed_VAS.getKeys(keyList=['right'], waitRelease=False)
                _proceed_VAS_allKeys.extend(theseKeys)
                if len(_proceed_VAS_allKeys):
                    proceed_VAS.keys = _proceed_VAS_allKeys[-1].name  # just the last key pressed
                    proceed_VAS.rt = _proceed_VAS_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in vasInstructionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "vasInstruction"-------
        for thisComponent in vasInstructionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        whether_break.addData('polygon_3.started', polygon_3.tStartRefresh)
        whether_break.addData('polygon_3.stopped', polygon_3.tStopRefresh)
        whether_break.addData('vasIns.started', vasIns.tStartRefresh)
        whether_break.addData('vasIns.stopped', vasIns.tStopRefresh)
        # check responses
        if proceed_VAS.keys in ['', [], None]:  # No response was made
            proceed_VAS.keys = None
        whether_break.addData('proceed_VAS.keys',proceed_VAS.keys)
        if proceed_VAS.keys != None:  # we had a response
            whether_break.addData('proceed_VAS.rt', proceed_VAS.rt)
        whether_break.addData('proceed_VAS.started', proceed_VAS.tStartRefresh)
        whether_break.addData('proceed_VAS.stopped', proceed_VAS.tStopRefresh)
        # the Routine "vasInstruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "VAS"-------
        continueRoutine = True
        # update component parameters for each repeat
        VAS1.reset()
        VAS2.reset()
        VAS3.reset()
        VAS4.reset()
        VAS5.reset()
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        VASComponents = [polygon_2, VAStext1, VAS1, VAStext2, VAS2, VAStext3, VAS3, VAStext4, VAS4, VAStext5, VAS5, proceed, key_resp_5]
        for thisComponent in VASComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        VASClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "VAS"-------
        while continueRoutine:
            # get current time
            t = VASClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=VASClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_2* updates
            if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(True)
            
            # *VAStext1* updates
            if VAStext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAStext1.frameNStart = frameN  # exact frame index
                VAStext1.tStart = t  # local t and not account for scr refresh
                VAStext1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAStext1, 'tStartRefresh')  # time at next scr refresh
                VAStext1.setAutoDraw(True)
            
            # *VAS1* updates
            if VAS1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAS1.frameNStart = frameN  # exact frame index
                VAS1.tStart = t  # local t and not account for scr refresh
                VAS1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAS1, 'tStartRefresh')  # time at next scr refresh
                VAS1.setAutoDraw(True)
            
            # *VAStext2* updates
            if VAStext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAStext2.frameNStart = frameN  # exact frame index
                VAStext2.tStart = t  # local t and not account for scr refresh
                VAStext2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAStext2, 'tStartRefresh')  # time at next scr refresh
                VAStext2.setAutoDraw(True)
            
            # *VAS2* updates
            if VAS2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAS2.frameNStart = frameN  # exact frame index
                VAS2.tStart = t  # local t and not account for scr refresh
                VAS2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAS2, 'tStartRefresh')  # time at next scr refresh
                VAS2.setAutoDraw(True)
            
            # *VAStext3* updates
            if VAStext3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAStext3.frameNStart = frameN  # exact frame index
                VAStext3.tStart = t  # local t and not account for scr refresh
                VAStext3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAStext3, 'tStartRefresh')  # time at next scr refresh
                VAStext3.setAutoDraw(True)
            
            # *VAS3* updates
            if VAS3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAS3.frameNStart = frameN  # exact frame index
                VAS3.tStart = t  # local t and not account for scr refresh
                VAS3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAS3, 'tStartRefresh')  # time at next scr refresh
                VAS3.setAutoDraw(True)
            
            # *VAStext4* updates
            if VAStext4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAStext4.frameNStart = frameN  # exact frame index
                VAStext4.tStart = t  # local t and not account for scr refresh
                VAStext4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAStext4, 'tStartRefresh')  # time at next scr refresh
                VAStext4.setAutoDraw(True)
            
            # *VAS4* updates
            if VAS4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAS4.frameNStart = frameN  # exact frame index
                VAS4.tStart = t  # local t and not account for scr refresh
                VAS4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAS4, 'tStartRefresh')  # time at next scr refresh
                VAS4.setAutoDraw(True)
            
            # *VAStext5* updates
            if VAStext5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAStext5.frameNStart = frameN  # exact frame index
                VAStext5.tStart = t  # local t and not account for scr refresh
                VAStext5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAStext5, 'tStartRefresh')  # time at next scr refresh
                VAStext5.setAutoDraw(True)
            
            # *VAS5* updates
            if VAS5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                VAS5.frameNStart = frameN  # exact frame index
                VAS5.tStart = t  # local t and not account for scr refresh
                VAS5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(VAS5, 'tStartRefresh')  # time at next scr refresh
                VAS5.setAutoDraw(True)
            
            # *proceed* updates
            if proceed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                proceed.frameNStart = frameN  # exact frame index
                proceed.tStart = t  # local t and not account for scr refresh
                proceed.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(proceed, 'tStartRefresh')  # time at next scr refresh
                proceed.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['right'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VASComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "VAS"-------
        for thisComponent in VASComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        whether_break.addData('polygon_2.started', polygon_2.tStartRefresh)
        whether_break.addData('polygon_2.stopped', polygon_2.tStopRefresh)
        whether_break.addData('VAStext1.started', VAStext1.tStartRefresh)
        whether_break.addData('VAStext1.stopped', VAStext1.tStopRefresh)
        whether_break.addData('VAS1.response', VAS1.getRating())
        whether_break.addData('VAS1.started', VAS1.tStartRefresh)
        whether_break.addData('VAS1.stopped', VAS1.tStopRefresh)
        whether_break.addData('VAStext2.started', VAStext2.tStartRefresh)
        whether_break.addData('VAStext2.stopped', VAStext2.tStopRefresh)
        whether_break.addData('VAS2.response', VAS2.getRating())
        whether_break.addData('VAS2.rt', VAS2.getRT())
        whether_break.addData('VAS2.started', VAS2.tStartRefresh)
        whether_break.addData('VAS2.stopped', VAS2.tStopRefresh)
        whether_break.addData('VAStext3.started', VAStext3.tStartRefresh)
        whether_break.addData('VAStext3.stopped', VAStext3.tStopRefresh)
        whether_break.addData('VAS3.response', VAS3.getRating())
        whether_break.addData('VAS3.rt', VAS3.getRT())
        whether_break.addData('VAS3.started', VAS3.tStartRefresh)
        whether_break.addData('VAS3.stopped', VAS3.tStopRefresh)
        whether_break.addData('VAStext4.started', VAStext4.tStartRefresh)
        whether_break.addData('VAStext4.stopped', VAStext4.tStopRefresh)
        whether_break.addData('VAS4.response', VAS4.getRating())
        whether_break.addData('VAS4.rt', VAS4.getRT())
        whether_break.addData('VAS4.started', VAS4.tStartRefresh)
        whether_break.addData('VAS4.stopped', VAS4.tStopRefresh)
        whether_break.addData('VAStext5.started', VAStext5.tStartRefresh)
        whether_break.addData('VAStext5.stopped', VAStext5.tStopRefresh)
        whether_break.addData('VAS5.response', VAS5.getRating())
        whether_break.addData('VAS5.rt', VAS5.getRT())
        whether_break.addData('VAS5.started', VAS5.tStartRefresh)
        whether_break.addData('VAS5.stopped', VAS5.tStopRefresh)
        whether_break.addData('proceed.started', proceed.tStartRefresh)
        whether_break.addData('proceed.stopped', proceed.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        whether_break.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            whether_break.addData('key_resp_5.rt', key_resp_5.rt)
        whether_break.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        whether_break.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "VAS" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Break"-------
        continueRoutine = True
        routineTimer.add(600.500000)
        # update component parameters for each repeat
        end_break.keys = []
        end_break.rt = []
        _end_break_allKeys = []
        # keep track of which components have finished
        BreakComponents = [background9, Break_text, end_break]
        for thisComponent in BreakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Break"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BreakClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BreakClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background9* updates
            if background9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background9.frameNStart = frameN  # exact frame index
                background9.tStart = t  # local t and not account for scr refresh
                background9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background9, 'tStartRefresh')  # time at next scr refresh
                background9.setAutoDraw(True)
            if background9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > background9.tStartRefresh + 600-frameTolerance:
                    # keep track of stop time/frame for later
                    background9.tStop = t  # not accounting for scr refresh
                    background9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(background9, 'tStopRefresh')  # time at next scr refresh
                    background9.setAutoDraw(False)
            
            # *Break_text* updates
            if Break_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Break_text.frameNStart = frameN  # exact frame index
                Break_text.tStart = t  # local t and not account for scr refresh
                Break_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Break_text, 'tStartRefresh')  # time at next scr refresh
                Break_text.setAutoDraw(True)
            if Break_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Break_text.tStartRefresh + 600-frameTolerance:
                    # keep track of stop time/frame for later
                    Break_text.tStop = t  # not accounting for scr refresh
                    Break_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Break_text, 'tStopRefresh')  # time at next scr refresh
                    Break_text.setAutoDraw(False)
            
            # *end_break* updates
            waitOnFlip = False
            if end_break.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                end_break.frameNStart = frameN  # exact frame index
                end_break.tStart = t  # local t and not account for scr refresh
                end_break.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
                end_break.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if end_break.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > end_break.tStartRefresh + 600-frameTolerance:
                    # keep track of stop time/frame for later
                    end_break.tStop = t  # not accounting for scr refresh
                    end_break.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                    end_break.status = FINISHED
            if end_break.status == STARTED and not waitOnFlip:
                theseKeys = end_break.getKeys(keyList=['right'], waitRelease=False)
                _end_break_allKeys.extend(theseKeys)
                if len(_end_break_allKeys):
                    end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                    end_break.rt = _end_break_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Break"-------
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        whether_break.addData('background9.started', background9.tStartRefresh)
        whether_break.addData('background9.stopped', background9.tStopRefresh)
        whether_break.addData('Break_text.started', Break_text.tStartRefresh)
        whether_break.addData('Break_text.stopped', Break_text.tStopRefresh)
        # check responses
        if end_break.keys in ['', [], None]:  # No response was made
            end_break.keys = None
        whether_break.addData('end_break.keys',end_break.keys)
        if end_break.keys != None:  # we had a response
            whether_break.addData('end_break.rt', end_break.rt)
        whether_break.addData('end_break.started', end_break.tStartRefresh)
        whether_break.addData('end_break.stopped', end_break.tStopRefresh)
        
        # ------Prepare to start Routine "Remainder"-------
        continueRoutine = True
        # update component parameters for each repeat
        proceed_to_next_condition.keys = []
        proceed_to_next_condition.rt = []
        _proceed_to_next_condition_allKeys = []
        # keep track of which components have finished
        RemainderComponents = [background10, stroop_remainder, proceed_to_next_condition]
        for thisComponent in RemainderComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RemainderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Remainder"-------
        while continueRoutine:
            # get current time
            t = RemainderClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RemainderClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background10* updates
            if background10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background10.frameNStart = frameN  # exact frame index
                background10.tStart = t  # local t and not account for scr refresh
                background10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background10, 'tStartRefresh')  # time at next scr refresh
                background10.setAutoDraw(True)
            
            # *stroop_remainder* updates
            if stroop_remainder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stroop_remainder.frameNStart = frameN  # exact frame index
                stroop_remainder.tStart = t  # local t and not account for scr refresh
                stroop_remainder.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop_remainder, 'tStartRefresh')  # time at next scr refresh
                stroop_remainder.setAutoDraw(True)
            
            # *proceed_to_next_condition* updates
            waitOnFlip = False
            if proceed_to_next_condition.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                proceed_to_next_condition.frameNStart = frameN  # exact frame index
                proceed_to_next_condition.tStart = t  # local t and not account for scr refresh
                proceed_to_next_condition.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(proceed_to_next_condition, 'tStartRefresh')  # time at next scr refresh
                proceed_to_next_condition.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(proceed_to_next_condition.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(proceed_to_next_condition.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if proceed_to_next_condition.status == STARTED and not waitOnFlip:
                theseKeys = proceed_to_next_condition.getKeys(keyList=['right'], waitRelease=False)
                _proceed_to_next_condition_allKeys.extend(theseKeys)
                if len(_proceed_to_next_condition_allKeys):
                    proceed_to_next_condition.keys = _proceed_to_next_condition_allKeys[-1].name  # just the last key pressed
                    proceed_to_next_condition.rt = _proceed_to_next_condition_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RemainderComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Remainder"-------
        for thisComponent in RemainderComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        whether_break.addData('background10.started', background10.tStartRefresh)
        whether_break.addData('background10.stopped', background10.tStopRefresh)
        whether_break.addData('stroop_remainder.started', stroop_remainder.tStartRefresh)
        whether_break.addData('stroop_remainder.stopped', stroop_remainder.tStopRefresh)
        # check responses
        if proceed_to_next_condition.keys in ['', [], None]:  # No response was made
            proceed_to_next_condition.keys = None
        whether_break.addData('proceed_to_next_condition.keys',proceed_to_next_condition.keys)
        if proceed_to_next_condition.keys != None:  # we had a response
            whether_break.addData('proceed_to_next_condition.rt', proceed_to_next_condition.rt)
        whether_break.addData('proceed_to_next_condition.started', proceed_to_next_condition.tStartRefresh)
        whether_break.addData('proceed_to_next_condition.stopped', proceed_to_next_condition.tStopRefresh)
        # the Routine "Remainder" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepBreak repeats of 'whether_break'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'loop_for_ct_balance'


# ------Prepare to start Routine "vasInstruction"-------
continueRoutine = True
# update component parameters for each repeat
proceed_VAS.keys = []
proceed_VAS.rt = []
_proceed_VAS_allKeys = []
# keep track of which components have finished
vasInstructionComponents = [polygon_3, vasIns, proceed_VAS]
for thisComponent in vasInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
vasInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "vasInstruction"-------
while continueRoutine:
    # get current time
    t = vasInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=vasInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *vasIns* updates
    if vasIns.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vasIns.frameNStart = frameN  # exact frame index
        vasIns.tStart = t  # local t and not account for scr refresh
        vasIns.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vasIns, 'tStartRefresh')  # time at next scr refresh
        vasIns.setAutoDraw(True)
    
    # *proceed_VAS* updates
    waitOnFlip = False
    if proceed_VAS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceed_VAS.frameNStart = frameN  # exact frame index
        proceed_VAS.tStart = t  # local t and not account for scr refresh
        proceed_VAS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed_VAS, 'tStartRefresh')  # time at next scr refresh
        proceed_VAS.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed_VAS.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed_VAS.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed_VAS.status == STARTED and not waitOnFlip:
        theseKeys = proceed_VAS.getKeys(keyList=['right'], waitRelease=False)
        _proceed_VAS_allKeys.extend(theseKeys)
        if len(_proceed_VAS_allKeys):
            proceed_VAS.keys = _proceed_VAS_allKeys[-1].name  # just the last key pressed
            proceed_VAS.rt = _proceed_VAS_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vasInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "vasInstruction"-------
for thisComponent in vasInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('vasIns.started', vasIns.tStartRefresh)
thisExp.addData('vasIns.stopped', vasIns.tStopRefresh)
# check responses
if proceed_VAS.keys in ['', [], None]:  # No response was made
    proceed_VAS.keys = None
thisExp.addData('proceed_VAS.keys',proceed_VAS.keys)
if proceed_VAS.keys != None:  # we had a response
    thisExp.addData('proceed_VAS.rt', proceed_VAS.rt)
thisExp.addData('proceed_VAS.started', proceed_VAS.tStartRefresh)
thisExp.addData('proceed_VAS.stopped', proceed_VAS.tStopRefresh)
thisExp.nextEntry()
# the Routine "vasInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VAS"-------
continueRoutine = True
# update component parameters for each repeat
VAS1.reset()
VAS2.reset()
VAS3.reset()
VAS4.reset()
VAS5.reset()
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
VASComponents = [polygon_2, VAStext1, VAS1, VAStext2, VAS2, VAStext3, VAS3, VAStext4, VAS4, VAStext5, VAS5, proceed, key_resp_5]
for thisComponent in VASComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VASClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VAS"-------
while continueRoutine:
    # get current time
    t = VASClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VASClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    
    # *VAStext1* updates
    if VAStext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext1.frameNStart = frameN  # exact frame index
        VAStext1.tStart = t  # local t and not account for scr refresh
        VAStext1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext1, 'tStartRefresh')  # time at next scr refresh
        VAStext1.setAutoDraw(True)
    
    # *VAS1* updates
    if VAS1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS1.frameNStart = frameN  # exact frame index
        VAS1.tStart = t  # local t and not account for scr refresh
        VAS1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS1, 'tStartRefresh')  # time at next scr refresh
        VAS1.setAutoDraw(True)
    
    # *VAStext2* updates
    if VAStext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext2.frameNStart = frameN  # exact frame index
        VAStext2.tStart = t  # local t and not account for scr refresh
        VAStext2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext2, 'tStartRefresh')  # time at next scr refresh
        VAStext2.setAutoDraw(True)
    
    # *VAS2* updates
    if VAS2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS2.frameNStart = frameN  # exact frame index
        VAS2.tStart = t  # local t and not account for scr refresh
        VAS2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS2, 'tStartRefresh')  # time at next scr refresh
        VAS2.setAutoDraw(True)
    
    # *VAStext3* updates
    if VAStext3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext3.frameNStart = frameN  # exact frame index
        VAStext3.tStart = t  # local t and not account for scr refresh
        VAStext3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext3, 'tStartRefresh')  # time at next scr refresh
        VAStext3.setAutoDraw(True)
    
    # *VAS3* updates
    if VAS3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS3.frameNStart = frameN  # exact frame index
        VAS3.tStart = t  # local t and not account for scr refresh
        VAS3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS3, 'tStartRefresh')  # time at next scr refresh
        VAS3.setAutoDraw(True)
    
    # *VAStext4* updates
    if VAStext4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext4.frameNStart = frameN  # exact frame index
        VAStext4.tStart = t  # local t and not account for scr refresh
        VAStext4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext4, 'tStartRefresh')  # time at next scr refresh
        VAStext4.setAutoDraw(True)
    
    # *VAS4* updates
    if VAS4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS4.frameNStart = frameN  # exact frame index
        VAS4.tStart = t  # local t and not account for scr refresh
        VAS4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS4, 'tStartRefresh')  # time at next scr refresh
        VAS4.setAutoDraw(True)
    
    # *VAStext5* updates
    if VAStext5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAStext5.frameNStart = frameN  # exact frame index
        VAStext5.tStart = t  # local t and not account for scr refresh
        VAStext5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAStext5, 'tStartRefresh')  # time at next scr refresh
        VAStext5.setAutoDraw(True)
    
    # *VAS5* updates
    if VAS5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VAS5.frameNStart = frameN  # exact frame index
        VAS5.tStart = t  # local t and not account for scr refresh
        VAS5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VAS5, 'tStartRefresh')  # time at next scr refresh
        VAS5.setAutoDraw(True)
    
    # *proceed* updates
    if proceed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceed.frameNStart = frameN  # exact frame index
        proceed.tStart = t  # local t and not account for scr refresh
        proceed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed, 'tStartRefresh')  # time at next scr refresh
        proceed.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VASComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VAS"-------
for thisComponent in VASComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('VAStext1.started', VAStext1.tStartRefresh)
thisExp.addData('VAStext1.stopped', VAStext1.tStopRefresh)
thisExp.addData('VAS1.response', VAS1.getRating())
thisExp.addData('VAS1.started', VAS1.tStartRefresh)
thisExp.addData('VAS1.stopped', VAS1.tStopRefresh)
thisExp.addData('VAStext2.started', VAStext2.tStartRefresh)
thisExp.addData('VAStext2.stopped', VAStext2.tStopRefresh)
thisExp.addData('VAS2.response', VAS2.getRating())
thisExp.addData('VAS2.rt', VAS2.getRT())
thisExp.addData('VAS2.started', VAS2.tStartRefresh)
thisExp.addData('VAS2.stopped', VAS2.tStopRefresh)
thisExp.addData('VAStext3.started', VAStext3.tStartRefresh)
thisExp.addData('VAStext3.stopped', VAStext3.tStopRefresh)
thisExp.addData('VAS3.response', VAS3.getRating())
thisExp.addData('VAS3.rt', VAS3.getRT())
thisExp.addData('VAS3.started', VAS3.tStartRefresh)
thisExp.addData('VAS3.stopped', VAS3.tStopRefresh)
thisExp.addData('VAStext4.started', VAStext4.tStartRefresh)
thisExp.addData('VAStext4.stopped', VAStext4.tStopRefresh)
thisExp.addData('VAS4.response', VAS4.getRating())
thisExp.addData('VAS4.rt', VAS4.getRT())
thisExp.addData('VAS4.started', VAS4.tStartRefresh)
thisExp.addData('VAS4.stopped', VAS4.tStopRefresh)
thisExp.addData('VAStext5.started', VAStext5.tStartRefresh)
thisExp.addData('VAStext5.stopped', VAStext5.tStopRefresh)
thisExp.addData('VAS5.response', VAS5.getRating())
thisExp.addData('VAS5.rt', VAS5.getRT())
thisExp.addData('VAS5.started', VAS5.tStartRefresh)
thisExp.addData('VAS5.stopped', VAS5.tStopRefresh)
thisExp.addData('proceed.started', proceed.tStartRefresh)
thisExp.addData('proceed.stopped', proceed.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "VAS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "completionScreen"-------
continueRoutine = True
# update component parameters for each repeat
end_key.keys = []
end_key.rt = []
_end_key_allKeys = []
# keep track of which components have finished
completionScreenComponents = [background11, text, end_key]
for thisComponent in completionScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
completionScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "completionScreen"-------
while continueRoutine:
    # get current time
    t = completionScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=completionScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background11* updates
    if background11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background11.frameNStart = frameN  # exact frame index
        background11.tStart = t  # local t and not account for scr refresh
        background11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background11, 'tStartRefresh')  # time at next scr refresh
        background11.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *end_key* updates
    waitOnFlip = False
    if end_key.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        end_key.frameNStart = frameN  # exact frame index
        end_key.tStart = t  # local t and not account for scr refresh
        end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key, 'tStartRefresh')  # time at next scr refresh
        end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key.status == STARTED and not waitOnFlip:
        theseKeys = end_key.getKeys(keyList=['space'], waitRelease=False)
        _end_key_allKeys.extend(theseKeys)
        if len(_end_key_allKeys):
            end_key.keys = _end_key_allKeys[-1].name  # just the last key pressed
            end_key.rt = _end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in completionScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "completionScreen"-------
for thisComponent in completionScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('background11.started', background11.tStartRefresh)
thisExp.addData('background11.stopped', background11.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if end_key.keys in ['', [], None]:  # No response was made
    end_key.keys = None
thisExp.addData('end_key.keys',end_key.keys)
if end_key.keys != None:  # we had a response
    thisExp.addData('end_key.rt', end_key.rt)
thisExp.addData('end_key.started', end_key.tStartRefresh)
thisExp.addData('end_key.stopped', end_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "completionScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
