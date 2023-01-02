from tkinter import Tk, Frame, Button  #tkinter is the standard Python interface for Tcl/Tk HUI toolkit
import settings
import utils
from cell import Cell

root = Tk() #Instance creator
#Override the settings of the window
root.config(bg='black') #select color of the window
root.geometry(f"""{settings.WINDOW_WIDTH}x{settings.WINDOW_HEGIHT}""") #WIDTHxHIGHT
root.title('Mine Sweeper Game')
root.resizable(False, False) #not resixing the window

#Creating different frames in the window
top_frame = Frame(root,
        bg='red',
        width=settings.WINDOW_WIDTH,
        height=utils.frame_height(25),
)
top_frame.place(x=0, y=0)

left_frame = Frame(root,
        bg='blue',
        width = utils.frame_width(25),
        height= utils.frame_height(75),
)
left_frame.place(x=0, y=utils.frame_height(25))

central_frame = Frame(root,
        bg='black',
        width= utils.frame_width(75),
        height= utils.frame_height(75),
            )
central_frame.place(x=utils.frame_width(25), y=utils.frame_height(25))

# Creating all the cells in my central frame
for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
                c = Cell(x,y)
                c.create_btn_object(central_frame)
                c.cell_btn_object.grid(row=x, column=y)


# Call the label from left frame
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
        x=0,
        y=0
)

# Randomizing which cells should have mines
Cell.randomize_mines()


#Run the window
root.mainloop()
