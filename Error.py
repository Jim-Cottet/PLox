class ErrorHandler:
    def __init__(self, message):
        self.message = message;
        self.line_number = 0;
    
    def display_error(self):
        print("Error : {} \nAt line number {}\n".format(self.message, self.line_number));