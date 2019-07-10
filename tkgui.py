from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from test import *

def insertPhoto1():
    ph1 = fd.askopenfilename()
    print(ph1)
    firstPhoto.config(text=ph1)
    img = ImageTk.PhotoImage(Image.open(ph1))
 
def results():
    r = create(firstPhoto.cget('text'))
    photoResults.config(text = r)
    
root = Tk()

b1 = Button(text="Открыть первую фотографию", command=insertPhoto1)
b1.pack()

firstPhoto = Label(root)
firstPhoto.pack()

secondPhoto = Label(root)
secondPhoto.pack()

b3 = Button(text="Результат", command=results)
b3.pack()


photoResults = Label(root, height = 3, width = 50)
photoResults.pack()
root.mainloop()





