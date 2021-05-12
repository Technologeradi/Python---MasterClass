from os import system, name
from tkinter import *
root = Tk()

def fun():
  print('/033c')
  if name == 'nt':
    _ = system('cls')
    print("Hello world"*10)


btn = Button(root, text='Hello', command = fun)
btn.place(x=100,y=100)
btn.grid(root)
root.mainloop()
