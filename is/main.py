from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Combobox
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

loginspasw = [row for row in cursor.execute("SELECT * FROM userss ORDER by login")]

print(loginspasw)

def registration():
	log = login.get()
	pas = password.get()
	a = chk_state.get()
	cursor.execute("INSERT INTO userss VALUES (?,?,?)",[log,pas,str(int(a))])
	conn.commit()

def au():
	a = chk_state.get()
	log = login.get()
	pas = password.get()

	if (log,pas,a) in loginspasw:
		lbl.configure(text='welcome')
		if a:
			tab_control.tab(tab2,state = 'normal')
		else:
			tab_control.tab(tab3,state = 'normal')
	else:
		lbl.configure(text='Не верно')

def go():
	cursor.execute("INSERT INTO books2 VALUES (?,?,?,?)",[who.get(),avtor.get(),book.get(),date.get()])
	conn.commit()

def wat():
	wa.delete(END)
	log = login.get()
	my_books = [b for b in cursor.execute("SELECT * FROM books2 WHERE who =?",[log])]
	for mb in my_books:
		wa.insert(END,mb[1:])

def wat2():
	ww = w.get()
	w_books = [b for b in cursor.execute("SELECT * FROM books2 WHERE who =?",[ww])]
	wa2['values'] = [wb[2:3] for wb in w_books]

def de():
	cursor.execute("DELETE FROM books2 WHERE who = ? AND book = ?",[w.get(),wa2.get()])
	conn.commit()

window = Tk()
window.title("biblioteka")
window.geometry('800x600')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control) 
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Регистрация/Вход')  
tab_control.add(tab2, text='Личный кабинет',state = 'hidden')
tab_control.add(tab3, text='Личный кабинет',state = 'hidden')
# ---------------------------------1
l1 = Label(tab1,text = "login")
l1.grid(column = 0,row = 0)

login = Entry(tab1,width=10,textvariable = 'login')  
login.grid(column=0, row=1)  

l2 = Label(tab1,text = "Password")
l2.grid(column = 1,row = 0)

password = Entry(tab1,width=10)  
password.grid(column=1, row=1) 

btn = Button(tab1, text="Регистрация", command=registration)  
btn.grid(column=2, row=1) 

btn2 = Button(tab1, text="Вход", command=au)  
btn2.grid(column=3, row=1)   

chk_state = BooleanVar() 
chk_state.set(False)
chk = Checkbutton(tab1, text='Администратор', var=chk_state)  
chk.grid(column=4, row=1)  

lbl = Label(tab1, text="")
lbl.grid(column=1, row=3) 

# ---------------------------------2

l3 = Label(tab2,text = 'Кто взял')
l3.grid(column = 0, row = 0)
who = Combobox(tab2,width = 10)
who['values'] = [lo[0] for lo in loginspasw]
who.grid(column=0, row=1)  

l4 = Label(tab2,text = 'Автор')
l4.grid(column = 1, row = 0)
avtor = Entry(tab2,width=10)
avtor.grid(column=1, row=1)

l5 = Label(tab2,text = 'Книга')
l5.grid(column = 2, row = 0)
book = Entry(tab2,width=10)
book.grid(column=2, row=1)

l6 = Label(tab2,text = 'Дата')
l6.grid(column = 3, row = 0)
date = Entry(tab2,width=10)
date.grid(column=3, row=1)

btn3 = Button(tab2, text="Занести в бд", command=go)  
btn3.grid(column=4, row=1)


l7 = Label(tab2,text = 'Кто?')
l7.grid(column = 0, row = 2)

w = Combobox(tab2,width = 10)
w['values'] = [lo[0] for lo in loginspasw]
w.grid(column=0, row=3)

btn5 = Button(tab2, text="поиск", command=wat2)  
btn5.grid(column=1, row=3)  

wa2 = Combobox(tab2,width = 20)
wa2.grid(column=2, row=3)

btn6 = Button(tab2, text="убрать из бд", command=de)  
btn6.grid(column=3, row=3)

# --------------------------------3

btn4 = Button(tab3, text="Что я взял?", command=wat)  
btn4.grid(column=0, row=0)  

wa = Listbox(tab3, selectmode = SINGLE,width = 50)
wa.grid(column=0, row=1)

tab_control.pack(expand=1, fill='both') 

window.mainloop()