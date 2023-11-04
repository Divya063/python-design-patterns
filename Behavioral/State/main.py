class SystemState:
    allowed = []
    state = "state"

    def switch(self, state):
        if state.state in self.allowed:
            print("Switched state to", state.state)
            self.__class__ = state
        else:
            print(f"Cannot switch to {state}")
            
    # define a custom string representation of an object.
    def __str__(self):
        return self.state



class On(SystemState):
    allowed = ["off", "hibernate"]
    state = "on"

class Off(SystemState):
    allowed = ["on"]
    state = "off"

class hibernate(SystemState):
    allowed = ["on"]
    state = "hibernate"

class System():
    def __init__(self):
        self.state = Off()
    def change(self, state):
        self.state.switch(state)

if __name__ == "__main__":
    comp = System()
    comp.change(On)
    comp.change(hibernate)



    
        
