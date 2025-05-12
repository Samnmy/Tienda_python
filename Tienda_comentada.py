# Initialize an empty list to store products
inventory = []

# Function to safely read an integer from the user
def input_integer(message):
    while True:
        try:
            value = int(input(message))  # Try converting user input to integer
            return value
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")  # Error if input is not an integer

# Function to safely read a float from the user
def input_float(message):
    while True:
        try:
            value = float(input(message))  # Try converting user input to float
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a decimal number.")  # Error if input is not a float

# Function to safely read non-empty text from the user
def input_text(message):
    while True:
        value = input(message).strip()  # Remove leading/trailing whitespace
        if value:  # If input is not empty
            return value
        else:
            print("❌ Text cannot be empty.")  # Error if empty

# Function to display all products in the inventory
def show_products():
    if not inventory:  # If inventory list is empty
        print("📦 The inventory is empty.")
    else:
        print("\n📋 Inventory List:")
        for product in inventory:  # Iterate over each product in inventory
            print(f"🔹 ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Quantity: {product['quantity']}")

# Function to add a new product to the inventory
def add_product():
    while True:
        new_id = input_integer("🔢 Product ID: ")  # Get product ID from user
        # Check if the ID already exists
        if any(p['id'] == new_id for p in inventory):
            print("❌ That ID already exists. Please enter a different one.")
        else:
            break  # ID is unique; exit loop
    name = input_text("📝 Product name: ")  # Get product name
    price = input_float("💵 Product price: ")  # Get product price
    quantity = input_integer("📦 Product quantity: ")  # Get product quantity

    # Add new product as a dictionary to the inventory list
    inventory.append({
        'id': new_id,
        'name': name,
        'price': price,
        'quantity': quantity
    })
    print("✅ Product added successfully.")

# Function to delete a product by ID
def delete_product():
    if not inventory:  # If inventory is empty
        print("❌ No products to delete.")
        return
    delete_id = input_integer("🗑️ Enter the ID of the product to delete: ")  # Ask for ID to delete
    for i, product in enumerate(inventory):  # Iterate with index
        if product['id'] == delete_id:  # If ID matches
            inventory.pop(i)  # Remove product by index
            print("✅ Product deleted.")
            return
    print("❌ No product found with that ID.")  # If no match is found

# Function to search for products by name (partial match)
def search_product():
    search_name = input_text("🔍 Enter the product name to search for: ").lower()  # Get search term
    # Filter products where name contains search term (case-insensitive)
    found = [p for p in inventory if search_name in p['name'].lower()]
    if found:
        print("📦 Matching products:")
        for p in found:
            print(f"🔹 ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Quantity: {p['quantity']}")
    else:
        print("❌ No products found with that name.")

# Function to update price and quantity of a product
def update_product():
    update_id = input_integer("✏️ Enter the product ID to update: ")  # Ask for ID to update
    for product in inventory:
        if product['id'] == update_id:  # If found
            new_price = input_float("💲 New price: ")  # Ask for new price
            new_quantity = input_integer("📦 New quantity: ")  # Ask for new quantity
            # Update the dictionary using .update()
            product.update({"price": new_price, "quantity": new_quantity})
            print("✅ Product updated.")
            return
    print("❌ Product not found.")  # If ID not found

# Function to display products below a certain stock threshold
def low_stock_products():
    threshold = input_integer("⚠️ Show products with quantity lower than: ")  # Ask user for threshold
    # Filter products with quantity below threshold
    low_stock = [p for p in inventory if p['quantity'] < threshold]
    if low_stock:
        print("📉 Products with low stock:")
        for p in low_stock:
            print(f"🔹 ID: {p['id']} | Name: {p['name']} | Quantity: {p['quantity']}")
    else:
        print("✅ All products have sufficient stock.")

# Main menu that keeps running until user exits
def menu():
    while True:
        # Display menu options
        print("\n🔧 MAIN MENU")
        print("1️⃣ Show all products")
        print("2️⃣ Add a new product")
        print("3️⃣ Delete a product")
        print("4️⃣ Search product by name")
        print("5️⃣ Update product")
        print("6️⃣ Show low stock products")
        print("7️⃣ Exit")

        # Get user option
        choice = input("📍 Choose an option (1-7): ").strip()

        # Execute the corresponding function
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
            break  # Exit the loop
        else:
            print("❌ Invalid option. Choose a number between 1 and 7.")  # Error if input is invalid

# Call the main menu to start the program
menu()
