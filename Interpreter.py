from TokenType import TokenType;

class Interpreter:
    
    def __init__(self):
        self.ast = None;
    
    def interpret(self, expression):
        self.ast = expression;
        try :
            value = self.evaluate(expression);
            print(self.stringify(value));
        except RuntimeError as e:
            print(e);
    
    def evaluate(self, node):
        
        if node == None:
            return None
        
        node_type_map = {
            1: "expr_unary",
            2: "expr_grouping",
            3: "expr_binary",
            4: "expr_literal",
            # Add other mappings as needed
        }
        
        node_type_str = node_type_map.get(node.type, "unknown")
        method_name = f"visit_{node_type_str}";
        method = getattr(self, method_name, self.generic_visit);
        
        return method(node);
    
    def generic_visit(self, node):
        raise Exception(f"No visit_{node.type.lower()} method")
    
    # Simply return the value of a node    
    def visit_expr_literal(self, node):
        return node.value;
    
    # Evaluate the expression of multiple nodes
    def visit_expr_grouping(self, node):
        return self.evaluate(node.expression);
    
    # Evaluate the expression of a unary node
    def visit_expr_unary(self, node):
        right = self.evaluate(node.right);
        if node.operator.type == TokenType.MINUS:
            return -right;
        if node.operator.type == TokenType.BANG:
            return not self.is_truthy(right);
        return None;
    
    
    def visit_expr_binary(self, node):
        left = self.evaluate(node.left);
        right = self.evaluate(node.right);
        
        if node.operator.type == TokenType.PLUS:
            # Useless in Python, but for the sake of my own edification :)
            if isinstance(left, float) and isinstance(right, float):
                return left + right;
            if isinstance(left, str) and isinstance(right, str):
                return left + right;
            return;
        elif node.operator.type == TokenType.MINUS:
            self.check_number_operands(node.operator, left, right);
            return left - right;
        elif node.operator.type == TokenType.STAR:
            self.check_number_operands(node.operator, left, right);
            return left * right;
        elif node.operator.type == TokenType.SLASH:
            self.check_number_operands(node.operator, left, right);
            return left / right;
        elif node.operator.type == TokenType.GREATER:
            self.check_number_operands(node.operator, left, right);
            return left > right;
        elif node.operator.type == TokenType.GREATER_EQUAL:
            self.check_number_operands(node.operator, left, right);
            return left >= right;
        elif node.operator.type == TokenType.LESS:
            self.check_number_operands(node.operator, left, right);
            return left < right;
        elif node.operator.type == TokenType.LESS_EQUAL:
            self.check_number_operands(node.operator, left, right);
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
    
    def check_number_operands(self, operator, left, right):
        if isinstance(left, float) and isinstance(right, float):
            return;
        raise RuntimeError(f"{left} {right} -> Operands must be numbers.");
    
    def stringify(self, value):
        if value == None:
            return "nil";
        return str(value);