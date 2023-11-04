class Subscriber:
    def __init__(self, name):
        self.subscriber = name

    def update(self):
        print("got an update")

# define subject
# attach/detach/notify
class NewAgency:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def deattach(self, subscriber):
        for subs in self.subscribers:
            if subs == subscriber:
                self.subscribers.remove(subscriber)
    def notify(self):
        for subs in self.subscribers:
            subs.update()

if __name__ == "__main__":
    sub1 = Subscriber("sub1")
    sub2 = Subscriber("sub2")
    newAgency = NewAgency()
    newAgency.subscribe(sub1)
    newAgency.subscribe(sub2)
    newAgency.notify()



