import tkinter as tk
from PIL import ImageTk, Image
import csv

# Read the product data from the CSV file
csv_path = "product_data.csv"  # Path to the CSV file
prod_data = []
with open(csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        prod_data.append(row)

# Create a Tkinter window
window = tk.Tk()

# Create a content frame
content_frame = tk.Frame(window)
content_frame.pack()

# Create a function to display the selected product
def show_product(index):
    # Get the data for the selected product
    title = prod_data[index][0]
    link = prod_data[index][1]
    image_path = f"images/product_{index+1}.png"

    # Clear the previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Display the product image
    image = ImageTk.PhotoImage(Image.open(image_path))
    image_label = tk.Label(content_frame, image=image)
    image_label.pack()

    # Display the product title
    title_label = tk.Label(content_frame, text=title)
    title_label.pack()

    # Display the product link
    link_label = tk.Label(content_frame, text=link, fg="blue", cursor="hand2")
    link_label.pack()
    link_label.bind("<Button-1>", lambda event: open_link(link))

# Function to open the product link in a web browser
def open_link(link):
    import webbrowser
    webbrowser.open(link)

# Create buttons for each product
for i, data in enumerate(prod_data):
    button = tk.Button(content_frame, text=f"Product {i+1}", command=lambda idx=i: show_product(idx))
    button.pack()

# Start the Tkinter event loop
window.mainloop()
