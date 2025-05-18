def fetch_discount_rate():
    pass

def get_discount(price: float) -> float:
    discount_rate = fetch_discount_rate()
    return price - (price * discount_rate)