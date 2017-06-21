from tkinter import *
import os
import win32com.client as wincl
import speech_recognition as sr
# from threading import Thread
from multiprocessing import Process


def initiation():
    spk = wincl.Dispatch("SAPI.SpVoice")
    spk.Speak('''Good to see you Sir, Dazzor, at your service.''')
    spk.Speak("Please Enter the movie name")


def window_set():
    win.wm_title("Line Counter")        # Gives title to window
    # Set window icon
    icon = PhotoImage(file=r"C:\Drives_kp\Learning\PyCodes\LOC\icon.png")
    win.tk.call('wm', 'iconphoto', win._w, icon)
    win.geometry("600x300") # Setting window default size
    # --- Adding Background image ---
    background_label = Label(win, image=background_image, justify=RIGHT)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


def clear_field():
    movie_entry.delete('1.0', END)
    op_text.delete('1.0', END)


def search_web():
    # do nothing
    ''' Empty field'''


if __name__ == '__main__':
    win = Tk()
    background_image = PhotoImage(file=r"C:\Drives_kp\Learning\PyCodes\LOC\FileExpo.png")
    window_set()
    text_font, text_size, bg_color = "Calibri", 12, '#1E3C5C'
    # Labels and Fields
    movie = Label(win, text="Movie Name")  # label.config(font=("Courier", 44))
    movie.config(font=(text_font, text_size), bg=bg_color, fg='white')
    movie_entry = Text(win, bd=4, height=1.2, width=43, font=(text_font, text_size), state=NORMAL)
    op = Label(win, text="Details", font=(text_font, text_size), bg=bg_color, fg='white')
    op_text = Text(win, bd=4, height=7, width=43, font=(text_font, text_size), state=NORMAL)
    # Speech function call (Multi processing)
    run_proc = Process(target=initiation)
    run_proc.start()
    # Placement for the fields
    movie.grid(row=1, column=1, padx=7, pady=7, sticky="W")  # If it is grid it should br grid in all places
    movie_entry.grid(row=1, column=2, padx=5, pady=7)
    op.grid(row=3, column=1, padx=7, pady=7, sticky="NW")  # sticky=NorthWest
    op_text.grid(row=3, column=2, padx=5, pady=5)
    # Buttons
    # q1 = Button(win, text='Close', command=win.quit, width=10, font=(text_font, text_size))
    q1 = Button(win, text='Clear', command=clear_field, width=10, font=(text_font, text_size))
    sub = Button(win, text='Submit', command=search_web, width=10, font=(text_font, text_size), relief="raised")
    sub.place(x=180, y=250)
    q1.place(x=300, y=250)
    center(win)
    win.mainloop() # && initiation()
