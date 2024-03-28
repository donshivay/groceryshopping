from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root=Tk()
def exit_command():
  root.destroy()
def continuecommand():
  root.destroy()
  def open_login_button():
    import Login_Button
  open_login_button()

root.geometry("650x650")
root.title("Smart Shelf Groceries")
icon_image = PhotoImage(file="icon.png")
root.iconphoto(True, icon_image)
img = ImageTk.PhotoImage(Image.open("icon.png"))
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")
button_frame= Frame(root)
continuebutton = ttk.Button(button_frame, text="Continue", default="active",command= continuecommand)
button_frame.pack(side="bottom", fill="x", padx=8, pady=8)
continuebutton.pack(side="right")
exit_button = ttk.Button(button_frame, text="Exit", default="normal",command=exit_command)
exit_button.pack(side="right", padx=8)

root.mainloop()
