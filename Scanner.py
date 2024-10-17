class Scanner:
    
    def __init__(self):
        self.line_number = 0;
        self.tokens = [];
        
    def start_scanner(self, file):
        lines = self.get_line(file);
        for line in lines:
            self.line_number += 1;
            chars = self.get_chars_from_line(line);
            self.analyse_the_line(chars);            
        
    def evaluate_char(self, char):
        if char == '(':
            print("Left Parenthesis found at line: ", self.line_number);
            return
        if char == ')':
            print("Right Parenthesis found at line: ", self.line_number);
            return
        if char == '{':
            print("Left Brace found at line: ", self.line_number);
            return
        
    def analyse_the_line(self, line):
        for char in line:
            self.evaluate_char(char);
        
    def get_chars_from_line(self, line) -> list:
        chars = list(line);
        return chars;
        
    def get_line(self, file) -> list:
        line = [];
        with open(file, 'r') as f:
            line = f.readlines();
        return line;
