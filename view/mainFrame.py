import webbrowser
from tkinter import *


class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("GSaver")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (width, height))
        self.window.minsize(720, 480)
        # self.window.iconbitmap("logo.ico")
        self.window.config(background='#dfe1e3')

        # initialization des composants
        self.frame = Frame(self.window, bg='#dfe1e3')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

        self.window.config(menu=self.create_menu_bar)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        # self.create_youtube_button()

    def create_title(self):
        label_title = Label(self.frame, text="Gsaver", font=("Courrier", 40), bg='#dfe1e3',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Help to save all your Guarantees", font=("Courrier", 25), bg='#dfe1e3',
                               fg='white')
        label_subtitle.pack()

    def create_youtube_button(self):
        yt_button = Button(self.frame, text="Ouvrir Youtube", font=("Courrier", 25), bg='white', fg='#dfe1e3',
                           command=self.open_graven_channel)
        yt_button.pack(pady=25, fill=X)

    def open_graven_channel(self):
        webbrowser.open_new("http://youtube.com/gravenilvectuto")




# afficher
app = MyApp()
app.window.mainloop()
