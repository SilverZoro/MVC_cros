from tkinter import ttk
import tkinter as tk


class GUIView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Name:')
        self.label.grid(row=1, column=0)

        # name entry
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(self, textvariable=self.name_var, width=30)
        self.name_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def save_button_clicked(self):
        if self.controller:
            self.controller.save(self.name_var.get())

    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.name_entry['foreground'] = 'red'

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.name_entry['foreground'] = 'black'
        self.name_var.set('')

    def hide_message(self):
        self.message_label['text'] = ''
