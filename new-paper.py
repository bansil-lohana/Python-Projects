from tkinter import *
from PIL import Image, ImageTk

def every_100(text):
    # Helper function to format or chunk the text
    return text

root = Tk()
root.title("CodeWithHarry News - Aapka Apna Akhabaar")
root.geometry("1000x800")

texts = []
photos = []

for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
        
    image = Image.open(f"{i+1}.png")
    # TODO: Resize these images if necessary
    photos.append(ImageTk.PhotoImage(image))

# Frame 1
f1 = Frame(root, width=900, height=200)
Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")

# Frame 2
f2 = Frame(root, width=900, height=200)
Label(f2, text=texts[1], padx=22, pady=22).pack(side="left")
Label(f2, image=photos[1], anchor="e").pack()
f2.pack(anchor="w")

# Frame 3
f3 = Frame(root, width=900, height=200)
Label(f3, text=texts[2], padx=22, pady=22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()