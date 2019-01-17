# requires 'pip install pillow'
from PIL import Image as img
from PIL import ImageFilter as filter

#open an image 
im = img.open("image.jpg")

def display():
    im.show()

def blur():
    blured_im = im.filter(filter.BLUR)
    blured_im.show()

def sharp():
    sharped_im = im.filter(filter.SHARPEN)
    sharped_im.show()

def embos():
    embosed_im = im.filter(filter.EMBOSS)
    embosed_im.show()

def counter():
    counter_im = im.filter(filter.CONTOUR)
    counter_im.show()

while True:
     print("Press:1 to display the orignal image")
     print("Press:2 to apply the blur filter to image")
     print("Press:3 to apply the sharp filter to image")
     print("Press:4 to apply the emboss filter to image")
     print("Press:5 to apply the contour filter to image")
     print("Press:6 to quit..")
     choice = int(input())
     if choice==6:
       break;
     switcher = { 
        1:display, 
        2:blur, 
        3:sharp,
        4:embos,
        5:counter  
    }
     print(switcher.get(choice, "Wrong choice")())
  

