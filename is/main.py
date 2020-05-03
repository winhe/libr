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
window.geometry('600x400')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control) 
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Регистрация/Вход')  
tab_control.add(tab2, text='Личный кабинет',state = 'hidden')
tab_control.add(tab3, text='Личный кабинет',state = 'hidden')
# ---------------------------------1
f_center = LabelFrame(tab1,text = "registration")
f_center.pack(expand = 1)

l1 = Label(f_center,text = "login:")
l1.grid(column=0, row=0 ,sticky=W)

login = Entry(f_center)  
login.grid(column=1, row=0,columnspan = 3,sticky=W)  

l2 = Label(f_center,text = "Password:")
l2.grid(column = 0,row = 1,sticky=W)

password = Entry(f_center)  
password.grid(column=1, row=1,columnspan = 3,sticky=W) 

btn = Button(f_center, text="Регистрация", command=registration)  
btn.grid(column=1, row=2) 

btn2 = Button(f_center, text="Вход", command=au)  
btn2.grid(column=2, row=2)   

chk_state = BooleanVar() 
chk_state.set(False)
chk = Checkbutton(f_center, text='Администратор', var=chk_state)  
chk.grid(column=3, row=0)  

lbl = Label(f_center, text="")
lbl.grid(column=1, row=3) 

# ---------------------------------2
f2_top = LabelFrame(tab2,text = "enter")
f2_top.pack(anchor=W)

f2_bot = LabelFrame(tab2,text = "delete")
f2_bot.pack(anchor=W)

l3 = Label(f2_top,text = 'Студент:')
l3.grid(column = 0, row = 0,sticky = W)
who = Combobox(f2_top,width = 8)
who['values'] = [lo[0] for lo in loginspasw]
who.grid(column=1, row=0)  

l4 = Label(f2_top,text = 'Автор:')
l4.grid(column = 0, row = 1,sticky = W)
avtor = Entry(f2_top,width=10)
avtor.grid(column=1, row=1)

l5 = Label(f2_top,text = 'Книга:')
l5.grid(column = 0, row = 2,sticky = W)
book = Entry(f2_top,width=10)
book.grid(column=1, row=2)

l6 = Label(f2_top,text = 'Дата:')
l6.grid(column = 0, row = 3,sticky = W)
date = Entry(f2_top,width=10)
date.grid(column=1, row=3)

btn3 = Button(f2_top, text="Занести в бд", command=go)  
btn3.grid(column=0, row=4)


l7 = Label(f2_bot,text = 'Студент:')
l7.grid(column = 0, row = 0,sticky = W)

l8 = Label(f2_bot,text = 'Книга:')
l8.grid(column = 0, row = 1,sticky = W)

w = Combobox(f2_bot,width = 20)
w['values'] = [lo[0] for lo in loginspasw]
w.grid(column=1, row=0,sticky = W)

btn5 = Button(f2_bot, text="поиск", command=wat2)  
btn5.grid(column=2, row=0 ,sticky = W)  

wa2 = Combobox(f2_bot,width = 20)
wa2.grid(column=1, row=1)

btn6 = Button(f2_bot, text="убрать из бд", command=de)  
btn6.grid(column=2, row=1)

# --------------------------------3

btn4 = Button(tab3, text="Что я взял?", command=wat)  
btn4.grid(column=0, row=0)  

wa = Listbox(tab3, selectmode = SINGLE,width = 50)
wa.grid(column=0, row=1)

tab_control.pack(expand=1, fill='both') 

window.mainloop()