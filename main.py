from Scanner import Scanner
from Parser import Parser
from Interpreter import Interpreter

def main():
    
    try:
        # Create an instance of the Parser class
        scanner = Scanner();
        scanner.start_scanner("test.lox");

        # Call a method from the Parser class (assuming a method named 'parse' exists)
        parser = Parser(scanner.tokens);
        stmt_list = parser.parse();
        
        # Call the interpreter method
        interpreter = Interpreter();
        print("\nResult of the expression : ");
        print("stmt_list length : ", len(stmt_list));
        for stmt in stmt_list:
            print("stmt : ", type(stmt));
        interpreter.interpret(stmt_list);
        
    except Exception as e:
        print(e);

if __name__ == "__main__":
    main()