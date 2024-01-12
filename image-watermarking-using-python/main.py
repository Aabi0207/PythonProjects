from tkinter import *
from tkinter import filedialog
from PIL import ImageFont, ImageDraw, Image, ImageTk

image_path = None
BACKGROUND_COLOR = "#85E6C5"


def watermark(text):
    global image_path
    image_path = filedialog.askopenfilename()
    text = text.get("1.0", END)
    watermark_image = Image.open(image_path)

    w, h = watermark_image.size
    x, y = int(w / 2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    font = ImageFont.truetype("arial.ttf", int(font_size/6))

    draw = ImageDraw.Draw(watermark_image)

    draw.text((x, y), text, fill="white", font=font, anchor='ms')

    result_image = Image.new('RGBA', watermark_image.size)
    result_image.paste(watermark_image, (0, 0))
    result_image.show()


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Image watermarking")

canvas = Canvas(width=800, height=526)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="img/card_back.png")
background_img = canvas.create_image(400, 263, image=card_back_img)
word_text = canvas.create_text(400, 50, text="Text Watermarking using Python", fill='white', font=("Arial", 35, "bold"))
watermark_text = canvas.create_text(400, 150, text="what should be the watermark text", fill='white', font=("Arial", 25, "italic"))
select_file = canvas.create_text(400, 250, text="Select the image you want to watermark.", fill='white', font=("Arial", 25, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

select_img = Button(text='SELECT', highlightthickness=0, height=2, width=10, bg="#FFFFDD", command=lambda: watermark(textbox))
select_img.place(x=375, y=270)

textbox = Text(height=2, width=15, bg="#FFFFDD", highlightthickness=0)
textbox.place(x=350, y=170)

window.mainloop()
