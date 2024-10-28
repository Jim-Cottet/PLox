class Stmt:
    def __init__(self, type, expr):
        self.line = 0;
        self.type = type;
        self.expr = expr;
        self.name = "";
        self.value = None;
        
    def print_stmt(self, type, expr, line):
        self.line = line;
        self.type = type;
        self.expr = expr;
        
    def var_stmt(self, type, value, name):
        self.type = type;
        self.value = value;
        self.name = name;
        
    
        
     

