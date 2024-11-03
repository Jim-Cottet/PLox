from TokenType import TokenType;
from Environment import Environment;

class Interpreter:
    
    def __init__(self):
        self.stmt_list = None;
        self.environment = Environment();
    
    def interpret(self, stmt_list):
        self.stmt_list = stmt_list;
        if stmt_list == None:
            return;
            
        for stmt in self.stmt_list: 
            self.execution(stmt);
    
    # Evaluate the expression of a node
    def evaluate(self, node):
        if node == None:
            return None
        
        method_name = f"visit_{node.type.name.lower()}";
        print(f"Method Name : {method_name}");
        method = getattr(self, method_name, self.generic_visit);
        
        return method(node);
    
    def generic_visit(self, node):
        raise Exception(f"No visit_{node.type.name.lower()} method")
    
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
    
    def visit_expr_variable(self, node):
        return self.environment.get(node.name);
    
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
    

    
    # Execution methods
    def execution(self, stmt):
        if stmt == None:
            return None
        
        print(f"Executing {stmt.type}");
        method_name = f"visit_stmt_{stmt.type.name.lower()}";
        print(f"Method Name : {method_name}");
        method = getattr(self, method_name, self.generic_visit);
        
        return method(stmt);
    
    def visit_stmt_print(self, stmt):
        value = self.evaluate(stmt.expr);
        print(self.stringify(value));
        
    def visit_stmt_var(self, stmt):
        value = None;
        print(f"Var name : {stmt.name}");
        if (stmt.initializer != None):
            value = self.evaluate(stmt.initializer);
        
        self.environment.define(stmt.name, value);
        return None;
    
    def visit_stmt_identifier(self, stmt):
        # For now we can't handle an expression into a variable
        value = stmt.expr.value;
        name = stmt.expr.name;
        print(f"Assigning {stmt.expr.value} with value {value}");
        self.environment.assign(name, value);
        return value;           

    # Helper methods
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