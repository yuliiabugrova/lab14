from tkinter import *
from random import *
from tkinter import messagebox

a = []

def mas():
    n = edit1.get()
    if not n:
        messagebox.showerror('Помилка', 'Розмірність масиву не вказана')
        return

    n = int(n)

    a.clear()
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    for i in range(n):
        a.append(randint(-50, 50))
        listbox1.insert(END, a[i])

def sort():
    n = len(a)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        if max_idx != i:
            a[i], a[max_idx] = a[max_idx], a[i]
    listbox2.delete(0, END)
    for i in range(n):
        listbox2.insert(END, a[i])

def replace_positive_with_indices():
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = i
    listbox1.delete(0, END)
    for i in a:
        listbox1.insert(END, i)

def about_author():
    messagebox.showinfo('Про автора', 'Автор: Юлія\nEmail: bugrovaula@example.com')

def problem_statement():
    messagebox.showinfo('Умова задачі', 'Замінити всі додатні елементи у масиві їх індексами.\nВідсортувати масив за спаданням методом екстремальних елементів.')

def set_light_theme():
    root['bg'] = '#e6f7ff'
    listbox1['bg'] = '#ffffff'
    listbox2['bg'] = '#ffffff'
    label1['bg'] = '#e6f7ff' 
    label1['fg'] = '#003366'
    label2['bg'] = '#e6f7ff' 
    label2['fg'] = '#003366'
    label3['bg'] = '#e6f7ff'
    label3['fg'] = '#003366'
    label4['bg'] = '#e6f7ff'
    label4['fg'] = '#003366'
    edit1['bg'] = '#ffffff'

def set_dark_theme():
    root['bg'] = '#2e2e2e'
    listbox1['bg'] = '#4d4d4d'
    listbox2['bg'] = '#4d4d4d'
    label1['bg'] = '#2e2e2e'
    label1['fg'] = '#f5f5f5'
    label2['bg'] = '#2e2e2e'
    label2['fg'] = '#f5f5f5'
    label3['bg'] = '#2e2e2e'
    label3['fg'] = '#f5f5f5'
    label4['bg'] = '#2e2e2e'
    label4['fg'] = '#f5f5f5'
    edit1['bg'] = '#4d4d4d'

def set_default_theme():
    root['bg'] = '#f0fff0'
    listbox1['bg'] = '#ffffff'
    listbox2['bg'] = '#ffffff'
    label1['bg'] = '#f0fff0'
    label1['fg'] = '#006400'
    label2['bg'] = '#f0fff0'
    label2['fg'] = '#006400'
    label3['bg'] = '#f0fff0'
    label3['fg'] = '#006400'
    label4['bg'] = '#f0fff0'
    label4['fg'] = '#006400'
    edit1['bg'] = '#ffffff'

x = y = 0

def do_popup(event):
    global x, y
    x = event.x
    y = event.y
    popupmenu.post(event.x_root, event.y_root)

root = Tk()
root.title('Масиви')
root.geometry('600x300')

label1 = Label(text='Вихідний масив')
label2 = Label(text='Посортований масив')
label1.place(x=20, y=30)
label2.place(x=200, y=30)

listbox1 = Listbox(height=10, width=20)
listbox2 = Listbox(height=10, width=20)
listbox1.place(x=20, y=70)
listbox2.place(x=200, y=70)

label3 = Label(text='Кількість елементів масиву:')
label3.place(x=400, y=30)

edit1 = Entry()
edit1.place(x=400, y=70)

button1 = Button(text='Заповнити', width=20, command=mas)
button1.place(x=400, y=100)

button2 = Button(text='Сортувати', width=20, command=sort)
button2.place(x=400, y=130)

button3 = Button(text='Замінити додатні на індекси', width=20, command=replace_positive_with_indices)
button3.place(x=400, y=160)

label4 = Label(text='')
label4.place(x=400, y=210)

# Головне меню
main_menu = Menu(root)
root.config(menu=main_menu)

array_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Дії з масивом', menu=array_menu)
array_menu.add_command(label='Заповнити', command=mas)
array_menu.add_command(label='Сортувати', command=sort)
array_menu.add_command(label='Замінити додатні на індекси', command=replace_positive_with_indices)

about_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Про програму', menu=about_menu)
about_menu.add_command(label='Про автора', command=about_author)
about_menu.add_command(label='Умова задачі', command=problem_statement)

popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label="Світлий", command=set_light_theme)
popupmenu.add_command(label="Темний", command=set_dark_theme)
popupmenu.add_command(label="Відновити початкові кольори", command=set_default_theme)
root.bind("<Button-3>", do_popup)

root.mainloop()