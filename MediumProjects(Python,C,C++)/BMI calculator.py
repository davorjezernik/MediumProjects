#This program was made in Croatia for my course
from tkinter import *
from tkinter.ttk import Combobox

#Funkcija za izracun tjelesne mase
def iitm():
    os = (cb.get())
    g = int(u3.get())#Godine
    v = int(u2.get())/100#Visina
    t = int(u1.get())#Kg
    if os == 'Musko':
        bmi = (t/v**2)*1.1
        if g < 18:
            bmi=bmi-0.1
    else:
        bmi = (t/v**2)*0.9
        if g < 18:
            bmi=bmi-0.1
    if os == 'Musko':
        if bmi < 20:
            opis='Podhranjen'
        elif 20<=bmi<25:
            opis='Idealno'
        elif 25<=bmi<30:
            opis='Prekomjerno'
        elif 30<=bmi<40:
            opis='Pretilost'
        else:
            opis='Jaka pretilost'
    else:
        if bmi < 20:
            opis='Podhranjen'
        elif 19<=bmi<24:
            opis='Idealno'
        elif 24<=bmi<30:
            opis='Prekomjerno'
        elif 30<=bmi<40:
            opis='Pretilost'
        else:
            opis='Jaka pretilost'

    izracun_bmi=Label(p,text='Vas BMI iznosi: '  +  str(bmi)  +  str(opis))
    izracun_bmi.place(x=70,y=300)



#Window
p = Tk()
p.geometry('400x350+800+300')
p.title('BMI Calculator')
p.configure(bg='grey')

#Tekst
#KG
l1 = Label(p, text='Write youre kg:',
 fg='black', bg='grey')
l1.place(x=30,y=50)
#Height
l2 = Label(p, text='Youre height in cm:',
 fg='black', bg='grey')
l2.place(x=30,y=100)
#Gender
l3 = Label(p, text='Chose M or W:',
 fg='black', bg='grey')
l3.place(x=30,y=150)
#Age
l4 = Label(p, text='Youre age:',
 fg='black', bg='grey')
l4.place(x=30,y=200)

#Unos polja
#Type youre kg
u1 = Entry(p, width=10, bg='white')
u1.place(x=160,y=53)
#Type youre height
u2 = Entry(p, width=10, bg='white')
u2.place(x=160,y=103)
#Type youre age
u3 = Entry(p, width=10, bg='white')
u3.place(x=160,y=203)

#ComboBox
#Chose gender
data=('Musko','Zensko')
cb=Combobox(p,values=data)
cb.place(x=160,y=153)

#Button for calculation
g1=Button(p,bd=5, text='Izracunaj', bg='grey', command= iitm)
g1.place(x=160,y=243,width=90,height=40)


p.mainloop()