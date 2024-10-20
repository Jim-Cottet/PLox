from TokenType import TokenType;
from ExprNode import Expr;
from TypeDef import TypeDef;

class Parser:
    
    def __init__(self, tokens):
        self.tokens = tokens;
        self.current = 0;
        self.ast = None;
        
    # Entry Function
    def parse(self):
        
        print("Display of the token list in the parser\n");
        for token in self.tokens:
            print("Type : {} Value : {} Line : {}".format(token.type, token.value, token.line));
       
        print("\n-------------------------------------------------------------------------------\n");       
       
         # Start the recursive descent parser     
        self.ast = self.expression();
        
        # Display the AST
        print("Display of the AST in the parser\n");
        self.print_ast(self.ast);
        
       
    #Regressive Descent Parser    
    def expression(self):
        
        return self.equality();
    
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
        
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression();
            self.match(TokenType.RIGHT_PAREN);
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
    
    def previous(self):
        return self.tokens[self.current - 1];
    
    # Printing the AST
    def print_ast(self, node, indent=""):
        if node.type == TypeDef.EXPR_BINARY:
            print(f"{indent}Binary:")
            print(f"{indent}  Operator: {node.value.value}")
            print(f"{indent}  Left:")
            self.print_ast(node.left, indent + "    ")
            print(f"{indent}  Right:")
            self.print_ast(node.right, indent + "    ")
        elif node.type == TypeDef.EXPR_LITERAL:
            print(f"{indent}Literal: {node.value}")
        elif node.type == TypeDef.EXPR_UNARY:
            print(f"{indent}Unary:")
            print(f"{indent}  Operator: {node.value.value}")
            print(f"{indent}  Right:")
            self.print_ast(node.right, indent + "    ")
        else:
            print(f"{indent}Unknown node type: {node.type}")
    
    
        
        
        
        
    