from tkinter import *
from tkinter import ttk
class tkinter:Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Window")
        self.root.geometry("400x300")

        self.label = ttk.Label(self.root, text="Hello, World!")
        self.label.pack(pady=20)

        self.button = ttk.Button(self.root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()