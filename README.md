Inventory Management System with User Login
This Streamlit app implements a basic inventory management system with user login functionality.

Features:

Product Management:
Add new products to the inventory.
Edit existing products (name, category, price, stock quantity).
Delete products from the inventory.
View all products in the inventory.
User Management (Admin Only):
Add new users with username and password. (Only accessible to the "admin" user)
User Login:
Users need to login with a valid username and password to access the inventory management features.
Running the App:

Install required libraries:
pip install streamlit

Run the app using Python:
streamlit run inventory_app.py (reamlit1.py)

Tech Stack:

Streamlit - Web framework for building data apps in Python.
Code Structure:

The code is organized into several classes:

Product: Represents a product with attributes like product ID, name, category, price, and stock quantity.
Inventory: Manages the product inventory by adding, editing, deleting, and displaying products.
WebLogin: Handles user login and authentication.
Session State:
The app utilizes Streamlit session state to store user authentication status, current user information, and the product inventory across app sessions.

Future Improvements:

Implement data persistence to store inventory and user data in a database instead of session state.
Enhance the UI with functionalities like searching and filtering products.
Add user roles and permissions for more control over user actions.
