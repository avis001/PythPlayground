def purchase_item(price, gold_available):
    if gold_available >= price:
        return gold_available - price
    else:
        raise Exception("not enough gold")
