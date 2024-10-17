from Token import Token
from TokenType import TokenType

class Scanner:
    
    def __init__(self):
        self.line_number = 0;
        self.current = 0;
        self.tokens = [];
        
    def start_scanner(self, file):
        lines = []
        with open(file, 'r') as f:
            lines = f.readlines();
        for line in lines:
            self.line_number += 1;
            self.current = 0;
            chars = self.get_chars_from_line(line);
            self.analyse_the_line(chars);
    
    def add_token_to_token_list(self, token):
        self.tokens.append(token);        
        
    def analyse_the_line(self, line):
        self.current_line = line;
        for char in self.current_line:
            self.current += 1;
            self.evaluate_char(char);
        
    def get_chars_from_line(self, line) -> list:
        chars = list(line);
        return chars;
    
    # We need a method to check if we are in the end of a line or not
    
    def match(self, expected):
        if self.current_line[self.current + 1] != expected:
            return False;
        return True;

    def evaluate_char(self, char) -> Token :
        # Single character tokens
        if char == '(':
            self.add_token_to_token_list((TokenType.LEFT_PAREN, '(', self.line_number));
            return
        if char == ')':
            self.add_token_to_token_list((TokenType.RIGHT_PAREN, ')', self.line_number));
            return
        if char == '{':
            self.add_token_to_token_list((TokenType.LEFT_BRACE, '{', self.line_number));
            return
        if char == '}':
            self.add_token_to_token_list((TokenType.RIGHT_BRACE, '}', self.line_number));
            return
        if char == ',':
            self.add_token_to_token_list((TokenType.COMMA, ',', self.line_number));
            return
        if char == '.':
            self.add_token_to_token_list((TokenType.DOT, '.', self.line_number));
            return
        if char == '-':
            self.add_token_to_token_list((TokenType.MINUS, '-', self.line_number));
            return
        if char == '+':
            self.add_token_to_token_list((TokenType.PLUS, '+', self.line_number));
            return
        if char == ';':
            self.add_token_to_token_list((TokenType.SEMICOLON, ';', self.line_number));
            return
        if char == '*':
            self.add_token_to_token_list((TokenType.STAR, '*', self.line_number));
            return
        # Two character tokens
        if char == '!':
            if self.match('='):
                self.add_token_to_token_list((TokenType.BANG_EQUAL, '!=', self.line_number));
                return
            self.add_token_to_token_list((TokenType.BANG, '!', self.line_number));
            return
        if char == '=':
            if self.match('='):
                self.add_token_to_token_list((TokenType.EQUAL_EQUAL, '==', self.line_number));
                return
            self.add_token_to_token_list((TokenType.EQUAL, '=', self.line_number));
            return
        if char == '<':
            if self.match('='):
                self.add_token_to_token_list((TokenType.LESS_EQUAL, '<=', self.line_number));
                return
            self.add_token_to_token_list((TokenType.LESS, '<', self.line_number));
            return
        if char == '>':
            if self.match('='):
                self.add_token_to_token_list((TokenType.GREATER_EQUAL, '>=', self.line_number));
                return
            self.add_token_to_token_list((TokenType.GREATER, '>', self.line_number));
            return
        