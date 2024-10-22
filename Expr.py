from TypeDef import TypeDef

class Expr:
    
    def __init__(self) -> None:
        self.type = None;
        self.value = None;
        self.left = None;
        self.right = None;
        self.expression = None;

        
    def literal(self, value) :
        self.type = TypeDef.EXPR_LITERAL;
        self.value = value;
        return self;
        
    def unary(self, value, right) :
        self.type = TypeDef.EXPR_UNARY;
        self.value = value;
        self.right = right;
        return self;
    
    def binary(self, left, value, right) :
        self.type = TypeDef.EXPR_BINARY;
        self.value = value;
        self.left = left;
        self.right = right;
        return self;
        
    def grouping(self, expression) :
        self.type = TypeDef.EXPR_GROUPING;
        self.expression = expression;
        return self;