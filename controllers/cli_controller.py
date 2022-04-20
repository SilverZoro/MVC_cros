class CLIController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, name):
        """
        Save the name
        :param name:
        :return:
        """
        try:

            # save the model
            self.model.name = name
            self.model.save()

            # show a success message
            self.view.print_success(f'The name {name} saved!')

        except ValueError as error:
            # show an error message
            self.view.print_error(error)
