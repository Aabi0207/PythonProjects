from tkinter import *
from tkinter import messagebox
import json
import random

# ------------------------------- PASSWORD GENERATOR ---------------------------------- #


def generate_password():
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
               ,'a','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symbols = ['!','@','#','$','%','^','&','*','(',')','_']
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    password_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for i in range(random.randint(2, 4))]

    random.shuffle(password_list)

    final_password = "".join(password_list)
    password_entry.insert(0, final_password)
# ------------------------------- SAVE PASSWORD --------------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="EMPTY ENTRY", message="You left something empty.")
    else:
        try:
            with open("data.json", "r") as data:
                # Reading old data
                previous_data = json.load(data)
                # Updating new data
                previous_data.update(new_data)

            with open("data.json", "w") as add_data:
                json.dump(previous_data, add_data, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------------- Find Password --------------------------------------- #

def find_password():
    website = website_entry.get()
    with open("data.json") as data:
        previous_data = json.load(data)
        try:
            fetched_email = previous_data[website]["email"]
            fetched_password = previous_data[website]["password"]
            messagebox.showwarning(title="Previous Password",
                                   message=f"email:{fetched_email}\npassword:{fetched_password}")
        except KeyError:
            messagebox.showwarning(message="You haven't saved password of any such website yet.")
        except json.decoder.JSONDecodeError:
            messagebox.showwarning(message="You haven't saved password of any such website yet.")
        except FileNotFoundError:
            messagebox.showwarning(message="No Data File found.")


# ------------------------------- UI SETUP --------------------------------------- #
window = Tk()
window.config(pady=20, padx=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="password_logo2.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=18)
website_entry.grid(row=1, column=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=36)
email_entry.insert(0, "abhishekbiradar0207@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightthickness=0, command=save)
add_button.grid(column=1, columnspan=2, row=4)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
