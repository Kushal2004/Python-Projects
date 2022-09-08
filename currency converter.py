import tkinter as tk
from tkinter import ttk
conv_rates = {'usd_inr': 74.77}


def money_conv(m, from_curr, to_curr):
    if from_curr == 'INR' and to_curr == 'USD':
        return m / conv_rates['usd_inr']
    elif from_curr == 'USD' and to_curr == 'INR':
        return m * conv_rates['usd_inr']
    else:
        return m


def convert():
    m = int(from_curr_txt.get())
    from_curr = from_drop.get()
    to_curr = to_drop.get()
    conv_m = money_conv(m, from_curr, to_curr)

    to_curr_txt.set(round(conv_m, 2))


top = tk.Tk()
top.geometry("400x400")
top.title("Currency Convertor")
title = tk.Label(top, text="Currency Convertor")
title.config(font=("Times New Roman", 20, 'bold'))

from_curr_txt = tk.StringVar()
from_curr_label = tk.Label(top, text='From Currency: ', font=('Times New Roman', 15))
from_curr_entry = tk.Entry(top, textvariable=from_curr_txt, font=('Times New Roman', 15, 'normal'))

to_curr_txt = tk.StringVar()
to_curr_label = tk.Label(top, text='To Currency: ', font=('Times New Roman', 15))
to_curr_entry = tk.Entry(top, state='readonly', textvariable=to_curr_txt, font=('Times New Roman', 15, 'normal'))

conv_but = tk.Button(top, text='Convert', command=convert, font=('Times New Roman', 15))

conv_opt = ["INR", "USD"]
from_drop = ttk.Combobox(top, values=conv_opt, width=10, state="readonly")
to_drop = ttk.Combobox(top, values=conv_opt, width=5, state="readonly")

from_drop.current(0)
to_drop.current(1)

title.place(relx=0.5, rely=0.1, anchor='center')

from_curr_label.place(relx=0.4, rely=0.2, anchor='center')
from_curr_entry.place(in_=from_curr_label, relx=1.1)
from_drop.place(in_=from_curr_entry, relx=1.1)

to_curr_label.place(relx=0.4, rely=0.35, anchor='center')
to_curr_entry.place(in_=to_curr_label, relx=1.1)
to_drop.place(in_=to_curr_entry, relx=1.1)

conv_but.place(relx=0.5, rely=0.5, anchor='center')


top.state('zoomed')

top.mainloop()



