import tkinter as tk
import textwrap as txtw

def destroy_window(root):
    root.destroy()

def gui_message_box(title:str="Message Box", message:str="", icon_im=""):
    # Window instanciation and initialization
    root = tk.Tk()
    root.title(title)

    # Load an icon image
    if icon_im:
        icon = tk.PhotoImage(file=icon_im)
        root.iconphoto(False, icon)

    # Widget class instanciation and initialization (Label and Button)
    button = tk.Button(root, text="OK", command=lambda:destroy_window(root))    
    wrapped_message = txtw.fill(message, width=30)
    label = tk.Label(root, text=wrapped_message)
    label.pack(padx= 10, pady=10)
    button.pack(pady=10)

    # /!\ Save updates
    root.update()

    # Dynamic window geometry
    x_window = root.winfo_width()
    y_window = root.winfo_height()
    x_offset = root.winfo_screenwidth() // 2
    y_offset = root.winfo_screenheight() // 2
    root.geometry(f"{x_window}x{y_window}+{x_offset - x_window // 2}+{y_offset - y_window // 2}")

    # Window display
    root.mainloop()