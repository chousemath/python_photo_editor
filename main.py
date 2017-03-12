import tkinter
from tkinter import Label
from PIL import Image, ImageFilter, ImageTk

# Some general setup code for the entire app
window = tkinter.Tk()
window.title("Python Photo Editor")
window.geometry("500x500")

# Code to add tkinter widgets will go here

# image import code
test_image = Image.open('test1.jpg')
test_photo = ImageTk.PhotoImage(test_image)
test_photo_label = Label(image=test_photo)
test_photo_label.image = test_photo
test_photo_label.pack()

window.mainloop()
