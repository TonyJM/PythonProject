import tkinter as tk
from tkinter import filedialog
from tkinter import font

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    x='Selected : '+filename
    lbl.config(text=x)
    txt.delete(0.0,tk.END)
    txt.insert(0.0,x)

def BackAction(event=None):
    lbl.config(text='')
    txt.delete(0.0,tk.END)

root = tk.Tk()
root.geometry("1500x800")

Hel=font.Font(family='Helvetica', size=12, weight='bold')

img=tk.PhotoImage(file="bg.gif")
bg=tk.Label(root,image=img)
bg.place(x=0,y=0,relwidth=1,relheight=1)

btn = tk.Button(root, text='Open', command=UploadAction)
#btn.pack()
btn.config(height=2,width=8,font=Hel,bg="#3aa9b5")
btn.place(relx=0.35,rely=0.2)

back = tk.Button(root, text='Back',command=BackAction)
#back.pack()
back.config(height=2,width=8,font=Hel,bg="#3aa9b5")
back.place(relx=0.55,rely=0.2)

lbl=tk.Label(root,text='Test')
#lbl.pack()
#lbl.place(relx=0.5,rely=0.5)

txt=tk.Text(root)
#txt.pack()
txt.config(font=Hel,bg="#3aa9b5")
txt.place(relx=0.25,rely=0.3)

root.mainloop()
