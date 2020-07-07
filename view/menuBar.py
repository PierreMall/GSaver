from tkinter import *


def create_menu_bar():
    menu_bar = Menu(self.window)
    menu_bar.add_command(label="Hello!", command=self.open_graven_channel)
    menu_bar.add_command(label="Quit!", command=self.window.quit)