from TokenType import TokenType;
from ExprNode import Expr;

class Parser:
    
    def __init__(self, tokens):
        self.tokens = tokens;
        self.current = 0;
        self.ast = None;
        
    def parse(self):
        
        print("Display of the token list in the parser");
        for token in self.tokens:
            print(token);
            
       #self.ast = self.expression();
    
    def expression(self):
        return self.equality();
    
    def equality(self):
        expr = self.comparison();
        
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous();
            right = self.comparison();
            expr = Expr().binary(expr, operator, right);
            
        return expr;
        
        
        
        
    