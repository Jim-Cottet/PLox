from Scanner import Scanner
from Parser import Parser

def main():
    
    try:
        # Create an instance of the Parser class
        scanner = Scanner();
        scanner.start_scanner("helloWorld.lox");

        # Call a method from the Parser class (assuming a method named 'parse' exists)
        parser = Parser(scanner.tokens);
        parser.parse();
        
    except Exception as e:
        print(e);

    
if __name__ == "__main__":
    main()