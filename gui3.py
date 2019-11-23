import tkinter as tk
from tkinter import filedialog
from tkinter import font

filename=''

def exit(event):
    root.destroy()

def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    x='Selected : '+filename
    txt.delete(0.0,tk.END)
    txt.insert(0.0,x)
    
    #p.config(file=filename)
    #txt.image_create(tk.END,image=p)

def RunAction(event=None):
    print('Running:', filename)
    x='Running : '+filename
    txt.delete(0.0,tk.END)
    txt.insert(0.0,x)

def BackAction(event=None):
    txt.delete(0.0,tk.END)
    

def DownloadAction(event=None):
    filename='rand'
    x=txt.get(1.0,tk.END)
    filename=filedialog.asksaveasfilename(defaultextension=".html", filetypes=(("html file", "*.html"),))
    with open(filename,'w') as f:
        f.write(x)

        

root = tk.Tk()
root.geometry("19200x1080")
root.config(background="white")
root.attributes("-fullscreen",True)
root.bind("<Escape>", exit)

Hel=font.Font(family='Helvetica', size=12, weight='bold')
HelTitle=font.Font(family='Helvetica', size=32, weight='bold')


#p=tk.PhotoImage(file="test.gif")

'''
img=tk.PhotoImage(file="bg.gif")
bg=tk.Label(root,image=img)
bg.place(x=0,y=0,relwidth=1,relheight=1)
'''

btn = tk.Button(root, text='Upload', command=UploadAction)
#btn.pack()
btn.config(height=2,width=8,font=Hel,bg="#4dbd6b")
btn.place(relx=0.35,rely=0.2)

run = tk.Button(root, text='Run', command=RunAction)
run.config(height=2,width=8,font=Hel,bg="#4dbd6b")
run.place(relx=0.45,rely=0.2)

dl = tk.Button(root, text='Download', command=DownloadAction)
dl.config(height=2,width=8,font=Hel,bg="#4dbd6b")
dl.place(relx=0.55,rely=0.2)

back = tk.Button(root, text='Back',command=BackAction)
#back.pack()
back.config(height=2,width=8,font=Hel,bg="#4dbd6b")
back.place(relx=0.65,rely=0.2)


lbl=tk.Label(root,text='HTML Code Generator')
#lbl.pack()
lbl.config(height=2,width=20,font=HelTitle,fg="#4dbd6b",bg="white")
lbl.place(relx=0.3,rely=0.05)

txt=tk.Text(root)
#txt.pack()
txt.config(font=Hel,bg="white")
txt.config(height=20,width=70)
txt.place(relx=0.25,rely=0.3)

root.mainloop()
