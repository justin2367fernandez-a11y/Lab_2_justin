# Precios de la panadería
MENU = {"Pan": 0.50, "Croissant": 1.50, "Pastel": 12.00, "Café": 2.00,"sopa":3.50 "quesitos": 4.50} 
IVA = 0.16  # 16% de impuesto

print("--- PANADERÍA LA ESPIGA ---")
for producto, precio in MENU.items():
    print(f"- {producto}: ${precio:.2f}")

# Simulación de pedido
compra = {"Pan": 6, "Croissant": 2, "Café": 1}

subtotal = sum(MENU[item] * cantidad for item, cantidad in compra.items())
impuesto = subtotal * IVA
total = subtotal + impuesto

# Ticket de venta
print("\n--- TICKET DE VENTA ---")
for item, cantidad in compra.items():
    costo = MENU[item] * cantidad
    print(f"{cantidad}x {item:<10} ${costo:.2f}")

print("-" * 23)
print(f"Subtotal:     ${subtotal:.2f}")
print(f"IVA (16%):    ${impuesto:.2f}")
print(f"TOTAL:        ${total:.2f}")
print("version actualizada")