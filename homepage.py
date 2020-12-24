from tkinter import *
from tkinter import messagebox as ms
import os
import check_camera
import Capture_Image
import Train_Image
import Recognize


def function1():
    check_camera.camer()
def function2():
    Capture_Image.takeImages()
def function3():
    Train_Image.TrainImages()
    ms.showinfo("All images trained")
def function4():
    Recognize.recognize_attendence()
    ms.showinfo("Attendance successful")
def function6():
    os.system("py automail.py")
def function7():
    root.destroy()

if __name__ == "__main__":
    root=Tk()
    root.title("FRAS")
    root.configure(background="white")
    Label(root, text="COLLEGE OF ENGINEERING AND TECHNOLOGY", font=("times new roman", 20), fg="black",
          height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)
    Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 20), fg="white", bg="green",
          height=2).grid(row=2, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

    Button(root, text="Check Camera", font=("times new roman", 20), bg="#0D47A1", fg='white', command=function1).grid(
        row=4, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)
    Button(root, text="Train Image", font=("times new roman", 20), bg="#0D47A1", fg='white', command=function2).grid(
        row=5, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)
    Button(root, text="Train Dataset", font=('times new roman', 20), bg="#0D47A1", fg="white",
           command=function3).grid(row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)
    Button(root, text="Recognize + Attendance", font=('times new roman', 20), bg="#0D47A1", fg="white", command=function4).grid(
        row=7, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)
    Button(root, text="Mail Me", font=('times new roman', 20), bg="#0D47A1", fg="white", command=function6).grid(row=9,
        columnspan=2, sticky=N + E + W + S, padx=5, pady=5)
    Button(root, text="Exit", font=('times new roman', 20), bg="maroon", fg="white", command=function7).grid(row=10,
        columnspan=2,sticky=N + E + W + S, padx=5, pady=5)
    root.mainloop()
