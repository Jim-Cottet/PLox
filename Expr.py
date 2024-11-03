from TypeDef import TypeDef
class Expr:
    
    def __init__(self) -> None:
        self.type = None;
        self.value = None;
        self.left = None;
        self.right = None;
        self.operator = None;
        self.expression = None;
        
    def literal(self, value) :
        self.type = TypeDef.EXPR_LITERAL;
        self.value = value;
        return self;
       
    def unary(self, operator, right) :
        self.type = TypeDef.EXPR_UNARY;
        self.operator = operator;
        self.right = right;
        return self;
    
    def binary(self, left, operator, right) :
        self.type = TypeDef.EXPR_BINARY;
        self.left = left;
        self.operator = operator;
        self.right = right;
        return self;
        
    def grouping(self, expression) :
        self.type = TypeDef.EXPR_GROUPING;
        self.expression = expression;
        return self;
    
    def variable(self, name) :
        self.type = TypeDef.EXPR_VARIABLE;
        self.name = name;
        return self;
    
    def assign(self, name, value) :
        self.type = TypeDef.EXPR_ASSIGN;
        self.name = name;
        self.value = value;
        return self;
   