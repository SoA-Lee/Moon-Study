#윈도우를 생성하고 윈도우 안에 캔버스 생성

from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk( )

x=input("가로의 길이: ")
y=input("세로의 길이: ")
canvas = tk.Canvas(window, width=x, height=y)
canvas.pack( )

img = Image.open("cat.jpg")
rimg=img.rotate(180)
tk_img = ImageTk.PhotoImage(rimg)

w=int(x)/2
h=int(y)/2

canvas.create_image(w, h, image=tk_img)

window.mainloop( )