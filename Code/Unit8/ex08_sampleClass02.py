class Shop:
    def __init__(self, product, quantum):
        self.product = product
        self.quantum = quantum

shop = Shop('Tea', 180)
print('Product: ', shop.product)
print('Quantum: ', shop.quantum)