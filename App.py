from Tkinter import *
import webbrowser

class App():

    w = 400
    h = 100
    bgColor = '#77216F'

    def __init__(self, labeltext):

        self.url = labeltext[labeltext.find('\n') + 1:]

        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.configure(background=self.bgColor)    # setting background color

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        # set the dimensions of the screen and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws - self.w - 25, 40))

        self.label = Label(self.root, text=labeltext, fg='#ffffff', bg=self.bgColor, wraplength=350)
        self.label.pack(pady=20)    # put label on root
        self.label.bind("<Button-1>", self.bopen)   # bind bopen function on label

        self.bQuit = Button(self.root, text="X", command=self.closeSelf)
        self.bQuit.configure(background = '#77216F')    # configure background of the button
        self.bQuit.place(x=375, y=0, height=25, width=25)   # place the quit button

        
        self.root.after(7500, lambda: self.root.destroy())  # close popup after 7500 second itself
        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', True)   # so that window is always topmost
        self.root.mainloop()

    def closeSelf(self):        # closes the popup
        self.root.destroy()

    def bopen(self, event):     # open the url in default webbrowser
        webbrowser.open(self.url)
        self.closeSelf()

# app = App('hello').root.mainloop()