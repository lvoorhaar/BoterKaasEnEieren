# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:55:13 2019

@author: Lenny
"""
##FUNCTIONS##
def turn(board, letter): #Speler doet een zet
    while True:
        try:
            tile = int(input("Kies een leeg vakje om een " + letter + " te plaatsen (1-9): "))
            board.play(tile, letter)
            break
        except ValueError:
            print("Geen geldig nummer. Probeer het nogmaals.")

def run_game(): #Speel een potje BKeE
    board = Board()
    board.print()
    while True:
        turn(board, "X")
        board.print()
        if board.check_if_won("X"):
            print("Speler X heeft gewonnen.")
            break
        elif board.check_if_draw():
            print("Het spel is geëindigd in gelijkspel.")
            break
        turn(board, "O")
        board.print()
        if board.check_if_won("O"):
            print("Speler O heeft gewonnen.")
            break
        elif board.check_if_draw():
            print("Het spel is geëindigd in gelijkspel.")
            break
    
def menu(): #Kies een optie om een nieuw spel te spelen of af te sluiten
    while True:
        option = input("Kies 'n' voor een nieuw spel, of 'x' om af te sluiten: ")
        if option == "x":
            print("Tot ziens!")
            break
        elif option == "n":
            run_game()
        else:
            print("Geen geldige optie.")
    
##CLASSES##
class Board(object):
    #Spelbord met 9 vakjes
    def __init__(self):
        self.tiles = {}
        for n in range (1, 10):
            self.tiles[n] = " "
    
    def print(self): #Print het speelveld
        print(self.tiles[1] + " | " + self.tiles[2] + " | " + self.tiles[3])
        print("---------")
        print(self.tiles[4] + " | " + self.tiles[5] + " | " + self.tiles[6])
        print("---------")
        print(self.tiles[7] + " | " + self.tiles[8] + " | " + self.tiles[9])
        
    def check_if_empty(self, tile): #Kijkt of een vakje leeg is
        if self.tiles[tile] == " ":
            return True
        else:
            return False
        
    def play(self, tile, letter): #Zet een X of O in een vakje
        if tile not in self.tiles:
            raise ValueError
        elif self.check_if_empty(tile) == False:
            raise ValueError
        else:
            self.tiles[tile] = letter
            
    def check_if_won(self, letter): #Kijkt of een speler heeft gewonnen
        if self.tiles[1] == letter and self.tiles[2] == letter and self.tiles[3] == letter:
            return True
        elif self.tiles[4] == letter and self.tiles[5] == letter and self.tiles[6] == letter:
            return True
        elif self.tiles[7] == letter and self.tiles[8] == letter and self.tiles[9] == letter:
            return True
        elif self.tiles[1] == letter and self.tiles[4] == letter and self.tiles[7] == letter:
            return True
        elif self.tiles[2] == letter and self.tiles[5] == letter and self.tiles[8] == letter:
            return True
        elif self.tiles[3] == letter and self.tiles[6] == letter and self.tiles[9] == letter:
            return True
        elif self.tiles[1] == letter and self.tiles[5] == letter and self.tiles[9] == letter:
            return True
        elif self.tiles[3] == letter and self.tiles[5] == letter and self.tiles[7] == letter:
            return True
        else:
            return False

    def check_if_draw(self): #Kijkt of er gelijkspel is
        if self.check_if_won("X") == True or self.check_if_won("O") == True:
            return False
        else:
            for n in range (1, 10):
                if self.tiles[n] == " ":
                    return False
        return True
        
        
##MAIN CODE##
print("Welkom bij boter, kaas & eieren.")
print("De vakjes zijn genummerd van 1 t/m 9 van linksboven naar rechtsonder.")
menu()