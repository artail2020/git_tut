def total_price_1item(unit_price: int, quantity: int = 1) -> str:
    total_price: int = unit_price * quantity
    return f'\\{total_price:,}'

total: str = total_price_1item(unit_price=1300)
print(total)
