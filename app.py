import tkinter

from controllers.cli_controller import CLIController
from controllers.gui_controller import GUIController
from model import Model
from views.cli_view import CLIView
from views.gui_view import GUIView

UseUI = False
model = Model('YegorMotruck')


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title('MVC')

        # create a view and place it on the root window
        view = GUIView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = GUIController(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    if UseUI:
        app = App()
        app.mainloop()
    else:
        view = CLIView()
        controller = CLIController(model, view)

        view.set_controller(controller)
        view.run()
