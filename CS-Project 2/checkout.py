from tkinter import *
import csv

checkout_window=Tk()
def display_checkout(selected_items):
  
  checkout_window.title("Checkout")

  checkout_label = Label(checkout_window,
                         text="Checkout",
                         font=("Helvetica", 16))
  checkout_label.grid(row=0, column=0, columnspan=3, pady=10)

  checkout_listbox = Listbox(checkout_window,
                             width=50,
                             height=10,
                             font=("Helvetica", 12))
  checkout_listbox.grid(row=1, column=0, columnspan=3, pady=10)

  total_price = 0

  for item in selected_items:
    item_name = item['name']
    quantity = item['quantity']
    price = item['price']
    total_price += price

    checkout_text = "Item: " + item_name + " | Quantity: " + str(quantity) + " | Price: " + str(price) + " RS"

    checkout_listbox.insert(END, checkout_text)

  total_price_label = Label(checkout_window,
                            text=f"Total Price: {total_price} RS",
                            font=("Helvetica", 12))
  total_price_label.grid(row=2, column=0, columnspan=2, pady=10, sticky=W)

  save_button = Button(checkout_window,
                       text='Save to CSV',
                       command=lambda: save_to_csv(selected_items))
  save_button.grid(row=2, column=2, pady=10, sticky=E)

  


def save_to_csv(items):
  with open('selected_items_checkout.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Item Name", "Quantity", "Price"])
     # csvwriter.writerow is a method in the csv module in Python that is used to write a single row to a CSV file. It takes an iterable (like a list or tuple) as an argument, and it writes each element of the iterable as a separate field in the CSV file, separated by the specified delimiter (usually a comma).
    for item in items:
      csvwriter.writerow([item['name'], item['quantity'], item['price']])


if __name__ == "__main__":
  # This block is executed when the file is run directly
 
  checkout_window.geometry("500x300")

  # Assuming 'selected_items' is defined in the main file
  selected_items = [
      {
          "name": "Apple",
          "quantity": 2,
          "price": 20
      },
      {
          "name": "Banana",
          "quantity": 1,
          "price": 10
      },
      # Add more sample items if needed
  ]

  display_checkout(selected_items)
checkout_window.mainloop()