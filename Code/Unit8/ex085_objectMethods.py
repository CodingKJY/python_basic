class Shop:
    def __init__(self, product = 'No Product', quantum = 0, price = 0):
        self.product = product
        self.quantum = quantum
        self.price   = price
        self.asset   = 0
        self.sold    = 0
    
    def __str__(self):
        product = f'Product: {self.product}\n'
        quantum = f'Quantum: {self.quantum}\n'
        price   = f'Price  : {self.price} NTD\n'
        sold    = f'Sold   : {self.sold}\n'
        asset   = f'Shop assets: {self.asset} NTD\n'
        return product + quantum + price + sold + asset
    
    def sell(self, amount):
        # if no product to sell
        if self.quantum == 0: 
            print('Nothing to sell!')
            return
        
        price = self.price
        sold  = amount
        # if demand higher than supply
        if self.quantum - amount < 0: sold = self.quantum
        
        # update attributes
        self.asset += sold * price
        self.sold  += sold 
        self.quantum -= sold 

coffeeShop = Shop('Coffee', 250, 35)
print(coffeeShop)
coffeeShop.sell(123)
print(coffeeShop)
coffeeShop.sell(130)
print(coffeeShop)
coffeeShop.sell(20)
print(coffeeShop)