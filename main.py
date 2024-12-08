from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("500x250")
root.title("convert")

def convert():
    celsius = c.get()
    if(celsius.replace('.','').isnumeric()):
        error.grid_forget()
        fahrenheit = (float(celsius) * 9/5)+32
        tf.config(text="temp in fahrenheit : " +str(fahrenheit))
    else:
        error.grid(row=1, column=1)


t = Label(root, text="positive celsius -> fahrenheit", font=font.Font(size=20),fg="light gray")
t.pack()

f = Frame(root)
f.pack(pady=20)

e = Label(f, text="celcius : ")
e.grid(row = 0, column = 0)

c = Entry(f)
c.grid(row = 0, column = 1)

error = Label(f, text="enter valid integer", fg="red")

tf = Label(f, font = font.Font(size = 12))
tf.grid(row = 2, column = 0, columnspan = 2, pady = 10)

cb = Button(f, text="convert", fg="white", bg="black", command=convert)
cb.grid(row = 3, column = 0, columnspan = 2, pady = 10)

root.mainloop()