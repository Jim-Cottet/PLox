from TokenType import TokenType;

class Stmt:
    def __init__(self, line, type_name, expr, name, initializer):
        self.line = line;
        self.type = type_name;
        self.expr = expr;
        self.name = name;
        self.initializer = initializer;
    
        
     

