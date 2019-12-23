from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import datetime
import webbrowser



root = Tk()
backgroundColor_lg = IntVar()
backgroundColor = "#597da3"
font = "Times"
color_fg = "White"
bg = backgroundColor
root.configure(background=bg)
root.resizable(width=False, height=False)
root.title("Помощник для школьника")




def check_pass():
    if name.get() == "EgorLedyaev" and password.get() == "qetuowryip" or name.get() == "Antoshka" and password.get() == "88005553535":
        messagebox.showinfo("Успешный вход", "Добро пожаловать, " + name.get())
        next_pass()
    elif name.get() == "" and password.get() == "":
        messagebox.showwarning("Внимание","Вы забыли написать никнейм и пароль")
    elif name.get() == "":
        messagebox.showwarning("Внимание","Вы забыли написать никнейм")
    elif password.get() == "":
        messagebox.showwarning("Внимание","Вы забыли написать пароль")
    else:
        messagebox.showerror("Ошибка","Проверьте правильность никнейма и пароля")

def create_main_menu():
    main_menu.entryconfig(3,state=DISABLED)
    btn_lessons.grid(row=0, column=0, padx=5, pady=5)
    btn_ollympiads.grid(row=1, column=0, padx=5, pady=5)
    btn_homework.grid(row=2, column=0, padx=5, pady=5)
    #btn_debts.grid(row=3, column=0, padx=5, pady=5)

def delete_main_menu():
    main_menu.entryconfig(3,state=NORMAL)
    btn_lessons.grid_remove()
    btn_ollympiads.grid_remove()
    btn_homework.grid_remove()
    #btn_debts.grid_remove()

def change_bg_white():
    backgroundColor = "#597da3"
    bg = backgroundColor
    color_fg = "White"
    root.configure(background=bg)
    name_entry.configure(background=bg,fg=color_fg)
    name_label.configure(background=bg,fg=color_fg)
    surname_entry.configure(background=bg,fg=color_fg)
    surname_label.configure(background=bg,fg=color_fg)
    message_button.configure(background=bg,fg=color_fg)
    btn_lessons.configure(background=bg,fg=color_fg)
    btn_ollympiads.configure(background=bg)
    btn_homework.configure(background=bg,fg=color_fg)
    #btn_debts.configure(background=bg,fg=color_fg)
    history_8_1.configure(background=bg,font=font)
    history_8_2.configure(background=bg,font=font)
    physics_16.configure(background=bg,font=font)
    informatics_10_1.configure(background=bg,font=font)
    informatics_10_2.configure(background=bg,font=font)
    pe_1.configure(background=bg,font=font)
    olympiad_1.configure(background=bg,font=font)
    olympiad_2.configure(background=bg,font=font)
    olympiad_3.configure(background=bg,font=font)
    olympiad_4.configure(background=bg,font=font)
      
    history_8_1_hw.configure(background=bg,font=font)   
    history_8_2_hw.configure(background=bg,font=font)
    physics_16_hw.configure(background=bg,font=font)   
    informatics_10_1_hw.configure(background=bg,font=font)   
    informatics_10_2_hw.configure(background=bg,font=font)   
    pe_1_hw.configure(background=bg,font=font)  

def change_bg_gray():
    backgroundColor = "#333335"
    bg = backgroundColor
    color_fg = "#fefefe"
    root.configure(background=bg)
    name_entry.configure(background=bg,fg=color_fg)
    name_label.configure(background=bg,fg=color_fg)
    surname_entry.configure(background=bg,fg=color_fg)
    surname_label.configure(background=bg,fg=color_fg)
    message_button.configure(background=bg,fg=color_fg)
    btn_lessons.configure(background=bg,fg=color_fg)
    btn_ollympiads.configure(background=bg)
    btn_homework.configure(background=bg,fg=color_fg)
    #btn_debts.configure(background=bg,fg=color_fg)
    history_8_1.configure(background=bg,font=font)
    history_8_2.configure(background=bg,font=font)
    physics_16.configure(background=bg,font=font)
    informatics_10_1.configure(background=bg,font=font)
    informatics_10_2.configure(background=bg,font=font)
    pe_1.configure(background=bg,font=font)
    olympiad_1.configure(background=bg,font=font)
    olympiad_2.configure(background=bg,font=font)
    olympiad_3.configure(background=bg,font=font)
    olympiad_4.configure(background=bg,font=font)
      
    history_8_1_hw.configure(background=bg,font=font)   
    history_8_2_hw.configure(background=bg,font=font)
    physics_16_hw.configure(background=bg,font=font)   
    informatics_10_1_hw.configure(background=bg,font=font)   
    informatics_10_2_hw.configure(background=bg,font=font)   
    pe_1_hw.configure(background=bg,font=font)   

def change_font_times():
    font = "Times"
    name_entry.configure(font=font)
    name_label.configure(font=font)
    surname_entry.configure(font=font)
    surname_label.configure(font=font)
    message_button.configure(font=font)
    btn_lessons.configure(font=font)
    btn_ollympiads.configure(font=font)
    btn_homework.configure(font=font)
    #btn_debts.configure(font=font)
    history_8_1.configure(font=font)
    history_8_2.configure(font=font)
    physics_16.configure(font=font)
    informatics_10_1.configure(font=font)
    informatics_10_2.configure(font=font)
    pe_1.configure(font=font)
    olympiad_1.configure(font=font)
    olympiad_2.configure(font=font)
    olympiad_3.configure(font=font)
    olympiad_4.configure(font=font)
    
    history_8_1_hw.configure(font=font)
    history_8_2_hw.configure(font=font)
    physics_16_hw.configure(font=font)
    informatics_10_1_hw.configure(font=font)
    informatics_10_2_hw.configure(font=font)
    pe_1_hw.configure(font=font)

def change_font_courier():
    font = "Courier"
    name_entry.configure(font=font)
    name_label.configure(font=font)
    surname_entry.configure(font=font)
    surname_label.configure(font=font)
    message_button.configure(font=font)
    btn_lessons.configure(font=font)
    btn_ollympiads.configure(font=font)
    btn_homework.configure(font=font)
    #btn_debts.configure(font=font)
    history_8_1.configure(font=font)
    history_8_2.configure(font=font)
    physics_16.configure(font=font)
    informatics_10_1.configure(font=font)
    informatics_10_2.configure(font=font)
    pe_1.configure(font=font)
    olympiad_1.configure(font=font)
    olympiad_2.configure(font=font)
    olympiad_3.configure(font=font)
    olympiad_4.configure(font=font)
    
    history_8_1_hw.configure(font=font)
    history_8_2_hw.configure(font=font)
    physics_16_hw.configure(font=font)
    informatics_10_1_hw.configure(font=font)
    informatics_10_2_hw.configure(font=font)
    pe_1_hw.configure(font=font)

def next_pass():
    name_label.grid_remove()
    surname_label.grid_remove()
    name_entry.grid_remove()
    surname_entry.grid_remove()
    message_button.grid_remove()
    create_main_menu()
def show_timetable():
    delete_main_menu()
    history_8_1.grid(row=0, column=0, padx=5, pady=5)
    history_8_2.grid(row=1, column=0, padx=5, pady=5)
    physics_16.grid(row=2, column=0, padx=5, pady=5)
    informatics_10_1.grid(row=3, column=0, padx=5, pady=5)
    informatics_10_2.grid(row=4, column=0, padx=5, pady=5)
    pe_1.grid(row=5, column=0, padx=5, pady=5)
    

def delete_timetable():
    history_8_1.grid_remove()
    history_8_2.grid_remove()
    physics_16.grid_remove()
    informatics_10_1.grid_remove()
    informatics_10_2.grid_remove()
    pe_1.grid_remove()
    

def history_8():
    delete_timetable()
    image = Image.open("photo/1.jpg")
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo
    label.pack()

def physics_16():
    delete_timetable()
    image = Image.open("photo/2.jpg")
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo
    label.pack()

def informatics_10():
    delete_timetable()
    image = Image.open("photo/3.jpg")
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo
    label.pack()

def pe_1():
    delete_timetable()
    image = Image.open("photo/4.jpg")
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo
    label.pack()

def show_olympiads():
    delete_main_menu()
    olympiad_1.grid(row=0, column=0, padx=5, pady=5)
    olympiad_2.grid(row=1, column=0, padx=5, pady=5)
    olympiad_3.grid(row=2, column=0, padx=5, pady=5)
    olympiad_4.grid(row=3, column=0, padx=5, pady=5)
    

def delete_olympiads():
    olympiad_1.grid_remove()
    olympiad_2.grid_remove()
    olympiad_3.grid_remove()
    olympiad_4.grid_remove()

def olympiad_1():
    webbrowser.open('http://www.unn.ru/bibn/calendar/samara', new=2)
def olympiad_2():
    webbrowser.open('https://math.gs-group.com/about/', new=2)
def olympiad_3():
    webbrowser.open('http://sammat.ru/', new=2)
def olympiad_4():
    webbrowser.open('https://olymp.innopolis.ru/ooui/informatics/', new=2)
    
def exit():
    label.pack_forget()
    delete_homework()
    delete_timetable()
    delete_olympiads()
    create_main_menu()
    
def show_homework():
    delete_main_menu()
    history_8_1_hw.grid(row=0, column=0, padx=5, pady=5)
    history_8_2_hw.grid(row=1, column=0, padx=5, pady=5)
    physics_16_hw.grid(row=2, column=0, padx=5, pady=5)
    informatics_10_1_hw.grid(row=3, column=0, padx=5, pady=5)
    informatics_10_2_hw.grid(row=4, column=0, padx=5, pady=5)
    pe_1_hw.grid(row=5, column=0, padx=5, pady=5)
    
    
def delete_homework():
    history_8_1_hw.grid_remove()
    history_8_1_hw.grid_remove()
    physics_16_hw.grid_remove()
    informatics_10_1_hw.grid_remove()
    informatics_10_2_hw.grid_remove()
    pe_1_hw.grid_remove()
    
    
def author():
    messagebox.showinfo("О программе","Авторы: Никанкин Антон\n                Ледяев Егор \nВерсия: 0.9x")
    
main_menu = Menu()
settings_menu = Menu()
theme_menu = Menu()
font_menu = Menu()
font_color_menu = Menu()

main_menu.add_cascade(label="Настройки", font=font, menu=settings_menu)
main_menu.add_command(label="О программе", font=font,command=author)
main_menu.add_command(label="Вернуться", font=font,command=exit,state=DISABLED)

settings_menu.add_cascade(label="Сменить тему", font=font, menu=theme_menu)
theme_menu.add_command(label="Светлая тема", font=font, command=change_bg_white)
theme_menu.add_command(label="Темная тема", font=font, command=change_bg_gray)

settings_menu.add_cascade(label="Сменить шрифт", font=font, menu=font_menu)
font_menu.add_command(label="Times New Roman", font=font, command=change_font_times)
font_menu.add_command(label="Courier", font=font, command=change_font_courier)


root.config(menu=main_menu)

name = StringVar()
password = StringVar()

name_label = Label(text="Введите ваш никнейм:",background=bg, font=font, fg=color_fg)
surname_label = Label(text="Введите ваш пароль:",background=bg, font=font, fg=color_fg,)

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name,background=bg,fg = "White")
surname_entry = Entry(textvariable=password,background=bg,fg = "White",show="*")

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

message_button = Button(text="Войти", command=check_pass,background=bg, font=font, fg=color_fg)
message_button.grid(row=2, columnspan=2, padx=5, pady=5)

btn_lessons = Button(text="Расписание уроков",height=4,width=50,command=show_timetable,background=bg, font=font, fg=color_fg)
btn_ollympiads = Button(text="Расписание олимпиад", height=4, width=50,command=show_olympiads,background=bg, font=font, fg=color_fg)
btn_homework = Button(text="Список домашних заданий", height=4, width=50,background=bg, font=font, fg=color_fg,command = show_homework)
#btn_debts = Button(text="Список долгов", height=5, width=50)

history_8_1 = Button(text="История, 8 кабинет", height=4, width=50,command=history_8,background=bg, font=font, fg=color_fg)
history_8_2 = Button(text="История, 8 кабинет", height=4, width=50,command=history_8,background=bg, font=font, fg=color_fg)
physics_16 = Button(text="Физика, 16 кабинет", height=4, width=50,command=physics_16,background=bg, font=font, fg=color_fg)
informatics_10_1 = Button(text="Информатика, 10 кабинет", height=4, width=50,background=bg, font=font, fg=color_fg)
informatics_10_2 = Button(text="Информатика, 10 кабинет", height=4, width=50,background=bg, font=font, fg=color_fg)
pe_1 = Button(text="Физ-ра, 1 кабинет", height=4, width=50,background=bg, font=font, fg=color_fg)

olympiad_1 = Button(text="Будущие исследователи (по математике) (26 января)", height=4, width=50,command=olympiad_1,background=bg, font=font, fg=color_fg)
olympiad_2 = Button(text="Я решаю (по математике) (26 января)", height=4, width=50,command=olympiad_2,background=bg, font=font, fg=color_fg)
olympiad_3 = Button(text="САММАТ (финал) (по математике) (16 февраля)", height=4, width=50,command=olympiad_3,background=bg, font=font, fg=color_fg)
olympiad_4 = Button(text="Innopolis Open (по информатике) (23 февраля)", height=4, width=50,command=olympiad_4,background=bg, font=font, fg=color_fg)


history_8_1_hw = Label(text="История: Параграф 22", height=4, width=50,background=bg, font=font, fg=color_fg)
history_8_2_hw = Label(text="История: Параграф 22", height=4, width=50,background=bg, font=font, fg=color_fg)
physics_16_hw = Label(text="Физика: Конспект", height=4, width=50,background=bg, font=font, fg=color_fg)
informatics_10_1_hw = Label(text="Информатика: Подготовка минипроекта ", height=4, width=50,background=bg, font=font, fg=color_fg)
informatics_10_2_hw = Label(text="Информатика: Подготовка минипроекта", height=4, width=50,background=bg, font=font, fg=color_fg)
pe_1_hw = Label(text="Физ-ра: Комплекс ОРУ №2", height=4, width=50,background=bg, font=font, fg=color_fg)

label=Label()

root.mainloop()
