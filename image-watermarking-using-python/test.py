from tkinter import *
from tkinter import filedialog
from PIL import Image

window = Tk()
window.config(padx=30, pady=20)

img=None
wtm_img=None
result_image= None

def open_img():
    global img
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail(img.size)
        # img.show()

def watermark():
    global wtm_img
    watermark_path=filedialog.askopenfilename()
    if watermark_path:
        wtm_img = Image.open(watermark_path)
        wtm_img.thumbnail((200, 200))
        # wtm_img.show()

def submit():
    global result_image
    if wtm_img != None and img !=None:
        result_image = img.copy()
        img_width,img_height = img.size
        wtm_img_width,wtm_img_height=wtm_img.size
        x_position = img_width-wtm_img_width
        y_position = img_height - wtm_img_height
        result_image.paste(wtm_img,(x_position,y_position))
        result_image.show()
def save():
    if result_image != None:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if file_path:
            result_image.save(file_path)

title = Label(text='Select an image, then it\'s watermark', pady=20, font=('Sans', 12))
title.grid(row=0, column=1, columnspan=2)

image = Button(text='Select Image', width=15, command=open_img)
image.grid(row=1, column=1)

watermark = Button(text='Select Watermark', width=15, command=watermark)
watermark.grid(row=1, column=2)


submit = Button(text='Submit', width=15, command=submit)
submit.grid(row=2, column=1, pady=5)

save= Button(text='Save', width=15, command=save)
save.grid(row=2, column=2, pady=5)

window.mainloop()
