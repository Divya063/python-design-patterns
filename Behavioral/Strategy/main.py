class PaymentStrategy:
    def pay(self, amount):
        pass

class PayPalStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class CardStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Card.")

class Cart:
    def __init__(self, payment_strategy):
        self.items = {}
        self.payment_strategy= payment_strategy

    def add_items(self, item, value):
        self.items[item] = value

    def calculate_total(self):
        return sum(self.items.values())

    def checkout(self):
        amount = self.calculate_total()
        self.payment_strategy.pay(amount)


if __name__ == "__main__":
    paypal = PayPalStrategy()
    card = CardStrategy()

    cart_one = Cart(paypal)
    cart_one.add_items("apple", 10)
    cart_one.checkout()

    cart_two = Cart(card)
    cart_two.add_items("oranges", 20)
    cart_two.checkout()

