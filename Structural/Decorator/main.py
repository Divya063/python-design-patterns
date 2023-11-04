
# Concrete Component
class SimpleCoffee():
    def cost(self):
        return 5
    
class BlackCoffee():
    def cost(self):
        return 10

# Decorator
class CoffeeDecorator(SimpleCoffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

class VanillaDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3
    
if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"Cost of simple coffee: {coffee.cost()}")

    cost_of_decorated_coffee = MilkDecorator(SugarDecorator(VanillaDecorator(coffee)))
    print(f"Cost of decorated coffee: {cost_of_decorated_coffee.cost()}")

    blackCoffee = BlackCoffee()
    print(f"Cost of black coffee: {blackCoffee.cost()}")

    cost_of_decorated_black_coffee = MilkDecorator(SugarDecorator(VanillaDecorator(blackCoffee)))
    print(f"Cost of decorated black coffee: {cost_of_decorated_black_coffee.cost()}")