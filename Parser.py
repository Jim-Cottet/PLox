from TokenType import TokenType;
from Expr import Expr;
from TypeDef import TypeDef;
from Stmt import Stmt;

class Parser:
    
    def __init__(self, tokens):
        self.tokens = tokens;
        self.current = 0;
        self.stmt_list = [];
        
    # Entry Function
    def parse(self):
        
        print("Display of the token list in the parser\n");
        for token in self.tokens:
            print("Type : {} Value : {} Line : {}".format(token.type, token.value, token.line));
       
        print("\n-------------------------------------------------------------------------------\n");       
        
         # Start the recursive descent parser     
        while not self.is_at_end():
           self.stmt_list.append(self.declaration());
            
        return self.stmt_list;
    # Declaration handling block
    def declaration(self):
        try:
            if self.match(TokenType.VAR):
                new_var = self.var_declaration();
                return new_var;
            
            return self.statement();
        
        except Exception as e:
            #self.synchronize();
            return None;
    
    def var_declaration(self) -> Stmt:
        name = self.consume(TokenType.IDENTIFIER, "Expect variable name.");
        print("Name : {} ".format(name.value));
        
        initializer = None;
        if self.match(TokenType.EQUAL):
            initializer = self.expression();
        print("Initializer : {} ".format(initializer.value));
        
        self.consume(TokenType.SEMICOLON, "Expect ';' after variable declaration.");
        return Stmt(0, TokenType.VAR, None, name.value, initializer);
     
    # Statement handling block   
    def statement(self):
        if self.match(TokenType.PRINT):
            return self.print_statement();

        return self.expression_statement();
    
    def print_statement(self):
        value = self.expression();
        self.consume(TokenType.SEMICOLON, "Expect ';' after value.");
        return Stmt(0, TokenType.PRINT, value, None, None);

    def expression_statement(self):
        value = self.expression();
        self.consume(TokenType.SEMICOLON, "Expect ';' after value.");
        return Stmt(0, TokenType.IDENTIFIER, value, None, None);
    
    # Expression handling block   
    def expression(self):
        return self.assignment();
    
    
    def assignment(self):
        expr = self.equality();
        print("current Token : {} ".format(self.peek().type));
        if (self.match(TokenType.EQUAL)):
            print("current Token : {} ".format(self.peek().type));
            equals = self.previous(2);
            value = self.assignment();
            
            print("Type : {} Value : {} ".format(equals.type, equals.value));
            print("Value : {} ".format(value.value));
            
            if (equals.type == TokenType.IDENTIFIER):
                return Expr().assign(equals.value, value.value);
            
            print("Error : Invalid assignment target.");

        return expr; 
    
    def equality(self):
        expr = self.comparison();
        
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous();
            right = self.comparison();
            expr = Expr().binary(expr, operator, right);
            
        return expr;
    
    def comparison(self):
        expr = self.term();
        
        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous();
            right = self.term();
            expr = Expr().binary(expr, operator, right);
            
        return expr;
    
    def term(self):
        expr = self.factor();
        
        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous();
            right = self.factor();
            expr = Expr().binary(expr, operator, right);
            
        return expr;
    
    def factor(self):
        expr = self.unary();
        
        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous();
            right = self.unary();
            expr = Expr().binary(expr, operator, right);
            
        return expr;
    
    def unary(self):   
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous();
            right = self.unary();
            return Expr().unary(operator, right);
        
        return self.primary();
    
    def primary(self):

        if self.match(TokenType.FALSE):
            return Expr().literal(False);
        
        if self.match(TokenType.TRUE):
            return Expr().literal(True);
        
        if self.match(TokenType.NIL):
            return Expr().literal(None);
        
        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Expr().literal(self.previous().value);
        
        if self.match(TokenType.IDENTIFIER):
            return Expr().variable(self.previous().value);
        
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression();
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.");
            return Expr().grouping(expr);
        
        raise Exception("Invalid Expression {} at line {}".format(self.peek().value, self.peek().line));
    
    # Utility Functions
    def match (self, *types):
        for type in types:
            if self.check(type):
                self.advance();
                return True;
            
        return False;
    
    def check(self, type):
        if self.is_at_end():
            return False;
                                                                                                                                                        
        return self.peek().type == type;
    
    def advance(self):
        if not self.is_at_end():
            self.current += 1;
            
        return self.previous();
    
    def is_at_end(self):
        return self.peek().type == TokenType.EOF;
    
    def peek(self):
        return self.tokens[self.current];
    
    def previous(self, number = 1):
        return self.tokens[self.current - number];
    
    def consume(self, type, message):
        if self.check(type):
            return self.advance();
        
        raise Exception(message);
    
    # The synchronize function
    #! Doesn't work as expected. Need to fix this
    def synchronize(self):
        self.advance();
        
        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return;
            
            if self.peek().type in [
                TokenType.CLASS, 
                TokenType.FUN, 
                TokenType.VAR, 
                TokenType.FOR, 
                TokenType.IF, 
                TokenType.WHILE, 
                TokenType.PRINT, 
                TokenType.RETURN
                ]: return;
            
            self.advance();
    
        
        
        
    