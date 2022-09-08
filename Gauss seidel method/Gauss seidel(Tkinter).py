from tkinter import *
from tkinter import font
from tkinter import ttk
import os
import sys

root=Tk()

#Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

#my_canvas.create_rectangle(20,0,650,100)

root.title("Gauss Seidel")
root.geometry("600x700")
title = Label(root, text=" Solution of equation: Gauss-seidel method ",relief=RIDGE)
title.config(font=("Times New Roman", 25, 'bold'))
title.place(x=1000,y=50, anchor='center')
f=font.Font(family='Century Gothic',size="19",weight="bold")
#taking a1,a2,a3,b1,b2,b3,c1,c2,c3
e1=Entry(root,width=5)
e1.place(x=750,y=100)
e2=Entry(root,width=5)
e2.place(x=850,y=100)
e3=Entry(root,width=5)
e3.place(x=950,y=100)
e4=Entry(root,width=5)
e4.place(x=750,y=150)
e5=Entry(root,width=5)
e5.place(x=850,y=150)
e6=Entry(root,width=5)
e6.place(x=950,y=150)
e7=Entry(root,width=5)
e7.place(x=750,y=200)
e8=Entry(root,width=5)
e8.place(x=850,y=200)
e9=Entry(root,width=5)
e9.place(x=950,y=200)
#d1,d2,d3
e10=Entry(root,width=5)
e10.place(x=1050,y=100)
e11=Entry(root,width=5)
e11.place(x=1050,y=150)
e12=Entry(root,width=5)
e12.place(x=1050,y=200)
#initial values
e14=Entry(root,width=5)
e14.place(x=780,y=470)
e15=Entry(root,width=5)
e15.place(x=880,y=470)
e16=Entry(root,width=5)
e16.place(x=980,y=470)
#inserting
e1.insert(0,2)
e2.insert(0,-1)
e3.insert(0,0)
e4.insert(0,-1)
e5.insert(0,2)
e6.insert(0,-1)
e7.insert(0,0)
e8.insert(0,-1)
e9.insert(0,2)
e10.insert(0,7)
e11.insert(0,1)
e12.insert(0,1)
e14.insert(0,0)
e15.insert(0,0)
e16.insert(0,0)
#labeling
lba1=Label(root,text="x1",font=f).place(x=780,y=90)
lbb1=Label(root,text="y1",font=f).place(x=880,y=90)
lbc1=Label(root,text="z1",font=f).place(x=980,y=90)
lb_equal=Label(root,text="=",font=f).place(x=1020,y=90)
#x2,y2,z2
lba2=Label(root,text="x2",font=f).place(x=780,y=140)
lbb2=Label(root,text="y2",font=f).place(x=880,y=140)
lbc2=Label(root,text="z2",font=f).place(x=980,y=140)
lb_equal2=Label(root,text="=",font=f).place(x=1020,y=140)
#for x3,y3,z3
lba3=Label(root,text="x3",font=f).place(x=780,y=190)
lbb3=Label(root,text="y3",font=f).place(x=880,y=190)
lbc3=Label(root,text="z3",font=f).place(x=980,y=190)
lb_equal3=Label(root,text="=",font=f).place(x=1020,y=190)
#for initial values
lbaIx=Label(root,text="x:",font=f).place(x=750,y=460)
lbbIy=Label(root,text="y:",font=f).place(x=850,y=460)
lbcIz=Label(root,text="z:",font=f).place(x=950,y=460)
#error-lable
e_error=Entry(root,width=8)
e_error.place(x=840,y=260)
e_error.insert(0,0.0001)
lbl_err=Label(root,text="Error%",font=("Times New Roman",20, 'bold'),fg="red").place(x=740,y=250)
#intial values lable
lbl_Ini=Label(root,text="Initial values of - ",font=("Times New Roman",20, 'bold'),relief=SUNKEN,fg="red").place(x=750,y=420)
mymenu=Menu(root)
mymenu.add_command(label="Quit!", command=root.destroy)
def opennew():
    os.startfile('new gauss.py')
mymenu.add_command(label="New",command=opennew)
root.config(menu=mymenu)

def seidel():   
    global a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3
    k1=e1.get()
    k2=e2.get()
    k3=e3.get()
    k10=e10.get()
    k4=e4.get()
    k5=e5.get()
    k6=e6.get()
    k11=e11.get()
    k7=e7.get()
    k8=e8.get()
    k9=e9.get()
    k12=e12.get()  
    k13=e_error.get()
    k14=e14.get()
    k15=e15.get()
    k16=e16.get()
    
    a1=int(k1)
    b1=int(k2)
    c1=int(k3)
    d1=float(k10)
    a2=int(k4)
    b2=int(k5)
    c2=int(k6)
    d2=float(k11)
    a3=int(k7)
    b3=int(k8)
    c3=int(k9)
    d3=float(k12)
# Reading tolerable error
    e=float(k13)
    x0 = int(k14)
    y0 = int(k15)
    z0 = int(k16)
    count = 1
# Implementation of Gauss Seidel Iteration
    print('\nCount\tx\ty\tz\n')
    global x1,y1,z1
    condition = True
    
    while condition:
        x1 = f1(x0,y0,z0)
        y1 = f2(x1,y0,z0)
        z1 = f3(x1,y1,z0)
        print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
        str0=StringVar()
        str0.set(count)
        ent0=Entry(second_frame,width=4,state='readonly',textvariable=str0).grid(row=count, column=0, pady=30, padx=count*1000)
        #text2=Label(second_frame, text='').grid(row=count, column=0)
        str1=StringVar()
        str1.set(count)
        ent1=Entry(second_frame,width=4,state='readonly',textvariable=str1,font=f)        
        ent1.place(x=80,y=count*40+70) 
        str2=StringVar()
        str2.set(round(x1,6))
        ent2=Entry(second_frame,width=9,state='readonly',textvariable=str2,font=f)
        ent2.place(x=180,y=count*40+70)
        str3=StringVar()
        str3.set(round(y1,6))
        ent3=Entry(second_frame,width=9,state='readonly',textvariable=str3,font=f)
        ent3.place(x=330,y=count*40+70)
        str4=StringVar()
        str4.set(round(z1,6))
        ent4=Entry(second_frame,width=9,state='readonly',textvariable=str4,font=f)
        ent4.place(x=480,y=count*40+70)
        #text2=Label(root, text=round(x1,6), font=f).place(x=180,y=count*40+70)
        #text3=Label(root, text=round(y1,6), font=f).place(x=330,y=count*40+70)
        #text3=Label(root, text=round(z1,6), font=f).place(x=480,y=count*40+70)
        er1 = abs(x0-x1);
        er2 = abs(y0-y1);
        er3 = abs(z0-z1);        
        count += 1
        x0 = x1
        y0 = y1
        z0 = z1    
        condition = er1>e and er2>e and er3>e
    sol()
x1,y1,z1=0,0,0
f1 = lambda x,y,z: (d1-b1*y-c1*z)/a1
f2 = lambda x,y,z: (d2-a2*x-c2*z)/b2
f3 = lambda x,y,z: (d3-a3*x-b3*y)/c3
#adding enter buton
Enter=Button(root, text="Enter ",command=seidel,fg="red",bg="white",font=('Times New Roman', 18))
Enter.place(x=950,y=250)
lbl_sol=Label(root,text="SOLUTION :",font=("Times New Roman",20, 'bold'),relief=GROOVE,fg="blue").place(x=740,y=320)
lbl_field0=Label(root,text='\t\t\t',font=("Times New Roman",40,'bold')).place(x=20,y=0)
lbl_field=Label(root,text='Count          ',font=("Times New Roman",20, 'bold')).place(x=70,y=50)
lbl_field1=Label(root,text='x                     ',font=("Times New Roman",20, 'bold'),fg="red").place(x=185,y=50)
lbl_field2=Label(root,text='y                     ',font=("Times New Roman",20, 'bold'),fg="blue").place(x=335,y=50)
lbl_field3=Label(root,text='z                     ',font=("Times New Roman",20, 'bold'),fg="green").place(x=485,y=50)
def sol():
    sol=('x=%0.3f , y=%0.3f ,z=%0.3f\n'% (x1,y1,z1))
    solution=Label(root,text=sol,font=f).place(x=920,y=320)

root.state('zoomed')
root.mainloop()
