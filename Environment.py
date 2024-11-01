class Environment:
    
    def __init__(self):
            self.values = dict();
        
    def define(self, name, value):
        print(f"Defining variable {name} with value {value}");
        self.values[name] = value
    
    def get(self, name) -> object:
        if name in self.values:
            return self.values[name];
        raise Exception(f"Undefined variable '{name}'.");
  