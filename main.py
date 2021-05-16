from tkinter import *
from tkinter import messagebox

window = Tk()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Err", message="Please Enter an Input")
    else:
        is_ok = messagebox.askokcancel(title=web,
                                       message=f"Email : {email}\n Password:{password} \n Is it Ok to SAVE it")

        if is_ok:
            with open("pas_data.txt", "a") as data_file:
                data_file.write(f"{web} | {email}| {password}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window.title("Password  Manager")
# for Padding
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row=0, column=1)
# lables
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_lablel = Label(text="Password:")
pass_lablel.grid(row=3, column=0)

# Entry
web_entry = Entry(width=52)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "guptasiddhant214@gmail.com")
pass_entry = Entry(width=30)
pass_entry.grid(row=3, column=1)

# BUTTONS
gen_pas_button = Button(text="Generate Password")
gen_pas_button.grid(row=3, column=2)
add_button = Button(text="Add", width=46, command=save_file)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
