from tkinter import Button
import utils

class Cell():
    def __init__(self, x_loc, y_loc, is_mine:bool=False):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_button(self, location):
        button = Button(
            location,
            width=utils.button_width(utils.frame_width(75)),
            height=utils.button_height(utils.frame_height(75)),
            bg='white',
            text=f"{self.x_loc, self.y_loc}"
        )
        button.bind('<Button-1>', self.left_click_action) #left click
        button.bind('<Button-2>', self.right_click_action) #right click
        self.cell_btn_object = button

    def left_click_action(self, event): #need to add event since it is convention for tkinter
        print(event)
        print('I am left clicked!')

    def right_click_action(self, event):
        print(event)
        print('I am right clicked!')
