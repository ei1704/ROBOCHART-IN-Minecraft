import os,sys,time
import tkinter

def main():
    root = tkinter.Tk()
    
    root.title("Tkinter test")
    root.geometry("640x480")

    box=tkinter.Entry(width=50)
    box.insert(tkinter.END,"")
    box.pack()

    value=box.get()

    print(value)

    root.mainloop()

if __name__ == "__main__":
        main()

