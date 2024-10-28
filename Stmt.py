class Stmt:
    def __init__(self, type, expr):
        self.line = 0;
        self.type = type;
        self.expr = expr;
        
    def print_stmt(self, type, expr, line):
        self.line = line;
        self.type = type;
        self.expr = expr;
        
    

