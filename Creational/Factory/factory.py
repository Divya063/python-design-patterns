def chooseDeviceFactory(input, device): 
    devices = {
        "alexa": Alexa,
        "kindle": Kindle,
        "echo": Echo
    }

    return devices[device](input)


class Alexa():
    def __init__(self, input):
        self.name = "Alexa"
        self.price = 100
        self.custom_input = input

    def play(self):
         print(self.custom_input)


class Kindle():
    def __init__(self, input):
        self.name = "Kindle"
        self.price = 200
        self.custom_input = input
       

    def play(self):
         print(self.custom_input)


class Echo():
    def __init__(self, input):
        self.name = "Echo"
        self.price = 300
        self.custom_input = input
    
    def play(self):
         print(self.custom_input)

if __name__ == "__main__":
    device = chooseDeviceFactory("play music", "alexa")
    device.play()
    device = chooseDeviceFactory("read book", "kindle")
    device.play()


