from tkinter import *
from PIL import Image, ImageTk


def every_100(text):
    # Helper function
    return text


root = Tk()
root.title("CodeWithHarry News - Aapka Apna Akhabaar")
root.geometry("1000x800")

texts = []
photos = []

for i in range(3):

    with open(f"{i+1}.txt") as f:
        text = f.read()

    texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")

    # Resize image
    image = image.resize((200, 150))

    photos.append(ImageTk.PhotoImage(image))


# Frame 1
f1 = Frame(root, width=900, height=200)

Label(
    f1,
    text=texts[0],
    padx=22,
    pady=22,
    wraplength=600
).pack(side="left")

Label(
    f1,
    image=photos[0]
).pack(side="right")

f1.pack(anchor="w", fill="x")


# Frame 2
f2 = Frame(root, width=900, height=200)

Label(
    f2,
    text=texts[1],
    padx=22,
    pady=22,
    wraplength=600
).pack(side="left")

Label(
    f2,
    image=photos[1]
).pack(side="right")

f2.pack(anchor="w", fill="x")


# Frame 3
f3 = Frame(root, width=900, height=200)

Label(
    f3,
    text=texts[2],
    padx=22,
    pady=22,
    wraplength=600
).pack(side="left")

Label(
    f3,
    image=photos[2]
).pack(side="right")

f3.pack(anchor="w", fill="x")


root.mainloop()
