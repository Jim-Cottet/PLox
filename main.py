from Scanner import Scanner

def main():
    # Create an instance of the Parser class
    scanner = Scanner()
    
    # Call a method from the Parser class (assuming a method named 'parse' exists)
    scanner.start_scanner("helloWorld.lox")
    print("Scanner has finished scanning the file")

if __name__ == "__main__":
    main()