#Ben Pygame Code (For Storage)

from turtle import width
import pygame
from pygame.locals import *

import yfinance as yf

import random

import matplotlib.pyplot as plt

import matplotlib
matplotlib.use ("Agg")

import matplotlib.backends.backend_agg as agg

import pylab

import pandas as pd

# Import Stock Codes
column_names = ["codes"]
df = pd.read_csv (r'D:\Computer Science\Personal Projects\ABCemn\StockCodes - Sheet1.csv', names = column_names)
print (df)
Stock_Codes = df.codes.to_list()
print (Stock_Codes)

# Cam Graph Code

def getData (code, period, interval) :

    try :
        df = yf.download (code, period = period, interval = interval)
        missing = list (yf.shared._ERRORS.keys ())
        print (missing)
    except Exception as e :
        print ("Couldn't download stock info :(") 
    return df
#normalize data between min max

def nextGraph () :
    stock = random.choice (Stock_Codes)
    data = getData (stock,'1mo','1h')
    curRow = 0
    batchSize = 60
    #while fix while to end when out of data
    curData = data [curRow : (curRow + batchSize)]
    #plt.plot (curData ['Close'])
    fig = pylab.figure (figsize = [8, 4], dpi = 100)
    ax = fig.gca ()
    ax.plot (curData ['Close'])
    global canvas
    canvas = agg.FigureCanvasAgg (fig)
    canvas.draw ()
    renderer = canvas.get_renderer ()
    global raw_data
    raw_data = renderer.tostring_rgb ()

# initializing the constructor
pygame.init ()
  
# screen resolution
res = (1200, 900)

# opens up a window
screen = pygame.display.set_mode(res)

#button colors

colorBuy = ("#FF312E")
colorSell = ("#20A4F3")
colorStay = ("#E2E4F6")
colorBackground = ("#6B654B")
colorBorders = ("#040403")

print ("Made Colors")

# stores the width of the
# screen into a variable
widthS = screen.get_width()
  
# stores the height of the
# screen into a variable
heightS = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Times New Roman',35)

print ("Made Font")

# rendering a text written in
# this font
textBuy = smallfont.render ('Buy' , True , colorBorders)
textSell = smallfont.render ('Sell' , True , colorBorders)
textStay = smallfont.render ('Stay' , True , colorBorders)

textBuyDark = smallfont.render ('Buy', True, colorStay)
textSellDark = smallfont.render ('Sell', True, colorStay)
textStayDark = smallfont.render ('Stay', True, colorStay)

print ("Made Text")

count = 0

print ("Start Game")
print ("\n----------------------------------------------------\n")

run = True

nextGraph ()

while run :
    
    for ev in pygame.event.get () :

        # fills the screen with a color
        screen.fill (colorBackground)
        
        # Quit Condition
        if ev.type == pygame.QUIT :
            print ("\n----------------------------------------------------\n")
            print ("Transactions Complete. Goodbye Now.\n")
            run = False
            pygame.quit ()
            break

        # Quit After Five
        if count == 5 :
            print ("\n----------------------------------------------------\n")
            print ("Transactions Complete. Goodbye Now.\n")
            run = False
            pygame.quit ()
            break


        # Quit Button
        if ev.type == pygame.MOUSEBUTTONDOWN :
            if widthS / 32 <= mouse [0] <= widthS / 32 + 50 and heightS / 32 <= mouse [1] <= heightS / 32 + 50 :
                print ("quit")
                run = False
                pygame.quit ()
                break


        # Stay Event
        if ev.type == pygame.MOUSEBUTTONDOWN :
            if widthS / 2 - 50 <= mouse [0] <= widthS / 2 + 50 and heightS * .9 <= mouse [1] <= heightS * .9 + 40 :
                print ("Stay")
                nextGraph ()
                count += 1

        # Sell Event
        if ev.type == pygame.MOUSEBUTTONDOWN :
            if widthS / 4 - 50 <= mouse [0] <= widthS / 4 + 50 and heightS * .9 <= mouse [1] <= heightS * .9 + 40 :
                print ("Sell Stocks")
                nextGraph ()
                count += 1

        # Buy Event
        if ev.type == pygame.MOUSEBUTTONDOWN :
            if widthS * .75 - 50 <= mouse [0] <= widthS * .75 + 50 and heightS * .9 <= mouse [1] <= heightS * .9 + 40 :
                print ("Buy Stocks")
                nextGraph ()
                count += 1
       
        # stores the (x,y) coordinates into
        # the variable as a tupl
        mouse = pygame.mouse.get_pos ()

        # Quit Button
        if widthS / 32 <= mouse [0] <= widthS / 32 + 50 and heightS / 32 <= mouse [1] <= heightS / 32 + 50 :
            pygame.draw.rect (screen, colorStay, [widthS / 32, heightS / 32, 50, 50])
            
        else :
            pygame.draw.rect (screen, colorBorders, [widthS / 32, heightS / 32, 50, 50])

        # Sell Button
        if widthS / 4 - 50 <= mouse [0] <= widthS / 4 + 50 and heightS * .9 <= mouse [1] <= heightS * .9 + 40 :
            pygame.draw.rect (screen, colorBorders, [widthS / 4 - 50, heightS * .9, 100, 40])
            screen.blit (textSellDark, (widthS / 4 - 25, heightS * .9))
            
        else :
            pygame.draw.rect (screen, colorSell, [widthS / 4 - 50, heightS * .9, 100, 40])  
            screen.blit (textSell , (widthS / 4 - 25, heightS * .9))

        # Stay Button
        if widthS / 2 - 50 <= mouse [0] <= widthS / 2 + 50 and heightS * .9 <= mouse [1] <= heightS * .9 + 40 :
            pygame.draw.rect (screen, colorBorders, [widthS / 2 - 50, heightS * .9, 100, 40])
            screen.blit (textStayDark, (widthS / 2 - 25, heightS * .9))
            
        else :
            pygame.draw.rect (screen, colorStay, [widthS / 2 - 50, heightS * .9, 100, 40])
            screen.blit (textStay, (widthS / 2 - 25, heightS * .9))

        #Buy Button
        if widthS * .75 - 50 <= mouse [0] <= widthS * .75 + 50 and heightS * .9 <= mouse [1] <= heightS * .9 + 40 :
            pygame.draw.rect (screen, colorBorders, [widthS * .75 - 50, heightS * .9, 100, 40])
            screen.blit (textBuyDark, (widthS * .75 - 25, heightS * .9))        
        else :
            pygame.draw.rect (screen, colorBuy, [widthS * .75 - 50, heightS * .9, 100, 40])
            screen.blit (textBuy, (widthS * .75 - 25, heightS * .9))

        # Graph
        #window = pygame.display.set_mode ((400, 400), DOUBLEBUF)
        screen = pygame.display.get_surface ()

        size = canvas.get_width_height ()

        surf = pygame.image.fromstring (raw_data, size, "RGB")
        screen.blit (surf, ((widthS / 2) - 400, (heightS / 2) - 200))
        
        # updates the frames of the game
        pygame.display.update ()
