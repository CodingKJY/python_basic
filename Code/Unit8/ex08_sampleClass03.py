class Shop:
    def __init__(self, product = 'No Product', quantum = 0):
        self.product = product
        self.quantum = quantum

shop1 = Shop()
shop2 = Shop('Flower', 1850)
print('Shop1')
print('Product: ', shop1.product)
print('Quantum: ', shop1.quantum)

print('Shop2')
print('Product: ', shop2.product)
print('Quantum: ', shop2.quantum)