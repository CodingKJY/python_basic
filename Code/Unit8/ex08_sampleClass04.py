class Shop:
    def __init__(self, product = 'No Product', quantum = 0):
        self.product = product
        self.quantum = quantum
    
    def __str__(self):
        return f'Product: {self.product}\nQuantum: {self.quantum}\n'

shop = Shop('Chocolate', 205)
print(shop)