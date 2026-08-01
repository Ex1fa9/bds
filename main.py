import tkinter as tk
import random, time
from PIL import Image, ImageTk, ImageSequence

root = tk.Tk()

root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.bind("<F8>", lambda e: root.destroy())
root.bind("<Alt-F4>", lambda e: "break")

canvas = tk.Canvas(root, bg="#0379d9", highlightthickness=0)
canvas.pack(fill="both", expand=True)

x, y = root.winfo_screenwidth()//6, root.winfo_screenheight()//4

sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()

nums = [0, 1, 7, 14, 23, 34, 42, 47, 52, 58, 67, 69, 72, 85, 92, 99, 100, 101, 1488]

#===== изоброжения =====#

img = Image.open("qr.jpg")
img = img.resize((150, 150))
photo = ImageTk.PhotoImage(img)

cat_g = Image.open("cat.gif")
catframe = [ImageTk.PhotoImage(f.copy()) for f in ImageSequence.Iterator(cat_g)]
index1 = 0
img1 = canvas.create_image(x//10, y*1.9, image=catframe[0], anchor="nw", state="hidden")

posxalko = Image.open("posxalko.gif")
posxalkoframe = [ImageTk.PhotoImage(f.copy()) for f in ImageSequence.Iterator(posxalko)]
index2 = 0
img2 = canvas.create_image(x*4, y//4, image=posxalkoframe[0], anchor="nw", state="hidden")

gifs = []
for _ in range(67):
    img_id = canvas.create_image(random.randint(0, sw), random.randint(0, sh), image=catframe[0], anchor="center", state="hidden")
    gifs.append({"id": img_id, "frames": catframe, "frame": 0})
 
    img_id = canvas.create_image(random.randint(0, sw), random.randint(0, sh), image=posxalkoframe[0], anchor="center", state="hidden")
    gifs.append({"id": img_id, "frames": posxalkoframe, "frame": 0})


#===== изоброжения =====#


progress = canvas.create_text(x//2, y*2.4, text="0% завершить", fill="white", font=("Segoe UI", 32), anchor="nw")

def animate():
    for gif in gifs:
        gif["frame"] = (gif["frame"] + 1) % len(gif["frames"])
        canvas.itemconfig(gif["id"], image=gif["frames"][gif["frame"]])
 
    root.after(50, animate)

def show_easter_egg():
    canvas.itemconfig(progress, text="1488% завершить ЧТООО???? ПОСХАЛКООООО????")

    canvas.itemconfig(img1, state="normal")
    canvas.itemconfig(img2, state="normal")

    for gif in gifs:
        canvas.itemconfig(gif["id"], state="normal")

    animate()

def update(i=0):
    if i >= len(nums):
        return

    canvas.itemconfig(progress, text=f"{nums[i]}% завершить")

    if nums[i] == 1488:
        root.after(3000, show_easter_egg)
    else:
        root.after(3000, update, i + 1)

update()

canvas.create_text(x//2, y//4, text=":(", fill="white", font=("Segoe UI", 200), anchor="nw")

canvas.create_text(x//2, y*1.6, text="На вашем ПК возникла проблема, и его необходимо перезагрузить.", fill="white", font=("Arial", 32), anchor="nw")
canvas.create_text(x//2, y*1.8, text="Мы лишь собираем некоторые сведения об ошибке, а затем будет", fill="white", font=("Arial", 32), anchor="nw")
canvas.create_text(x//2, y*2, text="автоматически выполнена перезагрузка.", fill="white", font=("Arial", 32), anchor="nw")


canvas.create_image(x//2, y*2.8, image=photo, anchor="nw")
canvas.create_text(x*1.1, y*2.78, text="Дополнительные сведения об этой проблеме и возможных способах ее решения см. на странице", fill="white", font=("Arial", 18), anchor="nw")
canvas.create_text(x*1.1, y*2.92, text="https://www.windows.com/stopcode", fill="white", font=("Arial", 18), anchor="nw")
canvas.create_text(x*1.1, y*3.12, text="При обращении в службу поддержки предоставьте следующие данные:", fill="white", font=("Arial", 18), anchor="nw")
canvas.create_text(x*1.1, y*3.26, text="Код остановки: KMODE EXCEPTION NOT HANDLED", fill="white", font=("Arial", 18), anchor="nw")


root.mainloop()