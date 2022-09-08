from tkinter import *
from tkinter import font
from pytube import *
root=Tk()
root.title("YOUTUBE VIDEO DOWNLOADER")
root.geometry("620x300")
f=font.Font(family='Century Gothic',size="15",weight="bold")
lb1=Label(root,text="LINK:",fg='red',font=f).place(x=10,y=15)
e1=Entry(root,width=55)
e1.place(x=75,y=15)
def lin():
    link=e1.get()
    yt=YouTube(link)
    lbl1=Label(root,text="Title:").place(x=10,y=65)
    lbl2=Label(root,text=yt.title).place(x=100,y=65)
    ys=yt.streams.filter(progressive=True)
    l=[]
    for i in ys:
        k=str(i.resolution)
        l.append(k)
    lbl5=Label(root,text="Streams available").place(x=10,y=100)
    lbl3=Label(root,text=l[0]).place(x=120,y=100)
    dlb=Button(root,text="Download",fg="green",command=dl360)
    dlb.place(x=170,y=100)
    try:
        if l[1]=='720p':
            lbl4=Label(root,text=l[1]).place(x=120,y=150)
            dlb=Button(root,text="Download",fg="green",command=dl720)
            dlb.place(x=170,y=150)
    except:
        pass
def dl360():
    link=e1.get()
    yt=YouTube(link)
    ys=yt.streams.filter(progressive=True)
    dwld=ys.filter(resolution='360p')
    dwld.first().download()
    popup=Tk()
    popup.title("Downloaded")
    popup.geometry("250x100")
    def close():
        root.destroy()
        popup.destroy()
    label=Label(popup,text="Download over!").place(x=10,y=10)
    myb=Button(popup,text="Close",fg="red",command=close)
    myb.place(x=10,y=60)
def dl720():
    link=e1.get()
    yt=YouTube(link)
    ys=yt.streams.filter(progressive=True)
    dwld=ys.filter(resolution='720p')
    dwld.first().download()
    popup=Tk()
    popup.title("Downloaded")
    popup.geometry("250x100")
    def close():
        root.destroy()
        popup.destroy()
    label=Label(popup,text="Download over!").place(x=10,y=10)
    myb=Button(popup,text="OK",fg="red",command=close)
    myb.place(x=30,y=30)
    
mybutton=Button(root, text="SHOW DETAILS",fg="blue",bg="white",command=lin)
mybutton['font']=f
mybutton.place(x=450,y=15)
root.mainloop()
