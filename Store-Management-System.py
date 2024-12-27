import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary containing available items with their prices and quantities
available_items = {
    "Google Pixel 6a": {"price": 280, "quantity": 5},
    "SAMSUNG Galaxy S23 Ultra": {"price": 1200, "quantity": 3},
    "iPhone 13 Pro Max": {"price": 1300, "quantity": 2},
    "Xiaomi Redmi 9A": {"price": 100, "quantity": 4},
    "Huawei P50 Pro": {"price": 1000, "quantity": 1},
    "OnePlus 9 Pro": {"price": 800, "quantity": 1},
    "HP Pavilion": {"price": 1200, "quantity": 3},
    "HP EliteBook": {"price": 1399, "quantity": 4},
    "Apple MacBook Air 15 ": {"price": 1610, "quantity": 2},
}

# Welcome message printed in the console
welcoming_message = "Welcome to U0sf Store!!!"
print(welcoming_message)

# Function to add an item to the cart
def push(lst, item):
    new_list = lst + [item]
    return new_list

# Function to remove the last item from the cart
def pop_item(lst):
    if not lst:
        print("Cannot pop from an empty list")
        return lst, None
    pop_product = lst[-1]
    new_lst = lst[:-1]
    return new_lst, pop_product

# Initialize an empty cart
cart = []
deleted_product = None

# Function to add an item to the cart after validating inputs
def add_to_cart():
    item = item_var.get()
    quantity = quantity_var.get()

    if item == "Select an Item" or quantity == "Select Quantity":
        messagebox.showerror("Input Error", "Please select an item and quantity!")
        return

    quantity = int(quantity)
    if available_items[item]["quantity"] < quantity:
        messagebox.showerror(
            "Stock Error", f"Only {available_items[item]['quantity']} left in stock!"
        )
        return

    available_items[item]["quantity"] -= quantity
    product_info = {item: {"price": available_items[item]["price"], "quantity": quantity}}
    cart.append(product_info)
    update_cart()
    messagebox.showinfo("Success", f"{item} added to cart!")

# Function to update the cart display in the GUI
def update_cart():
    cart_list.delete(0, tk.END)
    total_price = 0
    for item in cart:
        for product_name in item:
            price = item[product_name]["price"]
            quantity = item[product_name]["quantity"]
            total = price * quantity
            total_price += total
            cart_list.insert(
                tk.END,
                f"{product_name}: ${price:.2f} x {quantity} = ${total:.2f}",
            )
    total_label.config(text=f"Total: ${total_price:.2f}")

# Function to clear the cart after user confirmation
def clear_cart():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear the cart?"):
        global cart
        cart = []
        update_cart()

# Function to complete the checkout process
def checkout():
    if not cart:
        messagebox.showinfo("Cart Empty", "Your cart is empty!")
    else:
        messagebox.showinfo("Checkout", "Thank you for shopping with us!")
        clear_cart()

# Set up the GUI using tkinter
root = tk.Tk()
root.title("U0sf Store")
root.geometry("1200x750")
root.resizable(False, False)
root.configure(bg="white")  # Set the background color to white

# Add a title label to the GUI
title_label = tk.Label(root, text="Welcome to U0sf Store", font=("Arial", 20, "bold"), bg="white", fg="black")
title_label.pack(pady=10)

# Frame for selecting product and quantity
frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

item_var = tk.StringVar(value="Select an Item")
item_menu = ttk.Combobox(
    frame, textvariable=item_var, values=["Select an Item"] + list(available_items.keys()), state="readonly", width=30
)
item_menu.grid(row=0, column=0, padx=5)

quantity_var = tk.StringVar(value="Select Quantity")
quantity_menu = ttk.Combobox(
    frame, textvariable=quantity_var, values=["Select Quantity"] + [], state="readonly", width=15
)
quantity_menu.grid(row=0, column=1, padx=5)

# Function to update quantity options based on the selected item
def update_quantity_options(event):
    item = item_var.get()
    if item != "Select an Item":
        quantity_options = [str(i) for i in range(1, available_items[item]["quantity"] + 1)]
        quantity_menu.config(values=["Select Quantity"] + quantity_options)
    else:
        quantity_menu.config(values=["Select Quantity"])

item_menu.bind("<<ComboboxSelected>>", update_quantity_options)

# Button to add the product to the cart
add_button = tk.Button(
    frame, text="Add to Cart", command=add_to_cart, bg="#800000", fg="white", font=("Arial", 10, "bold"), relief="solid", bd=2, highlightbackground="black", highlightthickness=2, padx=10, pady=5
)
add_button.grid(row=0, column=2, padx=5)

# Label to display the cart title
cart_label = tk.Label(root, text="Your Cart:", font=("Arial", 14, "bold"), bg="white")
cart_label.pack(pady=10)

cart_list = tk.Listbox(root, width=80, height=10)
cart_list.pack()

# Label to display the total price
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"), bg="white")
total_label.pack(pady=5)

# Frame for cart control buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

clear_button = tk.Button(
    button_frame, text="Clear Cart", command=clear_cart, bg="#800000", fg="white", font=("Arial", 10, "bold"), relief="solid", bd=2, highlightbackground="black", highlightthickness=2, padx=10, pady=5
)
clear_button.grid(row=0, column=0, padx=10)

checkout_button = tk.Button(
    button_frame, text="Checkout", command=checkout, bg="#800000", fg="white", font=("Arial", 10, "bold"), relief="solid", bd=2, highlightbackground="black", highlightthickness=2, padx=10, pady=5
)
checkout_button.grid(row=0, column=1, padx=10)

root.mainloop()
