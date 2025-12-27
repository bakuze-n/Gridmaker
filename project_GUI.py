import tkinter as tk
from tkinter import ttk

# Base window for GUI, set width and height
window = tk.Tk()
window.title('Gridmaker')
w_width, w_height = 600, 400
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

tab_creategrid.grid_rowconfigure(index=0, weight=1, minsize=200)
tab_creategrid.grid_rowconfigure(index=1, weight=1)
tab_creategrid.grid_columnconfigure(index=0, weight=1)
tab_creategrid.grid_columnconfigure(index=1, weight=0, minsize=200)

frame_A = ttk.Frame(tab_creategrid, relief='flat')
frame_B = ttk.Frame(tab_creategrid, relief='flat')
frame_C = ttk.Frame(tab_creategrid, relief='flat')
frame_D = ttk.Frame(tab_creategrid, relief='flat')

frame_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_B.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
frame_C.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
frame_D.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

frame_A.grid_rowconfigure(index=0, weight=1)
frame_A.grid_rowconfigure(index=1, weight=1)
frame_A.grid_columnconfigure(index=0, weight=1)
frame_A.grid_columnconfigure(index=1, weight=1)

frame_A_subframe_A = tk.Frame(frame_A, relief='flat', bg='black')
frame_A_subframe_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_A_subframe_B = tk.Frame(frame_A, relief='flat', bg='black')
frame_A_subframe_B.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
frame_A_subframe_C = tk.Frame(frame_A, relief='flat', bg='black')
frame_A_subframe_C.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
frame_A_subframe_D = tk.Frame(frame_A, relief='flat', bg='black')
frame_A_subframe_D.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

frame_B.grid_rowconfigure(index=0, weight=0, minsize=150)
frame_B.grid_rowconfigure(index=1, weight=0, minsize=35)
frame_B.grid_rowconfigure(index=2, weight=1)
frame_B.grid_columnconfigure(index=0, weight=1)

frame_B_subframe_A = tk.Frame(frame_B, relief='flat', bg='black')
frame_B_subframe_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_B_subframe_B = tk.Frame(frame_B, relief='flat', bg='black')
frame_B_subframe_B.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

frame_C.grid_rowconfigure(index=0, weight=1)
frame_C.grid_rowconfigure(index=1, weight=1)
frame_C.grid_columnconfigure(index=0, weight=1)
frame_C.grid_columnconfigure(index=1, weight=2)

frame_C_subframe_A = tk.Frame(frame_C, relief='flat', bg='black')
frame_C_subframe_A.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
frame_C_subframe_B = tk.Frame(frame_C, relief='flat', bg='black')
frame_C_subframe_B.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
frame_C_subframe_C = tk.Frame(frame_C, relief='flat', bg='black')
frame_C_subframe_C.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
frame_C_subframe_D = tk.Frame(frame_C, relief='flat', bg='black')
frame_C_subframe_D.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

frame_D.grid_rowconfigure(index=0, weight=1)
frame_D.grid_rowconfigure(index=1, weight=0, minsize=35)
frame_D.grid_columnconfigure(index=0, weight=1)

frame_D_subframe_A = tk.Frame(frame_D, relief='flat', bg='black')
frame_D_subframe_A.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

# TAB 2: CROP GRID (upload image of grid with barcode, automatically crops cells)
tab_cropgrid = ttk.Frame(notebook_A)
notebook_A.add(tab_cropgrid, text='Crop a Grid')

tab_cropgrid.grid_rowconfigure(index=0, weight=1, minsize=200)
tab_cropgrid.grid_rowconfigure(index=1, weight=1)
tab_cropgrid.grid_columnconfigure(index=0, weight=1)
tab_cropgrid.grid_columnconfigure(index=1, weight=0, minsize=200)

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