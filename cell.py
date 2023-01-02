from tkinter import Button
import utils
import random
import settings
from typing import List

class Cell:
    all_cells = []

    def __init__(self, x_loc, y_loc, is_mine=False):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.is_mine = is_mine
        self.cell_btn_object = None
        
        Cell.all_cells.append(self) # Appending the object ti the cell.all list

    def create_btn_object(self, location):
        button = Button(
            location,
            width=utils.button_width(utils.frame_width(75)),
            height=utils.button_height(utils.frame_height(75)),
            text=f"{self.x_loc, self.y_loc}"
        )
        button.bind('<Button-1>', self.left_click_action) #left click
        button.bind('<Button-2>', self.right_click_action) #right click
        self.cell_btn_object = button

    def left_click_action(self, event): #need to add event since it is convention for tkinter
        if self.is_mine:
            print('I am a mine')
            self.show_mine()
        else:
            print('I am no mine!')
            self.show_cell()
    
    def show_mine(self):
        # logic to interupt the game and displaying lost message
        # temp solution while developing:
        self.cell_btn_object.configure(highlightbackground="red")

    def show_cell(self):
        print('surrounded_cells', self.surrounded_cells)
        print('num of mines near by', self.num_of_surrounded_mines)
    
    @property
    def surrounded_cells(self):
        cells = []
        for cell in Cell.all_cells:
            hypotenus = (self.x_loc-cell.x_loc)**2+(self.y_loc-cell.y_loc)**2
            if hypotenus >= 1 and hypotenus <= 2:
                cells.append(cell)
        return cells

    @property
    def num_of_surrounded_mines(self):
        num_of_mines = len([cell for cell in self.surrounded_cells if cell.is_mine])
        return num_of_mines


    def right_click_action(self, event):
        print(event)
        print('I am right clicked!')

    def get_cell_by_axis(self, x, y):
        # returning a cell object based on location of the cell
        for cell in Cell.all_cells:
            if cell.x_loc == x and cell.y_loc == y:
                return cell

    @staticmethod # belongs globally to the class - not to the instance
    def randomize_mines():
        picked_cells = random.sample(Cell.all_cells, settings.MINES_COUNT)
        print('mine cells:', picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
            
    def __repr__(self):
        return f"Cell({self.x_loc, self.y_loc})"
