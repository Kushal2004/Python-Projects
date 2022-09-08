import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import font
import os
import sys  

top= tk.Tk() 
top.title("unicode convertions")
ttk.Label(top, text="Unicode Convertions",
          font=("Times New Roman", 20)).grid(column=0, row=0)

ttk.Label(top, text="Input Data:", font=("Bold", 18)).place(x=15,y=70)
ttk.Label(top, text="Output:", font=("Bold", 18)).place(x=15,y=330)
  
text_area = scrolledtext.ScrolledText(top, wrap=tk.WORD,width=40, height=8,
                                      font=("Times New Roman", 15))
  
text_area.grid(column=0, row=5, pady=80, padx=10)

text_box = scrolledtext.ScrolledText(
    top,
    height=10,
    width=50
)
text_box.grid(column=0, row=20, pady=10, padx=100)

#adding menu option
mymenu=tk.Menu(top)
mymenu.add_command(label="Quit!", command=top.destroy)
def opennew():
    os.startfile('unicode converter.py')
mymenu.add_command(label="New",command=opennew)
top.config(menu=mymenu)

#actual logic of the program

def asci_text(m, from_curr, to_curr):
    if from_curr == 'Ascii' and to_curr == 'Text':
        x=m.split()
        lst=[]
        for i in x:
         lst.append(int(i))
        res = ""
        for i in lst:
         res = res + chr(i)
        print(str(res))       
        return str(res)
    elif from_curr == 'Text' and to_curr == 'Ascii':
        ascii_values = []
        for character in m:
         ascii_values.append(ord(character))     
        return ascii_values
    else:
        return m
def convert():                          # this function takes values from user and sends to the above method,                                    
    top.output_area = tk.Text(top)     
    m = text_area.get("1.0",'end-1c')   
    print("input data:",m)
    from_curr = from_drop.get()
    to_curr = to_drop.get()
    converted = asci_text(m, from_curr, to_curr) # the output is stored in "converted" variable
    print("function called:",converted )
    text_box.insert('end',converted)

conv_but = tk.Button(top, text='Convert', command=convert,fg="red",font=('Times New Roman', 15))
conv_but.place(x=300,y=70)

#adding drop box
conv_opt = ["Ascii", "Text"]
from_drop = ttk.Combobox(top, values=conv_opt, width=10, state="readonly")
to_drop = ttk.Combobox(top, values=conv_opt, width=10, state="readonly")
from_drop.current(1)
to_drop.current(0)

from_drop.place(x=140,y=75)
to_drop.place(x=130,y=334)



# placing cursor in text area
text_area.focus()
top.mainloop()
