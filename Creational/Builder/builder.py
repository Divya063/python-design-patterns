class Computer:
    def __init__(self, processor, memory, screen, graphics_card):
        self.processor = processor
        self.memory = memory
        self.screen = screen
        self.graphics_card = graphics_card

    def __str__(self):
        return f"Computer: {self.processor}, {self.memory}, {self.screen}, {self.graphics_card}"
    
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer("", "", "", "")

    # Method chaining: When you return self from each method in the builder class, you can call another method immediately after the previous one, 
    # and so on, on the same builder instance. 
    # This creates a fluent and readable API for building objects.
    def set_processor(self, processor):
        self.computer.processor = processor
        return self
    def set_memory(self, memory):
        self.computer.memory = memory
        return self

    def set_screen(self, screen):
        self.computer.screen = screen
        return self

    def set_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card
        return self

    def build(self):
        return self.computer
    
if __name__ == "__main__":
    computer = ComputerBuilder().set_processor("Intel").set_memory("8GB").set_screen("15 inch").set_graphics_card("Nvidia").build()
    print(computer)
    computer_two = ComputerBuilder().set_processor("AMD").set_memory("16GB").set_graphics_card("AMD").build()
    print(computer_two)