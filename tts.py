import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('battein karegay')
        #self.root.resizable(0,0)
        self.label1 = tk.Label(self.root, text='kya sunna chahegay aap?')
        self.label1.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text='bolo na!', command=self.clicked)
        self.button.pack()

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()

    def clicked(self):
        text = self.entry.get()
        self.speak(text)

if __name__ == '__main__':
    widget = Widget()
        
