class ExampleClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name} Age: {self.age}"

    def __len__(self):
        return int(self.age/2)

    def __del__(self):
        print(f"Deleting {self.name} object...")

    def __repr__(self):
        return f"ExampleClass(name='{self.name}', age={self.age})"


example = ExampleClass("Adam", 1000)

print(example)
print(len(example))

exampleCopy = repr(example)
print(exampleCopy)
