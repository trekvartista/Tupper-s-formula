from tkinter import *

from tkinter import filedialog

from PIL import Image, ImageTk


root = Tk()
  
# Set Title as Image Loader 
root.title("Image Loader") 
  
# Set the resolution of window 
root.geometry("600x400") 
  
# Allow Window to be resizable 
root.resizable(width = True, height = False) 
  
file_name = 'Файл не выбран'

# Main image to be pixelized
image = None

l = Label(root, text ='File name:')

T = Label(root, text = file_name)

l.grid(row = 1, column = 1);
T.grid(row = 2, column = 1);


def open_img():

    global image

    # Select the Imagename  from a folder  
    x = openfilename()

    file_name = x

    T = Label(root, text =file_name)
    T.grid(row = 2, column = 1);
  
    # opens the image 
    img = Image.open(x)
    image = img.convert("1")
    pixelize(image)
      
    # resize the image and apply a high-quality down sampling filter 
    img = img.resize((444, 250), Image.ANTIALIAS) 
  
    # PhotoImage class is used to add image to widgets, icons etc 
    img = ImageTk.PhotoImage(img) 
   
    # create a label 
    panel = Label(root, image = img) 
      
    # set the image as img  
    panel.image = img 
    # panel.grid(row = 4, column = 1)


def openfilename(): 
  
    # open file dialog box to select image 
    # The dialogue box has a title "Open" 
    filename = filedialog.askopenfilename(title ='Open')
    return filename 


# Create a button and place it into the window using grid layout 
btn = Button(root, text ='load image', command = open_img).grid(row = 3, column = 1)

def pixelize(image):

    byteset = ""

    for x in range(105,-1,-1):
        for y in range(0,17):
            if image.getpixel((x,y)) > 127:
                byteset += '1'
            else:
                byteset += '0'

    k = int(byteset,2)*17
    print("Все готово:")
    print(k)

root.mainloop() 
