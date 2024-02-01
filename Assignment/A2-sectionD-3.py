
def singleChange(priceList: list, seq: int, newPrice):
    priceList[seq - 1] = newPrice
    return priceList

def batchChange(newPriceList: str):
    priceList = list(map(float, newPriceList.split(' ')))
    return priceList

def output(itemList, priceList):
    for i in range(len(itemList)):
        print('{0:} {1:}@{2:.2f} hkd/kg'.format(i+1, itemList[i], priceList[i]))

def main():
    item = [
        'Tomato',
        'Potato',
        'Eggplant',
        'Cucumber',
        'Celery',
        'Brococoli'
    ]
    price = [
        12.80,
        8.50,
        4.99,
        1.80,
        3.55,
        2.59
    ]

    print('Current vegetables and prices: ')
    output(item, price)
    if input('Need to do single price change?[y for yes, n for no]: ') == 'y':
        seq = eval(input('Please input veg seq [1-6]: '))
        newPrice = eval(input('Please input veg new price: '))
        price = singleChange(price, seq, newPrice)
        print('Updated list: price change of vegetable {0:} to new price {1:.2f}:'.format(item[seq - 1], price[seq - 1]))
        output(item, price)
    elif input('Need to do multiple price changes?[y for yes, n for no]: ') == 'y':
        price = batchChange(input('Input prices for all vegetables in order[separate with space]: '))
        print('Updated list:')
        output(item, price)
    else:
        print('No price change, exit the program.')

main()