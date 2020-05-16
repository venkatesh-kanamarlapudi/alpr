from PIL import Image
import matplotlib.pyplot as plt
import pytesseract

file = open('./coordinates.txt', "r")

x = file.read()

file.close()

lst = x.split(',')

left = int(lst[0])
top = int(lst[1])
right = int(lst[2])
bottom = int(lst[3])



im = Image.open('./detected.jpg')
im1 = im.crop((left, top, right, bottom))
im1.save("cropped.jpg")



def process_image(image):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    img = Image.open("./cropped.jpg")
    img = img.convert('L')
    pix = img.load()
    plt.imshow(img)
    #plt.show()
    return pytesseract.image_to_string(img)

name = process_image("plat1.jpg")
print(name)


'''
from tkinter import *
root = Tk()
root.geometry('200x50')
root.resizable(True, True)
Label(root, text = name).grid(row = 0)
root.after(3000,lambda: root.destroy())
mainloop()'''


