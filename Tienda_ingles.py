# Inventory of products
inventory = []

# Input validation functions
def input_integer(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")

def input_float(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a decimal number.")

def input_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        else:
            print("❌ Text cannot be empty.")

# Function to show all products
def show_products():
    if not inventory:
        print("📦 The inventory is empty.")
    else:
        print("\n📋 Inventory List:")
        for product in inventory:
            print(f"🔹 ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Quantity: {product['quantity']}")

# Function to add a new product
def add_product():
    while True:
        new_id = input_integer("🔢 Product ID: ")
        if any(p['id'] == new_id for p in inventory):
            print("❌ That ID already exists. Please enter a different one.")
        else:
            break
    name = input_text("📝 Product name: ")
    price = input_float("💵 Product price: ")
    quantity = input_integer("📦 Product quantity: ")

    inventory.append({
        'id': new_id,
        'name': name,
        'price': price,
        'quantity': quantity
    })
    print("✅ Product added successfully.")

# Function to delete a product by ID
def delete_product():
    if not inventory:
        print("❌ No products to delete.")
        return
    delete_id = input_integer("🗑️ Enter the ID of the product to delete: ")
    for i, product in enumerate(inventory):
        if product['id'] == delete_id:
            inventory.pop(i)
            print("✅ Product deleted.")
            return
    print("❌ No product found with that ID.")

# Function to search for a product by name
def search_product():
    search_name = input_text("🔍 Enter the product name to search for: ").lower()
    found = [p for p in inventory if search_name in p['name'].lower()]
    if found:
        print("📦 Matching products:")
        for p in found:
            print(f"🔹 ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Quantity: {p['quantity']}")
    else:
        print("❌ No products found with that name.")

# Function to update a product's quantity and price
def update_product():
    update_id = input_integer("✏️ Enter the product ID to update: ")
    for product in inventory:
        if product['id'] == update_id:
            new_price = input_float("💲 New price: ")
            new_quantity = input_integer("📦 New quantity: ")
            product.update({"price": new_price, "quantity": new_quantity})
            print("✅ Product updated.")
            return
    print("❌ Product not found.")

# Show products with low stock
def low_stock_products():
    threshold = input_integer("⚠️ Show products with quantity lower than: ")
    low_stock = [p for p in inventory if p['quantity'] < threshold]
    if low_stock:
        print("📉 Products with low stock:")
        for p in low_stock:
            print(f"🔹 ID: {p['id']} | Name: {p['name']} | Quantity: {p['quantity']}")
    else:
        print("✅ All products have sufficient stock.")

# Main menu function
def menu():
    while True:
        print("\n🔧 MAIN MENU")
        print("1️⃣ Show all products")
        print("2️⃣ Add a new product")
        print("3️⃣ Delete a product")
        print("4️⃣ Search product by name")
        print("5️⃣ Update product")
        print("6️⃣ Show low stock products")
        print("7️⃣ Exit")

        choice = input("📍 Choose an option (1-7): ").strip()

        if choice == "1":
            show_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            search_product()
        elif choice == "5":
            update_product()
        elif choice == "6":
            low_stock_products()
        elif choice == "7":
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Choose a number between 1 and 7.")

# Run the program
menu()
