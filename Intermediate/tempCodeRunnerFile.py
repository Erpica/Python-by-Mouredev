def greet_fabric ():
    def greet(name):
        return f"hola, {name}"
    return greet

my_greet = greet_fabric()
my_greet("Anto")