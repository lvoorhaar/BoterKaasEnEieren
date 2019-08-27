# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:15:33 2019

@author: Lenny
"""

import tkinter as tk
from tkinter.messagebox import askokcancel
import random

##FUNCTIONS##

def Click(button): #Actie wanneer er op een knop geklikt wordt
    letter = current_letter.get()
    button["text"] = letter
    button["state"] = tk.DISABLED
    if check_if_won(letter):
        game_won()
    elif check_if_draw():
        draw()
    else:
        current_letter.change()
        bottom_message.set("Klik op een leeg vakje om een " + current_letter.get() + " te plaatsen.")
        bottom_text["text"] = bottom_message.get()

def Click1():
    Click(button1)

def Click2():
    Click(button2)

def Click3():
    Click(button3)

def Click4():
    Click(button4)

def Click5():
    Click(button5)

def Click6():
    Click(button6)

def Click7():
    Click(button7)

def Click8():
    Click(button8)

def Click9():
    Click(button9)
    
def check_if_won(letter): #Kijkt of een speler heeft gewonnen
    if button1["text"] == letter and button2["text"] == letter and button3["text"] == letter:
        return True
    elif button4["text"] == letter and button5["text"] == letter and button6["text"] == letter:
        return True
    elif button7["text"] == letter and button8["text"] == letter and button9["text"] == letter:
        return True
    elif button1["text"] == letter and button4["text"] == letter and button7["text"] == letter:
        return True
    elif button2["text"] == letter and button5["text"] == letter and button8["text"] == letter:
        return True
    elif button3["text"] == letter and button6["text"] == letter and button9["text"] == letter:
        return True
    elif button1["text"] == letter and button5["text"] == letter and button9["text"] == letter:
        return True
    elif button3["text"] == letter and button5["text"] == letter and button7["text"] == letter:
        return True
    else:
        return False

def game_won(): #Geeft de winnende speler 3 punten
    bottom_message.set("Het spel is afgelopen. Speler " + current_letter.get() + " heeft gewonnen.")
    bottom_text["text"] = bottom_message.get()
    if current_letter.get() == "X":
        score.increase_score_x(3)
    elif current_letter.get() == "O":
        score.increase_score_o(3)
    score_text["text"] = score.text()
    disable_buttons()
    start_new_game()

def check_if_draw(): #Kijkt of er gelijkspel is
    if check_if_won("X") == True or check_if_won("O") == True:
        return False
    elif button1["text"] == "" or button2["text"] == "" or button3["text"] == "" \
    or button4["text"] == "" or button5["text"] == "" or button6["text"] == "" or \
    button7["text"] == "" or button8["text"] == "" or button9["text"] == "":
        return False
    return True

def draw(): #Geeft beide spelers een punt bij gelijkspel
    bottom_message.set("Het spel is geëindigd in gelijkspel.")
    bottom_text["text"] = bottom_message.get()
    score.increase_score_x(1)
    score.increase_score_o(1)
    score_text["text"] = score.text()
    disable_buttons()
    start_new_game()
    
def disable_buttons(): #Deactiveert de knoppen
    button1["state"] = tk.DISABLED
    button2["state"] = tk.DISABLED
    button3["state"] = tk.DISABLED
    button4["state"] = tk.DISABLED
    button5["state"] = tk.DISABLED
    button6["state"] = tk.DISABLED
    button7["state"] = tk.DISABLED
    button8["state"] = tk.DISABLED
    button9["state"] = tk.DISABLED
    
def reset_buttons(): #Knoppen resetten voor een nieuw spel
    button1["state"] = tk.NORMAL
    button1["text"] = ""
    button2["state"] = tk.NORMAL
    button2["text"] = ""
    button3["state"] = tk.NORMAL
    button3["text"] = ""
    button4["state"] = tk.NORMAL
    button4["text"] = ""
    button5["state"] = tk.NORMAL
    button5["text"] = ""
    button6["state"] = tk.NORMAL
    button6["text"] = ""
    button7["state"] = tk.NORMAL
    button7["text"] = ""
    button8["state"] = tk.NORMAL
    button8["text"] = ""
    button9["state"] = tk.NORMAL
    button9["text"] = ""
    
def popup_button(): #Vraagt of een nieuw spel gestart moet worden
    if askokcancel("Spel afgelopen", "Wil je een nieuw spel starten?"):
        return True

def start_new_game(): #Start een nieuw spel
    if popup_button() == True:
        reset_buttons()
        current_letter.reset_new_game()
        bottom_message.set("Speler " + current_letter.get() + " begint. Klik op een leeg vakje om een " \
                         + current_letter.get() + " te plaatsen.")
        bottom_text["text"] = bottom_message.get()
    
##CLASSES##
class Current_letter(object): #Welke speler aan de beurt is
    
    def __init__(self):
        self.reset_new_game()
    
    def get(self):
        return self.letter
    
    def change(self):
        if self.get() == "X":
            self.letter = "O"
        else:
            self.letter = "X"
            
    def reset_new_game(self): #Kiest een willekeurige speler om een nieuw spel te beginnen
        if random.randrange(0, 2) == 0:
            self.letter = "X"
        else:
            self.letter = "O"

class Bottom_message(object): #Tekst die onder in beeld staat
    
    def __init__(self, text):
        self.text = text
        
    def get(self):
        return self.text
    
    def set(self, new_text):
        self.text = new_text

class Scoreboard(object): #Houdt de score van beide spelers bij
    
    def __init__(self):
        self.score_x = 0
        self.score_o = 0
    
    def get_score_x(self):
        return str(self.score_x)
    
    def increase_score_x(self, number):
        self.score_x += number

    def get_score_o(self):
        return str(self.score_o)
    
    def increase_score_o(self, number):
        self.score_o += number
        
    def text(self):
        return "Score speler X: " + score.get_score_x() + "\nScore speler O: " + score.get_score_o()

##MAIN CODE##
current_letter = Current_letter()
score = Scoreboard()
bottom_message = Bottom_message("Speler " + current_letter.get() + " begint. Klik op een leeg vakje om een " \
                         + current_letter.get() + " te plaatsen.")

root = tk.Tk()
root.title("Boter, kaas en eieren")
frame = tk.Frame(root)
frame.grid()

button1 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click1, state=tk.NORMAL)
button1.grid(row=1,column=0)
button2 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click2, state=tk.NORMAL)
button2.grid(row=1,column=1)
button3 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click3, state=tk.NORMAL)
button3.grid(row=1,column=2)
button4 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click4, state=tk.NORMAL)
button4.grid(row=2,column=0)
button5 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click5, state=tk.NORMAL)
button5.grid(row=2,column=1)
button6 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click6, state=tk.NORMAL)
button6.grid(row=2,column=2)
button7 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click7, state=tk.NORMAL)
button7.grid(row=3,column=0)
button8 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click8, state=tk.NORMAL)
button8.grid(row=3,column=1)
button9 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click9, state=tk.NORMAL)
button9.grid(row=3,column=2)
score_text = tk.Label(text=score.text(), font=('Helvetica', '14'))
score_text.grid(row=4, column=0, columnspan=3, sticky=tk.W)
bottom_text = tk.Label(text=bottom_message.get(), font=('Helvetica', '14'), foreground="red")
bottom_text.grid(row=5, column=0, columnspan=3)

root.mainloop()