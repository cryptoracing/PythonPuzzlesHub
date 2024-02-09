FIRST_ITEM = 100
NEXT_ITEM = 30

def delivery_calculator(qty):
    if quantity > 0:
        result = FIRST_ITEM + (qty-1) * NEXT_ITEM
    else:
        return -1
    return result

quantity=int(input("How many parcels would you order?\n"))
print(delivery_calculator(quantity))