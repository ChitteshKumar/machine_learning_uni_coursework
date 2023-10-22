#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 14:58:58 2021

@author: chittesh
"""

import turtle
import tkinter as tk


import random
from random import randint 
import turtle
import math
from tkinter import *
from functools import partial
import tkinter.font as font
# import sys    
                
       
 
def Name(name_open):
    name_open.destroy()
    name_open=Tk()
    name_open.geometry("400X400")
    name_open.title("Menu")
    

def startgame(initialise_game):
    initialise_game.destroy()  
    images_to_load=["treasure.gif","main_character.gif","main_character_left.gif","main_character_right.gif", "enemy_right.gif", "wall1.gif","enemy_left.gif","main.gif"]
    for image in images_to_load:
        turtle.register_shape(image)


    wn= turtle.Screen()
    wn.bgcolor("#0a424c")
    wn.title("DOO-MAAAAZZEEEE!!")
    wn.setup(1920,1080)  #Screen Resolution=1920x1080
    wn.tracer(0)


    class Table(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            self.speed(0)
            
            
    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            #self.shape('square')
            self.shape("main.gif") 
            self.color("yellow")
            self.penup()
            self.speed(0)
            self.gold = 0
            
        def go_up(self):
            mov_to_x = self.xcor()
            mov_to_y = self.ycor() + 24 
            self.shape("main.gif")
            if (mov_to_x,mov_to_y) not in walls:
                self.goto(mov_to_x, mov_to_y)
            
        def go_down(self):
            mov_to_x = self.xcor()
            mov_to_y = self.ycor() - 24 
            self.shape("main.gif")
            if (mov_to_x,mov_to_y) not in walls:
                self.goto(mov_to_x, mov_to_y)

        def go_right(self):
            mov_to_x = self.xcor() + 24
            mov_to_y = self.ycor() 
            self.shape("main_character_right.gif")
            
            if (mov_to_x,mov_to_y) not in walls:
                self.goto(mov_to_x, mov_to_y)

        def go_left(self):
            mov_to_x = self.xcor() - 24
            mov_to_y = self.ycor() 
            self.shape("main_character_left.gif")
            
            if (mov_to_x,mov_to_y) not in walls:
                self.goto(mov_to_x, mov_to_y)
                
        def collision_object(self, other):
            a=self.xcor()-other.xcor()
            b=self.ycor()-other.ycor()
            distance = math.sqrt((a**2)+(b**2))
            if distance==0:
                return True
            else:
                return False

    class Treasure(turtle.Turtle):
        def __init__(self, x,y):
            turtle.Turtle.__init__(self)
            #self.shape("circle")
            self.shape("treasure.gif")
            #self.shapesize(stretch_wid=24,stretch_len=24,outline=3)
            self.color("gold")
            #self.pencolor("red")
            self.penup()
            self.speed(0)
            self.gold=100     #scoring mechanism 
            self.goto(x,y)
            print(x,y)
        def destroy(self):
            self.goto(2000,2000)
            self.hideturtle()
         
    class Enemy(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("enemy_right.gif")
            self.color("red")
            self.penup()
            self.speed(0)
            self.gold= 25
            self.goto(x,y)
            self.direction = random.choice(['up','down','left','right'])
        def move(self):
            if self.direction == 'up':
                dx =0
                dy=24
            elif self.direction == 'down':
                dx =0
                dy=-24
            elif self.direction == 'left':
                dx=-24
                dy=0
                self.shape("enemy_left.gif")
            elif self.direction == 'right':
                dx=24
                dy=0
                self.shape("enemy_right.gif")
            else:
                dx=0
                dy=0

            if self.is_close(player):
                if player.xcor() < self.xcor():
                    self.direction="left"
                elif player.xcor() > self.xcor():
                    self.direction="right"
                elif player.ycor() < self.ycor():
                    self.direction="down"
                elif player.ycor() > self.ycor():
                    self.direction="up"

            
            mov_to_x=self.xcor()+dx
            mov_to_y=self.ycor()+dy
            
            if (mov_to_x,mov_to_y) not in walls:
                self.goto(mov_to_x, mov_to_y )
            else:
                self.direction= random.choice(['up','down','left','right'])
            turtle.ontimer(self.move, t=random.randint(100,300))

        
        def is_close(self,other):
            a=self.xcor()-other.xcor()
            b=self.ycor()-other.ycor()
            distance=math.sqrt((a**2)+(b**2))

            if distance<75:
                return True
            else:
                return False


        def destroy(self):
            self.goto(2000,2000)
            self.hideturtle()        
         
            
    levels=[""]

    level1=[
    '#########################', 
    '##P #####T     ##########',
    '##  ## #####          E##',
    '##  ########  ###########',
    '##      A###  ### ### ###',
    '##  ######## E### ### ###',
    '##  ###A      ### ### T##',
    '##  ########  ###A###  ##',
    '##  ### T###  ### ### ###',
    '##  ###  ###  ### ### ###',
    '## E###  ###  ### ### ###',
    '##             ## ### ###',
    '##  #########    E    ###',
    '##  ### #####    ########',
    '####### ######   #A    ##',
    '####### ######  E##### ##',
    '##  ###   A###   ##### ##',
    '##  ##########   ##### ##',
    '## E##########   ##### ##',
    '##  #####   E    ##### ##',
    '##  ##########   ##### ##',
    '##      ######      E  ##',
    '##  ##########    ## ####',
    '###       T       ## ####',
    '#########################',  
    ]



    levels.append(level1)

    treasures=[]

    def setup_maze(level):
        for y in range(len(level)):
            for x in range (len(level[y])):
                character = level[y][x]
                screen_x= -288 + (x*24)
                screen_y= 288 - (y*24)
                
                if character == "#":
                    table.goto(screen_x,screen_y)
                    table.shape("wall1.gif")
                    table.stamp()
                    walls.append((screen_x,screen_y))
                    
                if character == "P":
                    player.goto(screen_x, screen_y)
                    
                if character == "T":
                    treasures.append(Treasure(screen_x,screen_y))
                    
                if character == "A":
                    
                    treasures.append(Treasure(screen_x,screen_y))
                
                    
                if character == "E":
                    enemies.append(Enemy(screen_x,screen_y))
            #=len(treasures)
            #b=random.randint(-a,a)

    table=Table()
    player=Player()
    enemies = []

    walls=[]

    setup_maze(levels[1])

    turtle.listen()
    turtle.onkey(player.go_left, "Left")
    turtle.onkey(player.go_right, "Right")
    turtle.onkey(player.go_up, "Up")
    turtle.onkey(player.go_down, "Down")
    #turtle.onkey(,"s")

    for enemy in enemies:
        turtle.ontimer(enemy.move, t=250)


    x=0
    while True:
        for treasure in treasures:
            if player.collision_object(treasure):
                player.gold+= treasure.gold
                print("Player Gold: {}".format(player.gold))
                treasure.destroy()
                treasures.remove(treasure)
                score_pen = turtle.Turtle()
                score_pen.speed(0)
                score_pen.color("white")
                score_pen.penup()
                score_pen.setposition(-290, 310)
                scorestring = "Score %s" %player.gold
                score_pen.write(scorestring, False, align="left", font=("Arial",25,"italic"))
                score_pen.hideturtle()

        for enemy in enemies:
            if player.collision_object(enemy):
                print("Player dies!")
                x=x+1

        if x==5:
            wn.bye()
            dead=Tk()
            dead.title("Game Lost!")
            home_go=partial(menu)
            dead.geometry("600x200")
            canvas=Canvas(dead, width=600, height=200)
            canvas.pack()
            img = PhotoImage(file="game_over.png")      
            canvas.create_image(25,25, anchor=NW, image=img)  
            dead.mainloop()
        wn.update()
        




def sel():
    selection=[]
    select="you selected set "+str(var.get())
    selection.append(select)
    for i in range(len(selection)):
        label.config(text=selection[i])
        label.pack()
    
def controls(changecon):
    changecon.destroy()
    changecon=Tk()
    global var
    var=IntVar()
    changecon.title("Controls")
    r1=Radiobutton(changecon,fg="blue",text="Option-1\n W,A,S,D",variable=var,value=1,command=sel, width=24, height=14)
    r2=Radiobutton(changecon,fg="blue",text="Option-2\n Arrow Keys",value=2,variable=var,command=sel,width=24, height=14)
    r1.pack(anchor=W)
    r2.pack(anchor=W)
    global label
    label=Label(changecon)
   
def Settings(opensett):
    opensett.destroy()
    opensett=Tk()
    opensett.title("Menu")
    cc=partial(controls,opensett)
    # opensett.geometry("400x400")
    bgchange=Button(opensett,text="Change Background",width=30,height=3,fg="blue",activeforeground="orange")
    lead=Button(opensett,text="Leaderboard",width=30,height=3,bg="orange",fg="blue")
    cont=Button(opensett,text="Controls",width=30,height=3,bg="orange",fg="blue",command=cc)
    #controlls
    lead.pack()
    bgchange.pack()
    cont.pack() 
        
    #exit the game/window
def Exit(openexit):
    openexit.destroy()
#Main menu
def menu():
    window=Tk()
    window.title("test")
    window.geometry("450x330")
    start=partial(startgame,window)
    settings=partial(Settings,window)
    name=partial(Name,window)
    exitt=partial(Exit,window)
    name=Button(window,text="CHAKRAVYU",command="name",activeforeground = 'orange'
                ,activebackground = "black",
                fg = "white",bg="#fbf9f6",width = 50,state=DISABLED,height=3,font = "Arial 20", bd = None)
    name.pack()
    play = Button(window, text = "Start", command=start,
                activeforeground = 'red', 
                activebackground = "yellow", bg = "orange", 
                fg = "blue", width = 50,height=2, font = 'Arial 16', bd = 4) 
    play.pack(side="top")
    sett = Button(window, text = "Settings", command=settings,
                activeforeground = 'red', 
                activebackground = "yellow", bg = "orange", 
                fg = "blue", width = 50,height=2,font = 'Arial 16', bd = 4) 
    sett.pack(side="top")
    exitt = Button(window, text = "Quit", command=exitt,
                activeforeground = 'red', 
                activebackground = "yellow", bg = "orange", 
                fg = "blue", width = 50,height=2, font = 'Arial 16', bd = 4) 
    exitt.pack(side="top")
    
    button=Button()
    # canvas=Canvas(window,width=400,height=400,bg="#28363D")
    # canvas.pack()
    window.mainloop()
global bgcol
bgcol="#051e3e"    
     

if __name__=="__main__"   :
    menu()


            
