from PIL import Image as PILImage, ImageTk
from tkinter import *
from itertools import cycle


root = Tk()
root.title("Image Slideshow Viewer")


# List of image paths
image_paths = [
    r"C:\Users\N TECH\Documents\images (1).jfif",
    r"C:\Users\N TECH\Documents\images (2).jfif",
    r"C:\Users\N TECH\Documents\images.jfif",
    r"C:\Users\N TECH\Documents\images (3).jfif",
]


# Resize images
image_size = (500, 500)

images = [
    PILImage.open(path).resize(image_size)
    for path in image_paths
]

photo_images = [
    ImageTk.PhotoImage(image)
    for image in images
]


# Label to display image
label = Label(root)
label.pack()


# Create an infinite cycle of images
slideshow = cycle(photo_images)


# Function to update image
def update_image():
    photo_image = next(slideshow)

    label.config(image=photo_image)

    # Show next image after 3 seconds
    root.after(3000, update_image)


# Start slideshow
def start_slideshow():
    update_image()


# Play button
play_button = Button(
    root,
    text="Play Slideshow",
    command=start_slideshow
)

play_button.pack(side=BOTTOM)


root.mainloop()