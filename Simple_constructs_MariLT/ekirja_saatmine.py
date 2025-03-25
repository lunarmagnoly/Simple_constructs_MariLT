import os
import ssl
import smtplib
import imghdr
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from email.message import EmailMessage
from turtle import width
from PIL import Image, ImageTk
from tkinter import ttk

# Глобальная переменная для хранения пути к файлу
file = None

import os

def vali_pilt():
    global file
    file = filedialog.askopenfilename()
    
    max_length = 20  # Максимальная длина для имени файла
    if file:
        # Получаем базовое имя файла
        filename = os.path.basename(file)
        
        # Если длина имени файла больше максимальной, обрезаем с добавлением многоточия
        if len(filename) > max_length:
            filename = filename[:max_length] + "..."
        
        l_lisatud.configure(text=f"Lisatud: {filename}")
    else:
        l_lisatud.configure(text="Ühtegi faili pole lisatud")
    
    return file


def saada_kiri():
    try:
        kellele = entry_email.get()
        teema = entry_teema.get()
        kiri = kiri_box.get("1.0", END)

        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "mary.luna.tey@gmail.com"

        password = simpledialog.askstring("App Password", "Enter your email app password:", show="*")
        if not password:
            messagebox.showwarning("Warning", "No password entered.")
            return

        context = ssl.create_default_context()
        msg = EmailMessage()
        msg.set_content(kiri)
        msg['Subject'] = teema
        msg['From'] = sender_email
        msg['To'] = kellele

        if file:
            with open(file, 'rb') as fpilt:
                pilt = fpilt.read()
            msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))

        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()

        messagebox.showinfo("Informatsioon", "Kiri oli saadetud")

        # Очистка полей после успешной отправки
        entry_email.delete(0, END)
        entry_teema.delete(0, END)
        kiri_box.delete("1.0", END)
        # Очистка строки состояния (метка l_lisatud)
        l_lisatud.configure(text="Ühtegi faili pole lisatud")

        

    except Exception as e:
        messagebox.showerror("Tekkis viga!", str(e))

def aken_grid():
    global entry_email, entry_teema, kiri_box, l_lisatud

    aken = Tk()
    aken.geometry("800x600")
    aken.title("E-kirja saatmine")
    aken.resizable(False, False)

    # Загружаем и уменьшаем изображение
    bg_image = Image.open("letter.jpg")  # Загружаем оригинальное изображение
    bg_image = bg_image.resize((800, 600), Image.LANCZOS)  # Уменьшаем до 800x600 пикселей
    bg_photo = ImageTk.PhotoImage(bg_image)  # Конвертируем в формат Tkinter

    # Создаем Canvas
    canvas = Canvas(aken, width=800, height=600)
    canvas.pack()

    # Размещаем уменьшенное изображение без растяжения
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Получаем цвет фона canvas, чтобы использовать его в стиле ttk.Label
    canvas_bg = canvas.cget('bg')  

    # Создаем стиль для ttk.Label с таким же фоном
    style = ttk.Style()
    style.configure('Transparent.TLabel', background=canvas_bg)

    # Create all widgets on the canvas
    lbl_email = ttk.Label(canvas, text="Email:", font=("Arial", 16), width=7, style='Transparent.TLabel', anchor="center")
    canvas.create_window(259, 100, anchor="nw", window=lbl_email)

    entry_email = Entry(canvas, font=("Arial", 16), width=26, highlightthickness=0, bd=1, bg="white")
    canvas.create_window(357, 100, anchor="nw", window=entry_email)

    lbl_teema = ttk.Label(canvas, text="Teema:", font=("Arial", 16), width=7, style='Transparent.TLabel', anchor="center")
    canvas.create_window(259, 160, anchor="nw", window=lbl_teema)

    entry_teema = Entry(canvas, font=("Arial", 16), width=26, highlightthickness=0, bd=1, bg="white")
    canvas.create_window(357, 160, anchor="nw", window=entry_teema)

    lbl_kiri = ttk.Label(canvas, text="Kiri:", font=("Arial", 16), width=45, style='Transparent.TLabel', anchor="center")
    canvas.create_window(130, 270, anchor="nw", window=lbl_kiri)

    kiri_box = Text(canvas, font=("Arial", 16), width=45, height=7, highlightthickness=0, bd=1, bg="white")
    canvas.create_window(130, 300, anchor="nw", window=kiri_box)

    btn_lisa_pilt = Button(canvas, text="Lisa", font=("Arial", 16), fg="white", bg="#74a490", bd=0, command=vali_pilt, width=7)
    canvas.create_window(260, 210, anchor="nw", window=btn_lisa_pilt)

    l_lisatud = ttk.Label(canvas, text="Ühtegi faili pole lisatud", font=("Arial", 16), foreground="#fa3e40", style='Transparent.TLabel',width=26)
    canvas.create_window(357, 215, anchor="nw", window=l_lisatud)

    btn_saada_kiri = Button(canvas, text="Saada Kiri", font=("Arial", 16), fg="white", bg="#74a490", bd=0, command=saada_kiri, width=10)
    canvas.create_window(339, 490, anchor="nw", window=btn_saada_kiri)

    

    aken.mainloop()

aken_grid()