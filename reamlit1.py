import streamlit as st

# Initialize session state variables
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'products' not in st.session_state:
    st.session_state['products'] = []

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock Quantity: {self.stock_quantity}"

class Inventory:
    def __init__(self):
        # Initialize products in session state if not already
        if 'products' not in st.session_state:
            st.session_state['products'] = []

    def add_product(self, product_id, name, category, price, stock_quantity):
        product = Product(product_id, name, category, price, stock_quantity)
        st.session_state['products'].append(product)
        st.success("Product added successfully!")

    def edit_product(self, product_id, new_name, new_category, new_price, new_stock_quantity):
        for product in st.session_state['products']:
            if product.product_id == product_id:
                product.name = new_name
                product.category = new_category
                product.price = new_price
                product.stock_quantity = new_stock_quantity
                st.success("Product updated successfully!")
                return
        st.error("Product not found.")

    def delete_product(self, product_id):
        for i, product in enumerate(st.session_state['products']):
            if product.product_id == product_id:
                del st.session_state['products'][i]
                st.success("Product deleted successfully!")
                return
        st.error("Product not found.")

    def display_products(self):
        if not st.session_state['products']:
            st.write("No products in inventory.")
        else:
            st.write("### Current Inventory")
            for product in st.session_state['products']:
                st.write(product)

class WebLogin:
    def __init__(self):
        if 'users' not in st.session_state:
            st.session_state['users'] = {"admin": "admin123"}

    def add_user(self, username, password):
        st.session_state['users'][username] = password
        st.success(f"User '{username}' added successfully!")

    def login(self, username, password):
        if username in st.session_state['users'] and st.session_state['users'][username] == password:
            return True
        return False

# Initialize inventory and user login
inventory = Inventory()
web_login = WebLogin()

# Streamlit interface
st.title("Inventory Management System")

# Login interface
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["current_user"] = None

# Check if user is authenticated
if not st.session_state["authenticated"]:
    st.write("### Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if web_login.login(username, password):
            st.session_state["authenticated"] = True
            st.session_state["current_user"] = username
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")
else:
    st.write(f"Welcome, {st.session_state['current_user']}!")
    menu_options = ["Add Product", "Edit Product", "Delete Product", "Display Products", "Add User", "Logout"]
    choice = st.selectbox("Choose an option:", menu_options)

    if choice == "Add Product":
        product_id = st.text_input("Enter Product ID:")
        name = st.text_input("Enter Product Name:")
        category = st.text_input("Enter Product Category:")
        price = st.number_input("Enter Product Price:", min_value=0.0, step=0.01)
        stock_quantity = st.number_input("Enter Stock Quantity:", min_value=0, step=1)

        if st.button("Add Product"):
            st.write("Add Product button clicked")  # Debug message
            inventory.add_product(product_id, name, category, price, stock_quantity)

    elif choice == "Edit Product":
        product_id = st.text_input("Enter Product ID to Edit:")
        new_name = st.text_input("Enter New Name:")
        new_category = st.text_input("Enter New Category:")
        new_price = st.number_input("Enter New Price:", min_value=0.0, step=0.01)
        new_stock_quantity = st.number_input("Enter New Stock Quantity:", min_value=0, step=1)

        if st.button("Edit Product"):
            inventory.edit_product(product_id, new_name, new_category, new_price, new_stock_quantity)

    elif choice == "Delete Product":
        product_id = st.text_input("Enter Product ID to Delete:")

        if st.button("Delete Product"):
            inventory.delete_product(product_id)

    elif choice == "Display Products":
        inventory.display_products()

    elif choice == "Add User":
        if st.session_state["current_user"] == "admin":
            new_username = st.text_input("Enter new username:")
            new_password = st.text_input("Enter new password:", type="password")
            if st.button("Add User"):
                web_login.add_user(new_username, new_password)
        else:
            st.error("Only admin can add new users.")

    elif choice == "Logout":
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = None
