from tkinter import *
from tkinter.font import Font
from tkinter import messagebox,filedialog
from PIL import Image
import img2pdf
import os
import webbrowser

def main():
    
    #########################    Root Frame ########################
    root=Tk()
    root.overrideredirect(1)

    root.geometry('388x565+500+50')
    #########   Background Image    ############
    img=PhotoImage(file=r'B:\All- Python\Projects\0- Low Level\Image2pdf\Screenshot_2.png')
    lb=Label(root,image=img)
    lb.place(x=0,y=0)

    icont=PhotoImage(file=r'B:\All- Python\Projects\0- Low Level\Image2pdf\cont.png')
   
    
    ##########################   MAIN WINDOW    ###################
    
    def mini1():
        root.overrideredirect(0)
        root.iconify()

    def show1(event):
        root.overrideredirect(1)

    def move1(event):
        root.geometry('+{0}+{1}'.format(event.x_root,event.y_root))

    def prog():
        
        ###################     LOGIC     ############
        def conv():
            try:
                ip=s1.get()
                op=s2.get()
                if ip.lower().endswith('.jpg'):
                    img=Image.open(ip)
                    pdf=img2pdf.convert(img.filename)
                    file=open(op,'wb')
                    file.write(pdf)
                    img.close()
                    file.close()
                    m=messagebox.showinfo('Success','The File is successfully converted. : )')
                    conf=messagebox.askyesno('','Do you want to view the PDF file?')
                    if conf:
                        os.startfile(op)
                else:
                    if os.path.exists('C:/Img-2-PDF/JPG_images'):
                        pass
                    else:
                        os.makedirs('C:/Img-2-PDF/JPG_images')


                    img=Image.open(ip)
                    fol=os.path.dirname(ip)
                    img.load()
                    image=Image.new('RGB',img.size,(255,255,255))
                    image.paste(img,mask=img.split()[3])
                    nm='C:/Img-2-PDF/JPG_images/ix1080.jpg'
                    image.save(nm,'JPEG',quality=100)
                    im=Image.open(nm)
                    pdf=img2pdf.convert(im.filename)
                    file=open(op,'wb')
                    file.write(pdf)
                    img.close()
                    file.close()
                    m=messagebox.showinfo('Success','The File is successfully converted. : )')
                    conf=messagebox.askyesno('','Do you want to view the PDF file?')
                    if conf:
                        os.startfile(op)

            except Exception as e :
                if s1.get=='':
                    messagebox.showerror('Error','Please choose a source file.')
                elif s2.get=='':
                    messagebox.showerror('Error','Please choose a destination folder.')
                else:
                    messagebox.showerror('Error',e)
                  

        def ex():
            win.destroy()        
        def mode():
            i=r.get()
            if i==1:
                lbg.configure(bg='wheat',fg='black')
                lsrc.configure(bg='wheat',fg='black')
                bsrc.configure(bg='wheat',fg='black')
                esrc.configure(bg='white',fg='black')
                ldest.configure(bg='wheat',fg='black')
                bdest.configure(bg='wheat',fg='black')
                edest.configure(bg='white',fg='black')
                ltheme.configure(bg='wheat',fg='black')
                r1.configure(bg='wheat',fg='black')
                r2.configure(bg='wheat',fg='black')
                bok.configure(bg='wheat',fg='black')
                bconv.configure(bg='wheat',fg='black')
                bclr.configure(bg='wheat',fg='black')
                bex.configure(bg='wheat',fg='black')
                lcrdt.configure(bg='wheat',fg='blue')
                lmail.configure(bg='wheat',fg='blue')
            if i==2:
                lbg.configure(bg='black')
                lsrc.configure(bg='black',fg='gray')
                bsrc.configure(bg='gray',fg='black')
                esrc.configure(bg='gray',fg='black')
                ldest.configure(bg='black',fg='gray')
                bdest.configure(bg='gray',fg='black')
                edest.configure(bg='gray',fg='black')
                ltheme.configure(bg='black',fg='gray')
                r1.configure(fg='gray',bg='black')
                r2.configure(fg='gray',bg='black')
                bok.configure(bg='gray',fg='black')
                bconv.configure(bg='gray',fg='black')
                bclr.configure(bg='gray',fg='black')
                bex.configure(bg='gray',fg='black')
                lcrdt.configure(bg='black',fg='red')
                lmail.configure(bg='black',fg='red')
        
        def src():
            try:
                op=filedialog.askopenfile(mode='r',filetypes=[('Image Files','*.jpeg'),('Image Files','*.jpg'),('Image Files','*.png'),('Image Files','*.gif'),('Image Files','*.ico')])
                pt=op.name
                esrc.configure(state=NORMAL)
                s1.set(pt)
                esrc.configure(state=DISABLED)
            except AttributeError:
                pass
        def dest():
            op=filedialog.asksaveasfile(filetypes=[('PDF Files','*.pdf')],defaultextension=[('PDF Files','*.pdf')])
            edest.configure(state=NORMAL)
            s2.set(op.name)
            edest.configure(state=DISABLED)
        
        def clr():
            esrc.configure(state=NORMAL)
            edest.configure(state=NORMAL)
            s1.set('')
            s2.set('')
            esrc.configure(state=DISABLED)
            edest.configure(state=DISABLED)

        def mini2():
            win.overrideredirect(0)
            win.iconify()

        def show2(event):
            win.overrideredirect(1)

        def move2(event):
            win.geometry('+{0}+{1}'.format(event.x_root,event.y_root))


        root.destroy()  ###   Closing First Window

        win=Tk()     ###    Starting New Window
        win.geometry('380x390+500+50')
        win.overrideredirect(1)
        lbg=Label(win,height=565,width=388,bg='wheat',fg='black')
        lbg.place(x=0,y=0)
        ##############################################
        frm1=Frame(win,bg='orange',relief='sunken',bd=0)
        lb2=Label(frm1,text='Image 2 PDF',bg='orange',fg='green',font=Font(size=11,weight='bold'))
        lb2.pack(anchor=CENTER)
        
        close1=Button(frm1,text='X',bg='orange',highlightbackground='white',font=Font(size=10,weight='bold'),width=2,relief='flat',command=win.destroy)
        close1.place(x=357,y=0)

        min1=Button(frm1,text='-',bg='orange',highlightbackground='white',font=Font(size=10,weight='bold'),width=2,relief='flat',command=mini2)
        min1.place(x=332,y=0)
        

        frm1.pack(fill=X)

        frm1.bind('<Map>',show2)
        frm1.bind('<B1-Motion>',move2)


        ###############   LABELS    #####################3
        
        
        lsrc=Label(win,text='Source File : ',font=Font(size=15,weight='bold'),bg='wheat',fg='black')
        lsrc.place(x=20,y=40)

        bsrc=Button(win,text='Choose a File',font=Font(size=14),bg='wheat',fg='black',command=src)
        bsrc.place(x=200,y=40)

        s1=StringVar()
        esrc=Entry(win,textvariable=s1,width=30,font=Font(size=14),bg='wheat',fg='black',state=DISABLED)
        esrc.place(x=20,y=85)
        
        ldest=Label(win,text='Destination : ',font=Font(size=15,weight='bold'),bg='wheat',fg='black')
        ldest.place(x=20,y=130)

        bdest=Button(win,text='Save Here .',font=Font(size=14),bg='wheat',fg='black',command=dest)
        bdest.place(x=200,y=130)

        s2=StringVar()
        edest=Entry(win,textvariable=s2,width=30,font=Font(size=14),state=DISABLED,bg='wheat',fg='black')
        edest.place(x=20,y=175)

        ltheme=Label(win,text='Theme : ',font=Font(size=15,weight='bold'),bg='wheat',fg='black')
        ltheme.place(x=20,y=220)
        r=IntVar()
        r1=Radiobutton(win,text='Light',font=Font(size=14),value=1,variable=r,bg='wheat',fg='black')
        r1.place(x=125,y=220)
        r2=Radiobutton(win,text='Dark',font=Font(size=14),value=2,variable=r,bg='wheat',fg='black')
        r2.place(x=210,y=220)
        bok=Button(win,text='OK',font=Font(size=14,weight='bold'),command=mode,bg='wheat',fg='black')
        bok.place(x=300,y=215)

        bconv=Button(win,text='Convert',font=Font(size=14),bg='wheat',fg='black',relief='groove',command=conv)
        bconv.place(x=30,y=280)
        bclr=Button(win,text='Clear',font=Font(size=14),relief='groove',bg='wheat',fg='black',command=clr)
        bclr.place(x=180,y=280)
        bex=Button(win,text='Exit',font=Font(size=14),relief='groove',bg='wheat',fg='black',command=ex)
        bex.place(x=300,y=280)

        lcrdt=Label(win,text='Created By- Sagar Vishwakarma',fg='blue',bg='wheat',font=Font(weight='bold',size=9))
        lcrdt.place(x=188,y=330)
        lmail=Label(win,text='E-Mail:- sagarvishwakarma4200@gmail.com',font=Font(size=9,weight='bold'),fg='blue',bg='wheat')
        lmail.place(x=120,y=353)
        
        

        win.resizable(False,False)
        win.mainloop()
        
        main()

 ############################################
    frm=Frame(root,bg='orange',relief='sunken',bd=0)


    lb=Label(frm,text='Image 2 PDF',bg='orange',fg='green',font=Font(size=11,weight='bold'))
    lb.pack(anchor=CENTER)

    close1=Button(frm,text='X',bg='orange',highlightbackground='white',font=Font(size=10,weight='bold'),width=2,relief='flat',command=root.destroy)
    close1.place(x=357,y=0)

    min1=Button(frm,text='-',bg='orange',highlightbackground='white',font=Font(size=10,weight='bold'),width=2,relief='flat',command=mini1)
    min1.place(x=332,y=0)


    frm.pack(fill=X)
    
    ###########    Buttons   ###################

    bcont=Button(root,image=icont,command=prog)
    bcont.place(x=90,y=370)

    lbx=Label(root,text='Created By:- Sagar Vishwakarma',font=Font(size=11,weight='bold'),bg='black',fg='brown').place(x=150,y=460)

    lbc=Label(root,text='Contact Me:- +91 7234834592',font=Font(size=11,weight='bold'),bg='black',fg='brown').place(x=150,y=500)
    ###########################################
    frm.bind('<Map>',show1)
    frm.bind('<B1-Motion>',move1)

    root.resizable(False,False)
    root.mainloop()
main()
