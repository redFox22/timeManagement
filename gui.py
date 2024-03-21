import csv
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import time
import csv
from datetime import datetime
import os
from datetime import datetime

current_folder_path = os.getcwd()
print(current_folder_path)
ASSETS_PATH = current_folder_path + "\\assets\\frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class TimeManagement:

    
    def __init__(self, root):
        self.root = root
        self.root.title("ITeD")
        self.timers = {"Assistenza": 0, "Aree_Esistenti": 0, "Organizzazioni": 0, "Sito_internet" : 0, "Pausa": 0, "Corso": 0}
        self.current_timer = None
        self.start_time = None
        self.active_button = None
        self.button_images = {}
        self.start_session = datetime.now()

    def seconds_to_minutes(self, secondi):
        minuti = secondi / 60
        return minuti
    
    def start_timer(self, category):
        if self.current_timer:
            self.timers[self.current_timer] +=  self.seconds_to_minutes(time.time() - self.start_time)
        self.current_timer = category
        self.start_time = time.time()

    def end_day(self):
        if self.current_timer:
            self.timers[self.current_timer] += time.time() - self.start_time
            self.timers[self.current_timer] = self.seconds_to_minutes(self.timers[self.current_timer])
            self.current_timer = None
        messagebox.showinfo("Riepilogo Giornaliero", "\n".join(f"{k}: {v} minuti" for k, v in self.timers.items()))
        self.active_button.config(image=self.button_images[self.active_button])
        filename = f"ITeD-giornata_lavorativa.{datetime.now().strftime('%Y%m%d')}.csv"
        file_exists = os.path.isfile(filename)
        with open(filename, 'a', newline='') as csvfile: 
            writer = csv.writer(csvfile)
            end_session_str = f"Sessione terminata il {datetime.now().strftime('%d/%m/%Y')} alle ore {datetime.now().strftime('%H:%M')}"
            start_session_str = f"Sessione iniziata il {self.start_session.strftime('%d/%m/%Y')} alle ore {datetime.now().strftime('%H:%M')}"
            if not file_exists:
                writer.writerow(['Categoria', 'Tempo (minuti)'])
            writer.writerow(start_session_str)
            for category, time_spent in self.timers.items():
                writer.writerow([category, time_spent])
            writer.writerow(end_session_str)
        self.timers = {k: 0 for k in self.timers}
    
    def change_button_image(self, new_active_button, default_image, active_image):
        print("E' stato cliccato il bottone " + str(new_active_button))
        if new_active_button not in self.button_images:
            self.button_images[new_active_button] = default_image
        if self.active_button and self.active_button != new_active_button:
            self.active_button.config(image=self.button_images[self.active_button])
        new_active_button.config(image=active_image)
        self.active_button = new_active_button



window = Tk()

window.geometry("1026x529")
window.configure(bg = "#FFFFFF")
time_manager = TimeManagement(window)

def button_click(button, category, default_image, active_image):
    time_manager.change_button_image(button, default_image, active_image)
    time_manager.start_timer(category)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 529,
    width = 1026,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1026.0,
    529.0,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    1026.0,
    57.0,
    fill="#083D77",
    outline="")

canvas.create_text(
    78.0,
    9.0,
    anchor="nw",
    text="Ufficio Innovazione Tecnologica e Digitalizzazione ",
    fill="#FFFFFF",
    font=("TitilliumWeb Bold", 25 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    42.0,
    28.0,
    image=image_image_1
)

button_1_pressed = PhotoImage(file=relative_to_assets("button_1_pressed.png"))

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(button_1, "Assistenza", button_image_1, button_1_pressed),
    relief="flat"
)
button_1.place(
    x=82.0,
    y=105.0,
    width=208.0,
    height=105.0
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: time_manager.end_day(),
    relief="flat"
)
button_2.place(
    x=288.0,
    y=403.0,
    width=450.0,
    height=105.0
)

button_3_pressed = PhotoImage(file=relative_to_assets("button_3_pressed.png"))
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(button_3, "Organizzazioni", button_image_3, button_3_pressed),
    relief="flat"
)
button_3.place(
    x=80.0,
    y=249.0,
    width=208.0,
    height=105.0
)

button_4_pressed = PhotoImage(file=relative_to_assets("button_4_pressed.png"))
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(button_4, "Aree_Esistenti", button_image_4, button_4_pressed),
    relief="flat"
)
button_4.place(
    x=738.0,
    y=105.0,
    width=208.0,
    height=105.0
)

button_5_pressed = PhotoImage(file=relative_to_assets("button_5_pressed.png"))
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(button_5, "Sito_internet", button_image_5, button_5_pressed),
    relief="flat"
)
button_5.place(
    x=738.0,
    y=249.0,
    width=208.0,
    height=105.0
)

button_6_pressed = PhotoImage(file=relative_to_assets("button_6_pressed.png"))
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(button_6, "Corso", button_image_6, button_6_pressed),
    relief="flat"
)
button_6.place(
    x=409.0,
    y=105.0,
    width=208.0,
    height=105.0
)

button_7_pressed = PhotoImage(file=relative_to_assets("button_7_pressed.png"))
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(button_7, "Pausa", button_image_7, button_7_pressed),
    relief="flat"
)
button_7.place(
    x=409.0,
    y=254.0,
    width=208.0,
    height=105.0
)

window.resizable(False, False)
window.mainloop()
