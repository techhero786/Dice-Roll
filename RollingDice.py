import tkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random

#Create A Window 
window=tkinter.Tk();
window.geometry("1200x700")
window.title("Dice Roll")  #Create A Title

#Fill Background Image 
img=PhotoImage(file=r"C:\PYTHON SAHIL\redice.png")
bg_img=tkinter.Label(window, image=img)
bg_img.pack()

#Change Window Icone
img1=PhotoImage(file="C:\PYTHON SAHIL\icon dice.png")
window.iconphoto(False,img1)

#Insert Dice Images
dice=["d1.png","d2.png","d3.png","d4.png","d5.png","d6.png"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

Label1=tkinter.Label(window,image=image1)
Label2=tkinter.Label(window,image=image2)

Label1.image=image1
Label2.image=image2

Label1.place(x=70, y=100)
Label2.place(x=340, y=100)

def dice_roll():   
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    Label1.configure(image=image1)
    Label1.image=image1
    
    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    Label2.configure(image=image2)
    Label2.image=image2

# Create Button for Clicking and Rolling Dice    
button=tkinter.Button(window,text="Roll",bg="Green",fg="White",font="Times 20", command=dice_roll)
button.place(x=250, y=10)

window.mainloop()