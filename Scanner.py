from Token import Token
from TokenType import TokenType
from KeywordDic import keywords

class Scanner:
    
    def __init__(self):
        self.line_number = 0;
        self.current = 0;
        self.start = 0;
        self.tokens = [];
        
    def start_scanner(self, file):
        lines = []
        
        try:
            with open(file, 'r') as f:
                lines = f.readlines();
                
        except FileNotFoundError:
            raise Exception(f"File {file} not found");
            
        for line in lines:
            self.line_number += 1;
            self.current = 0;
            chars = self.get_chars_from_line(line);
            self.analyse_the_line(chars);
            
        self.add_token_to_token_list((TokenType.EOF, '', self.line_number));
    
    def add_token_to_token_list(self, token):
        new_token = Token(token[0], token[1], token[2]);
        self.tokens.append(new_token);        
        
    def analyse_the_line(self, line):
        self.current_line = line;
        
        while self.not_at_end():
            self.evaluate_char(self.peek());
            self.current += 1
        
    def not_at_end(self):
        return self.current < len(self.current_line);

    def peek(self):
        if not self.not_at_end():
            return '\0';
        
        return self.current_line[self.current];
    
    def peek_forward(self):
        if self.current + 1 >= len(self.current_line):
            return '\0';
        
        return self.current_line[self.current + 1];
    
    def get_chars_from_line(self, line) -> list:
        chars = list(line);
        
        return chars;
    
    def string_handling(self) -> str :
        while self.not_at_end() and self.peek_forward() != '"':
            self.current += 1;
            
        self.current += 1;
        
        return ''.join(self.current_line[self.start:self.current]);
    
    def identifier_handling(self) -> Token :
        while self.not_at_end() and self.peek_forward().isalpha():
            self.current += 1;
            
        result = ''.join(self.current_line[self.start:self.current + 1]);
        new_token = Token(TokenType.IDENTIFIER, result, self.line_number);
        
        if result in keywords:
            new_token.type = keywords[result];
            return new_token;
        
        return new_token;
    
    def number_handling(self) -> str:
        while self.not_at_end and self.peek().isdigit():
            self.current += 1;
            
        return ''.join(self.current_line[self.start:self.current]);
    
    def match(self, expected):
        if self.not_at_end() and self.peek_forward() != expected:
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
                self.current += 1;
                self.add_token_to_token_list((TokenType.BANG_EQUAL, '!=', self.line_number));
                return
            self.add_token_to_token_list((TokenType.BANG, '!', self.line_number));
            return
        if char == '=':
            if self.match('='):
                self.current += 1;
                self.add_token_to_token_list((TokenType.EQUAL_EQUAL, '==', self.line_number));
                return
            self.add_token_to_token_list((TokenType.EQUAL, '=', self.line_number));
            return
        if char == '<':
            if self.match('='):
                self.current += 1;
                self.add_token_to_token_list((TokenType.LESS_EQUAL, '<=', self.line_number));
                return
            self.add_token_to_token_list((TokenType.LESS, '<', self.line_number));
            return
        if char == '>':
            if self.match('='):
                self.current += 1;                
                self.add_token_to_token_list((TokenType.GREATER_EQUAL, '>=', self.line_number));
                return
            self.add_token_to_token_list((TokenType.GREATER, '>', self.line_number));
            return
        if char == '/':
            if self.match('/'):
                while self.current_line[self.current + 1] != '\n':
                    self.current += 1;
                return
            self.add_token_to_token_list((TokenType.SLASH, '/', self.line_number));
            return
        if char == ' ' or char == '\r' or char == '\t':
            self.start += self.current + 1;
            return
        if char == '\n':
            self.start = 0;
            return
        if char == '"':
            self.start = self.current + 1;
            string_literal = self.string_handling();
            self.add_token_to_token_list((TokenType.STRING, string_literal, self.line_number));
            return
        # "Default" cases
        if char.isdigit():
            self.start = self.current;
            self.number_handling();
            self.add_token_to_token_list((TokenType.NUMBER, self.number_handling(), self.line_number));
            return
        if char.isalpha():
            self.start = self.current;
            identifier = self.identifier_handling();
            self.add_token_to_token_list((identifier.type, identifier.value, identifier.line));
            return
        # Error handling
        raise Exception(f"Unexpected character '{char}' at line {self.line_number}");
        