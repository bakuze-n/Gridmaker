import tkinter as tk
from tkinter import ttk

'''
GUI for Gridmaker with two tabs: one to create a grid, and one to crop a grid (using the barcode).
Will be refactored soon after the design has been figured out.
(repetitive code will be refactored into concise functions)
'''

# Base window for GUI, set width and height
window = tk.Tk()
window.title('Gridmaker')
w_width, w_height = 550, 400
window.geometry(f'{w_width}x{w_height}')
window.minsize(w_width,w_height)
window.grid_columnconfigure(index=0, weight=1)
window.grid_rowconfigure(index=0, weight=1)

# try to retrieve custom program icon, or else resort to default Tkinter icon
try:
    gridmaker_icon = tk.PhotoImage(file=r'D:\Users\falco\Pictures\My Art\Other\Coding\CS50P\Final Assignment\Extra\gridmaker_icon_small.png')
    window.iconphoto('wm', gridmaker_icon)
except:
    pass

notebook_A = ttk.Notebook(window)
notebook_A.grid(row=0, column=0, sticky='nwse', padx=5, pady=5)

# TAB 1: CREATE GRID (User enters cell width/height, no. of rows/columns and border thickness)
tab_creategrid = ttk.Frame(notebook_A)
notebook_A.add(tab_creategrid, text='Create a Grid')

tab_creategrid.grid_rowconfigure(index=0, weight=1)
tab_creategrid.grid_rowconfigure(index=1, weight=1)
tab_creategrid.grid_columnconfigure(index=0, weight=0)
tab_creategrid.grid_columnconfigure(index=1, weight=1)

frame_A = ttk.Frame(tab_creategrid, relief='flat')
frame_B = ttk.Frame(tab_creategrid, relief='flat')
frame_C = ttk.Frame(tab_creategrid, relief='flat')
frame_D = ttk.Frame(tab_creategrid, relief='flat')

frame_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_B.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
frame_C.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
frame_D.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

frame_A.grid_rowconfigure(index=0, weight=1)
frame_A.grid_columnconfigure(index=0, weight=1)

frame_A_LabelFrame = ttk.Labelframe(frame_A, text='Grid Settings')
frame_A_LabelFrame.grid(row=0, column=0, sticky='nwse', padx=5, pady=5)
frame_A_LabelFrame.grid_rowconfigure(index=0, weight=0)
frame_A_LabelFrame.grid_rowconfigure(index=1, weight=1)
frame_A_LabelFrame.grid_columnconfigure(index=0, weight=0)
frame_A_LabelFrame.grid_columnconfigure(index=1, weight=1, minsize=25)
frame_A_LabelFrame.grid_columnconfigure(index=2, weight=0)

frame_A_column0 = tk.Frame(frame_A_LabelFrame, relief='flat')
frame_A_column0.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_A_column0.grid_rowconfigure(index=0, weight=1, pad=5)
frame_A_column0.grid_rowconfigure(index=1, weight=1, pad=5)
frame_A_column0.grid_rowconfigure(index=2, weight=1, pad=5)
frame_A_column0.grid_rowconfigure(index=3, weight=1, pad=5)
frame_A_column0.grid_columnconfigure(index=0, weight=1, minsize=150)
frame_A_column1 = tk.Frame(frame_A_LabelFrame, relief='flat')
frame_A_column1.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
frame_A_column2 = tk.Frame(frame_A_LabelFrame, relief='flat')
frame_A_column2.grid(row=0, column=2, sticky='nsew', padx=2, pady=2)
frame_A_column2.grid_rowconfigure(index=0, weight=1, pad=5)
frame_A_column2.grid_rowconfigure(index=1, weight=1, pad=5)
frame_A_column2.grid_rowconfigure(index=2, weight=1, pad=5)
frame_A_column2.grid_columnconfigure(index=0, weight=1, minsize=150)

label_CellWidth = ttk.Label(frame_A_column0, text='Cell width:')
label_CellWidth.grid(row=0, column=0, sticky='w')
label_Rows = ttk.Label(frame_A_column0, text='Rows:')
label_Rows.grid(row=1, column=0, sticky='w')
label_GridColor = ttk.Label(frame_A_column0, text='Grid Color:')
label_GridColor.grid(row=2, column=0, sticky='w')

entry_CellWidth = ttk.Entry(frame_A_column0, width=12)
entry_CellWidth.grid(row=0, column=0, sticky='e')
entry_Rows = ttk.Spinbox(frame_A_column0, width=4, from_=1, to=100, increment=1)
entry_Rows.grid(row=1, column=0, sticky='e')

label_CellHeight = ttk.Label(frame_A_column2, text='Cell height:')
label_CellHeight.grid(row=0, column=0, sticky='w')
label_Columns = ttk.Label(frame_A_column2, text='Columns:')
label_Columns.grid(row=1, column=0, sticky='w')

entry_CellHeight = ttk.Entry(frame_A_column2, width=12)
entry_CellHeight.grid(row=0, column=0, sticky='e')
entry_Columns = ttk.Entry(frame_A_column2, width=12)
entry_Columns.grid(row=1, column=0, sticky='e')
list_gridcolors = ['#000000', "#252525", "#505050", "#757575"]
combobox_GridColor = ttk.Combobox(frame_A_column2, values=list_gridcolors, width=22)
combobox_GridColor.grid(row=2, column=0, sticky='e')

frame_B.grid_rowconfigure(index=0, weight=1)
frame_B.grid_columnconfigure(index=0, weight=1)

frame_B_LabelFrame = ttk.Labelframe(frame_B, text='Preview')
frame_B_LabelFrame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
# frame_B_subframe_B = tk.Frame(frame_B, relief='flat', bg='black')
# frame_B_subframe_B.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)

frame_C.grid_rowconfigure(index=0, weight=1)
frame_C.grid_columnconfigure(index=0, weight=1)

frame_C_LabelFrame = ttk.Labelframe(frame_C, text='Output Settings')
frame_C_LabelFrame.grid(row=0, column=0, sticky='nwse', padx=5, pady=5)

# frame_C_subframe_A = tk.Frame(frame_C, relief='flat', bg='black')
# frame_C_subframe_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
# frame_C_subframe_B = tk.Frame(frame_C, relief='flat', bg='black')
# frame_C_subframe_B.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
# frame_C_subframe_C = tk.Frame(frame_C, relief='flat', bg='black')
# frame_C_subframe_C.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
# frame_C_subframe_D = tk.Frame(frame_C, relief='flat', bg='black')
# frame_C_subframe_D.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

frame_D.grid_rowconfigure(index=0, weight=1)
frame_D.grid_rowconfigure(index=1, weight=1)
frame_D.grid_rowconfigure(index=2, weight=1)
frame_D.grid_columnconfigure(index=0, weight=1)

# WIP: non-functional. Add function that creates grid and prompts user to save it.
frame_D_button_CreateAGrid = ttk.Button(frame_D, text='Save grid', width=15, padding=7.5)
frame_D_button_CreateAGrid.grid(row=2, column=0, sticky='se', padx=2, pady=2)

# TAB 2: CROP GRID (upload image of grid with barcode, automatically crops cells)
tab_cropgrid = ttk.Frame(notebook_A)
notebook_A.add(tab_cropgrid, text='Crop a Grid')

tab_cropgrid.grid_rowconfigure(index=0, weight=1)
tab_cropgrid.grid_rowconfigure(index=1, weight=1)
tab_cropgrid.grid_columnconfigure(index=0, weight=1)
tab_cropgrid.grid_columnconfigure(index=1, weight=1)

frame_A2 = ttk.Frame(tab_cropgrid, relief='flat')
frame_B2 = ttk.Frame(tab_cropgrid, relief='flat')
frame_C2 = ttk.Frame(tab_cropgrid, relief='flat')
frame_D2 = ttk.Frame(tab_cropgrid, relief='flat')

frame_A2.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_A2.grid_rowconfigure(index=0, weight=1)
frame_A2.grid_columnconfigure(index=0, weight=1)
frame_B2.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
frame_B2.grid_rowconfigure(index=0, weight=1)
frame_B2.grid_columnconfigure(index=0, weight=1)
frame_C2.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
frame_C2.grid_rowconfigure(index=0, weight=1)
frame_C2.grid_columnconfigure(index=0, weight=1)
frame_D2.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)
frame_D2.grid_rowconfigure(index=0, weight=1)
frame_D2.grid_columnconfigure(index=0, weight=1)

frame_A_subframe_A = tk.Frame(frame_A2, relief='flat', bg='black')
frame_A_subframe_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_B_subframe_A = tk.Frame(frame_B2, relief='flat', bg='black')
frame_B_subframe_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_C_subframe_A = tk.Frame(frame_C2, relief='flat', bg='black')
frame_C_subframe_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_D_subframe_A = tk.Frame(frame_D2, relief='flat', bg='black')
frame_D_subframe_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

window.mainloop()