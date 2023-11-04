class Receipe:
    def collect_items(self):
        pass
    def cook(self):
        pass
    def serve(self):
        pass

    def go(self):
        self.collect_items()
        self.cook()
        self.serve()

class MakePizza(Receipe):
    def collect_items(self):
        print("collect items for pizza")
    
    def cook(self):
        print("cook pizza")

    def serve(self):
        print("serve the pizza")


class MakeNoodles(Receipe):
    def collect_items(self):
        print("collect items for Noodles")
    
    def cook(self):
        print("cook noodles")

    def serve(self):
        print("serve noodles")


if __name__ == "__main__":
    noodles = MakeNoodles()
    pizza = MakePizza()

    noodles.go()
    pizza.go()

