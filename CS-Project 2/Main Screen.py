from tkinter import *
import csv

def update(data):
  my_list.delete(0, END)
  for item in data:
    my_list.insert(END, item)

def fillout(e):
  my_entry.delete(0, END)
  my_entry.insert(0, my_list.get(ANCHOR))


def check(e):
  typed = my_entry.get()
  if typed == '':
    data = fruits
  else:
    data = [item for item in fruits if typed.lower() in item.lower()]
  update(data)


def select():
  selected_item = my_list.get(ANCHOR)
  display_selected_item(selected_item)


def display_selected_item(item):
  item_name_label.config(text="Item Name: " + item)
  selected_item = None

  for x in selected_items:
    if x["name"] == item:
      selected_item = x
      break

  if selected_item:
    selected_item['quantity'] += 1
    selected_item['price'] = prices[item] * selected_item['quantity']
  else:
    selected_items.append({"name": item, "quantity": 1, "price": prices[item]})
    selected_item = selected_items[-1]

  quantity_entry.delete(0, END)
  quantity_entry.insert(0, selected_item['quantity'])
  update_price(selected_item['quantity'])


def update_price_entry(event, quantity=None):
  try:
    if quantity:
      update_price(quantity)
    else:
      update_price(int(quantity_entry.get()))
  except ValueError:
    price_label.config(text="Price: Invalid Quantity")


def update_price(quantity):
  selected_item = my_list.get(ANCHOR)
  price = prices[selected_item] * quantity
  price_label.config(text="Price: " + str(price))


def save_selected_items():
    update_price_entry(None, int(quantity_entry.get()))

    selected_items_text = my_Label.cget("text")  # Get existing text
    item = selected_items[-1]
    selected_items_text += f"\nItem: {item['name']}, Quantity: {int(quantity_entry.get())}, Price: {int(quantity_entry.get())*prices[item['name']]} RS"
    my_Label.config(text=selected_items_text)

    save_to_csv(selected_items)







def save_to_csv(items):
  with open('selected_items.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Item Name", "Quantity", "Price"])
    for item in items:
      csvwriter.writerow([item['name'], item['quantity'], item['price']])


root = Tk()
root.geometry("800x400")

# Left Section
left_frame = Frame(root)
left_frame.pack(side=LEFT, padx=10, pady=10)

my_label = Label(left_frame,
                 text="Choose your groceries!",
                 font=("Helvetica", 14),
                 fg="grey")
my_label.pack(pady=20)

my_entry = Entry(left_frame, font=("Helvetica", 20))
my_entry.pack()

my_list = Listbox(left_frame, width=50)
my_list.pack(pady=40)

fruits = [
    "Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry",
    "Orange", "Olive"
]

update(fruits)

my_list.bind("<Button-1>", fillout)
my_entry.bind("<KeyRelease>", check)

my_button2 = Button(left_frame,
                    text='Select',
                    command=select,
                    font=("Helvetica", 16))
my_button2.pack()

# Right Section
right_frame = Frame(root)
right_frame.pack(side=RIGHT, padx=10, pady=10)

# Item Name Column
item_name_label = Label(right_frame, text="Item Name: ")
item_name_label.grid(row=0, column=0, pady=10, sticky=W)

# Quantity Column
quantity_label = Label(right_frame, text="Quantity:")
quantity_label.grid(row=1, column=0, pady=10, sticky=W)
quantity_entry = Entry(right_frame, font=("Helvetica", 16))
quantity_entry.grid(row=1, column=1, pady=10, sticky=W)

# Price Column
price_label = Label(right_frame, text="Price: ")
price_label.grid(row=2, column=0, pady=10, sticky=W)






# Save Button
save_button = Button(right_frame,
                     text='Save',
                     command=save_selected_items,
                     font=("Helvetica", 16))
save_button.grid(row=3, column=0, columnspan=2, pady=10)




# Selected Items Column
selected_items_label = Label(right_frame, text="Selected Items:")
selected_items_label.grid(row=4, column=0, columnspan=2, pady=10, sticky=W)
my_Label = Label(right_frame, text=' ')
my_Label.grid(row=5, column=0, columnspan=2, pady=10, sticky=W)

# Default Prices for each item
prices = {
    "Apple": 10,
    "Apricot": 20,
    "Avocado": 50,
    "Banana": 10,
    "Blackberry": 20,
    "Blueberry": 30,
    "Orange": 20,
    "Olive": 50
}

selected_items = []

quantity_entry.bind("<KeyRelease>", update_price_entry)

root.mainloop()
