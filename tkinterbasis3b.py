#lets redo it all from the 1st video EnigmaCode
#2nd video

#BismAllah
from tkinter import*

window = Tk()
window.geometry('400x300+250+150')
window.configure (background='powder blue')
#window.title('My Application')
window.title('Nouralhuda Learning TK')

myLabel1 = Label(window,font=('Times',12,'bold'),bg='yellow', fg='black',text='Name')#bg='yellow', when deleted the volor become default /to make it as the bg of the window we put the same at the code of the label bg
#myLabel1.grid(row=0,column=1) Alhumdalah
myLabel1.place(x=10,y=10) #Alhumdallah 

myLabel2 = Label(window,font=('Times',12,'bold'),bg="yellow",fg='black',text='Age')
myLabel2.place(x=10,y=50)

name = Entry(window,width=10,font=('Times',12,'bold'),bg='orange',fg='black',bd=4,justify='center')
name.place(x=80,y=10) 
#-Ahumdallah so far so good slightly mistok comma 2 insteat one annd misspell yellow 
age = Entry(window,width=10,font=('Times',12,'bold'),bg='orange',fg='black',bd=4,justify='center')
age.place(x=80,y=50) 
#Finished Alhumd Allah only the loop issue still happining / 3:10 a.m , 13th June,2024



window.mainloop()
