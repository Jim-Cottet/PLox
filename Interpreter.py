from TokenType import TokenType;

class Interpreter:
    
    def __init__(self, ast):
        self.ast = ast;
        
    def evaluate(self):
        return self.evaluate(self.ast)
    
    # Simply return the value of a node    
    def literal_expression(self, node):
        return node.value;
    
    # Evaluate the expression of multiple nodes
    def grouped_expression(self, node):
        return self.evaluate(node.expression);
    
    # Evaluate the expression of a unary node
    def unary_expression(self, node):
        right = self.evaluate(node.right);
        if node.operator.type == TokenType.MINUS:
            return -right;
        if node.operator.type == TokenType.BANG:
            #! What if the expression cannot produce any boolean value?
            return not self.is_truthy(right);
        return None;
    
    
    def binary_expression(self, node):
        left = self.evaluate(node.left);
        right = self.evaluate(node.right);
        
        self.check_number_operand(node.operator, left);
        self.check_number_operand(node.operator, right);
        
        if node.operator.type == TokenType.PLUS:
            # Useless in Python, but for the sake of my own edification :)
            if isinstance(left, float) and isinstance(right, float):
                return left + right;
            if isinstance(left, str) and isinstance(right, str):
                return left + right;
            return;
        elif node.operator.type == TokenType.MINUS:
            return left - right;
        elif node.operator.type == TokenType.STAR:
            return left * right;
        elif node.operator.type == TokenType.SLASH:
            return left / right;
        elif node.operator.type == TokenType.GREATER:
            return left > right;
        elif node.operator.type == TokenType.GREATER_EQUAL:
            return left >= right;
        elif node.operator.type == TokenType.LESS:
            return left < right;
        elif node.operator.type == TokenType.LESS_EQUAL:
            return left <= right;
        elif node.operator.type == TokenType.BANG_EQUAL:
            return left != right;
        elif node.operator.type == TokenType.EQUAL_EQUAL:
            return left == right;
        return None;
    
    def is_truthy(self, value):
        if value == None:
            return False;
        if value == False:
            return False;
        return True;
    
    def is_equal(self, a, b):
        if a == None and b == None:
            return True;
        if a == None:
            return False;
        return a == b;
    
    def check_number_operand(self, operator, operand):
        if isinstance(operand, float):
            return;
        raise RuntimeError(f"{operand} -> Operand must be a number.");
    