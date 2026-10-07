# File: main_fixed.py
def process_shopping_cart_fixed(cart_items, discount_code):
    # Handling Fault 3: Guard clause jika keranjang kosong
    if not cart_items:
        return {"subtotal": 0, "total_pay": 0, "avg_price": 0}

    subtotal = 0

    # Handling Fault 1: Validasi data input (boundary check)
    for item in cart_items:
        if item.get("price", 0) <= 0 or item.get("quantity", 0) <= 0:
            raise ValueError(f"Invalid item data: {item['name']}. Price and quantity must be > 0.")
        subtotal += item["price"] * item["quantity"]

    # Handling Fault 2: Perbaikan rumus diskon 20%
    if discount_code == "DISKON20":
        total_pay = subtotal * 0.80  # Potongan 20%
    else:
        total_pay = subtotal

    total_quantity = sum(item["quantity"] for item in cart_items)
    
    # Handling Fault 3 tambahan (Double safety check)
    avg_price_per_item = total_pay / total_quantity if total_quantity > 0 else 0

    return {
        "subtotal": round(subtotal, 2),
        "total_pay": round(total_pay, 2),
        "avg_price": round(avg_price_per_item, 2)
    }