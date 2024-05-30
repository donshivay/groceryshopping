import csv
from tkinter import *
from PIL import Image, ImageTk
import sys

def display_checkout(selected_items):
  def thank_click():
    proceed_to_pay(selected_items, checkout_window)
  checkout_window = Tk()
  checkout_window.title("Checkout")
  checkout_window.configure(background='#ADD8E6')

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

    checkout_text = "Item: " + item_name + " | Quantity: " + str(
        quantity) + " | Price: " + str(price) + " RS"

    checkout_listbox.insert(END, checkout_text)

  total_price_label = Label(checkout_window,
                            text=f"Total Price: {total_price} RS",
                            font=("Helvetica", 12))
  total_price_label.grid(row=2, column=0, columnspan=2, pady=10, sticky=W)
  def proceed_to_pay(items, checkout_window):
    with open('selected_items_checkout.csv', 'w', newline='') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow(["Item Name", "Quantity", "Price"])
      for item in items:
        csvwriter.writerow([item['name'], item['quantity'], item['price']])
    checkout_window.destroy()
    showimage()

  save_button = Button(checkout_window, text='Proceed to Pay',command=thank_click)


  save_button.grid(row=2, column=2, pady=10, sticky=E)


  checkout_window.mainloop()




def showimage():
    def endit():
        thankyou.destroy()
        sys.exit('Program Ended')

    global img_tk  # Access the global variable

    # Create the main Tkinter window
    thankyou = Toplevel()
    thankyou.geometry("830x830")  # Adjust the size as needed
    thankyou.title("Thank you!")
    thankyou.configure(background='#ADD8E6')


    close_button = Button(thankyou, text="Close", command=endit, height=2, width=10)
    close_button.pack(side="bottom", padx=5,pady=10)

    # Load and resize the image
    img = Image.open("smart shelf groceries.png")  # Make sure the image file name is correct
    img = img.resize((600, 800), Image.BICUBIC)  # Use BICUBIC for resizing
    img_tk = ImageTk.PhotoImage(img)

    panel = Label(thankyou, image=img_tk,bg="#ADD8E6")
    panel.pack(side="top", fill="both", expand="yes")

    thankyou.mainloop()


