from Scanner import Scanner
from Parser import Parser

def main():
    # Create an instance of the Parser class
    scanner = Scanner();
    scanner.start_scanner("helloWorld.lox");
    
    # Call a method from the Parser class (assuming a method named 'parse' exists)
    parser = Parser(scanner.tokens);
    parser.parse();
    
if __name__ == "__main__":
    main()