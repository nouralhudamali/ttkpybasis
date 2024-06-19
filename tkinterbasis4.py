from tkinter import*
#-- adding frames -- 13th June , 10:39p.m 

window = Tk()
window.geometry('400x300+250+150')
window.configure (background='powder blue')
window.title('Nouralhuda Learning TK')

myName = StringVar()
myAge = StringVar()
#--adding str var linked to command in the btn which def 'db functions'

def getInfo():
    myName.set('Abdelkrim')
    #myAge.set('32')
    #I think set here to set the str var into the label /adding some dimands with the command of the btn instead '32'
    var_age = int(age.get())
    result = var_age * 2
    myAge.set(result) #didnt use .set at first run
   #extra I want to be able to press th btn or do the command with entre /Homework
   #the issue in the mainloop still ggoinig to rerun and stay on previous run 


frame1=Frame(window,width=180,height=120,bg='green',bd=4,relief='raise')
frame1.place(x=20,y=15)

myLabel1 = Label(frame1,font=('Times',12,'bold'),bg='yellow', fg='black',text='Name')
myLabel1.place(x=5,y=5) 

myLabel2 = Label(frame1,font=('Times',12,'bold'),bg="yellow",fg='black',text='Age')
myLabel2.place(x=5,y=40)

name = Entry(frame1,width=10,font=('Times',12,'bold'),textvariable=myName,bg='orange',fg='black',bd=4,justify='center')
name.place(x=60,y=5) 
age = Entry(frame1,width=10,font=('Times',12,'bold'),textvariable=myAge,bg='orange',fg='black',bd=4,justify='center')
age.place(x=60,y=40) 
#first fixing of sizing want sucess the 2nd fix went well directly
#adding button 
#extra my own aadition btn inside the frame let's check if all the video done first 
btn_submit = Button(window,width=10,font=('Times',12,'bold'),bd=4,text='Submit',bg='sea green',fg='gold',padx=4,pady=4,command=getInfo)
btn_submit.place(x=40,y=150)

btn_submit = Button(frame1,width=5,font=('Times',12,'bold'),bd=4,text='Submit',bg='sky blue',fg='brown',padx=2,pady=2)
btn_submit.place(x=50,y=70) #finish extra work all is done only homework left to do / Alhumdallah Done all the Video 12:13 a.m 14th, June,Fri 



window.mainloop()
