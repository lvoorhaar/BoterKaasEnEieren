# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:15:33 2019

@author: Lenny
"""

import tkinter as tk

##FUNCTIONS##

def Click(button): #Actie wanneer er op een knop geklikt wordt
    if button["text"] == "":
        letter = current_letter.get()
        button["text"] = letter
        if check_if_won(letter):
            game_won()
            disable_buttons()
        elif check_if_draw():
            draw()
            disable_buttons()
        else:
            current_letter.change()
            message.set("Klik op een leeg vakje om een " + current_letter.get() + " te plaatsen.")
            bottom_text["text"] = message.get()
    else:
        message.set("Dit vakje is al gebruikt. Klik op een leeg vakje om een " + current_letter.get() + " te plaatsen.")
        bottom_text["text"] = message.get()

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

def game_won():
    message.set("Het spel is afgelopen. Speler " + current_letter.get() + " heeft gewonnen.")
    bottom_text["text"] = message.get()

def check_if_draw(): #Kijkt of er gelijkspel is
    if check_if_won("X") == True or check_if_won("O") == True:
        return False
    elif button1["text"] == "" or button2["text"] == "" or button3["text"] == "" or button4["text"] == "" or button5["text"] == "" or button6["text"] == "" or button7["text"] == "" or button8["text"] == "" or button9["text"] == "":
        return False
    return True

def draw():
    message.set("Het spel is geëindigd in gelijkspel.")
    bottom_text["text"] = message.get()
    
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
    
##CLASSES##
class Current_letter(object): #Welke speler aan de beurt is
    
    def __init__(self, letter):
        self.letter = letter
    
    def get(self):
        return self.letter
    
    def change(self):
        if self.get() == "X":
            self.letter = "O"
        else:
            self.letter = "X"

class Message(object): #Tekst die onder in beeld staat
    
    def __init__(self, text):
        self.text = text
        
    def get(self):
        return self.text
    
    def set(self, new_text):
        self.text = new_text

##MAIN CODE##
current_letter = Current_letter("X")
message = Message("Klik op een leeg vakje om een " + current_letter.get() + " te plaatsen.")

root = tk.Tk()
root.title("Boter, kaas en eieren")
frame = tk.Frame(root)
frame.grid()

button1 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click1, state=tk.NORMAL)
button1.grid(row=1,column=1)
button2 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click2, state=tk.NORMAL)
button2.grid(row=1,column=2)
button3 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click3, state=tk.NORMAL)
button3.grid(row=1,column=3)
button4 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click4, state=tk.NORMAL)
button4.grid(row=2,column=1)
button5 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click5, state=tk.NORMAL)
button5.grid(row=2,column=2)
button6 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click6, state=tk.NORMAL)
button6.grid(row=2,column=3)
button7 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click7, state=tk.NORMAL)
button7.grid(row=3,column=1)
button8 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click8, state=tk.NORMAL)
button8.grid(row=3,column=2)
button9 = tk.Button(frame, text="", font=('Helvetica', '80'), width=3, command=Click9, state=tk.NORMAL)
button9.grid(row=3,column=3)
bottom_text = tk.Label(text=message.get(), font=('Helvetica', '14'))
bottom_text.grid(row=4)

root.mainloop()

