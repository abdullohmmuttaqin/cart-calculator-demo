# File: main_faulty.py
def process_shopping_cart(cart_items, discount_code):
    subtotal = 0

    # 1. Menghitung total harga per item
    for item in cart_items:
        # FAULT 1: Tidak ada validasi harga & kuantitas negatif
        subtotal += item["price"] * item["quantity"]

    # 2. Menerapkan kode diskon
    if discount_code == "DISKON20":
        # FAULT 2: Salah rumus logika diskon (flat deduction -20 rupiah)
        total_pay = subtotal - 20
    else:
        total_pay = subtotal

    # 3. Menghitung rata-rata harga per item
    total_quantity = sum(item["quantity"] for item in cart_items)
    
    # FAULT 3: ZeroDivisionError jika keranjang kosong
    avg_price_per_item = total_pay / total_quantity

    return {
        "subtotal": subtotal,
        "total_pay": total_pay,
        "avg_price": avg_price_per_item
    }