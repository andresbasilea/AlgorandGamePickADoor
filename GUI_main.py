import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import algorandGameTransaction
from algorandGameLogin import LoginWindow

door_image_path = "doorclosed.png"
value_bet = None
door_prize = random.randint(1,3)
#door_prize = 1 # for testing purposes

base = 1000000


root = tk.Tk()
root.withdraw()
login_window = LoginWindow(root)
# public_key, private_key = login_window.login()
root.wait_window(login_window) 
root.destroy()

algorandGameTransaction.get_public_key_user(login_window.public_key)
algorandGameTransaction.get_private_key_user(login_window.private_key)

initial_balance = algorandGameTransaction.get_balance()



# print(public_key, private_key)

#print(login_window.private_entry)


def door_clicked(door_num):
    global initial_balance
    global value_bet
    global base
    door_prize = random.randint(1,3)
    # door_prize = 1 # testing purposes

    if algorandGameTransaction.get_balance()/base < 3:
        messagebox.showinfo("Insufficient Funds", "Sorry, you need at least 3 Algos to play")
        return

    if value_bet == None:
        messagebox.showinfo("Error", "Error: You must select a bet value first!")
        return 

    if door_num == door_prize:
        messagebox.showinfo("Congrats!", "You selected door {} and won {} Algos".format(door_num,value_bet*2))
        initial_balance = initial_balance + (value_bet * 2 * base)
        user_balance_label.config(text="Balance: {} Algos".format(float(initial_balance/(base))))
        algorandGameTransaction.client_wins(value_bet)


    else:
        messagebox.showinfo("Sorry!", "You selected door {}, but the prize was in door {}".format(door_num, door_prize))
        initial_balance = initial_balance - (value_bet * base)
        user_balance_label.config(text="Balance: {} Algos".format(float(initial_balance/(base))))
        stop_user = algorandGameTransaction.client_looses(value_bet)


def image_clicked(value):
    global value_bet
    global base
    value_bet = value
    #messagebox.showinfo("You clicked", "Value: {}".format(value))
    last_value_label.config(text="Bet: {} Algos".format(value))  # Update the value in the label
    # user_balance_label.config(text="Balance: {}".format(algorandGameTransaction.get_balance())) 

def create_doors():
    doors_frame = tk.Frame(root)
    doors_frame.pack(pady=20)

    door_images = [
        Image.open(door_image_path), 
        Image.open(door_image_path),
        Image.open(door_image_path)
    ]

    max_width = max(image.width for image in door_images)
    max_height = max(image.height for image in door_images)
    target_width = 300
    target_height = 500
    scale_factor = min(target_width / max_width, target_height / max_height)

    for i in range(1, 4):
        door_image = door_images[i-1].resize((int(max_width * scale_factor), int(max_height * scale_factor)))
        door_photo = ImageTk.PhotoImage(door_image)
        door_btn = tk.Button(doors_frame, image=door_photo,
                             width=int(max_width * scale_factor), height=int(max_height * scale_factor),
                             command=lambda door_num=i: door_clicked(door_num))
        door_btn.image = door_photo
        door_btn.grid(row=0, column=i-1, padx=10)

def create_images():
    images_frame = tk.Frame(root)
    images_frame.pack(pady=20)

    image_values = [1, 2, 3]

    for i in range(3):
        image_path = "coin{}.png".format(i+1) 
        image = Image.open(image_path)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        image_btn = tk.Button(images_frame, image=photo,
                              width=100, height=100,
                              command=lambda value=image_values[i]: image_clicked(value))
        image_btn.image = photo
        image_btn.grid(row=0, column=i, padx=10)



if login_window.is_logged_in():
    # def open_main_window():

    # print(login_window.private_entry)
    root = tk.Tk()
    root.title("BasileKeller's Algorand Pick A Door")



    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 1000) // 2
    y = (screen_height - 679) // 2

    root.geometry("1000x679+{}+{}".format(x, y)) 



    bg_image = Image.open("background.png") 
    bg_image = bg_image.resize((1000, 679))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    create_doors()
    create_images()

    last_value_label = tk.Label(root, bg="#c3f2f7", text="Bet: ", font=("Montserrat", 12))
    last_value_label.pack(pady=0)

    user_balance_label = tk.Label(root, bg="#c3f2f7", text="Balance: ", font=("Montserrat", 12))
    user_balance_label.config(text="Balance: {} Algos".format(float(initial_balance/(base))))
    user_balance_label.pack(pady=0)


    photo_user_balance_label = ImageTk.PhotoImage(file="algorand.png")
    user_balance_label_image = tk.Label(root, bg="#c3f2f7")
    user_balance_label_image.config(image=photo_user_balance_label)
    user_balance_label_image.pack()

    root.resizable(False, False)  
    root.mainloop()

else:
    print("Auth error")

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window

#     login_window = LoginWindow(root)
#     login_window.mainloop()  # Display the login window and wait for it to close

#     if login_window.is_logged_in():
#         open_main_window()
#     else:
#         root.destroy() 


# if __name__ == "__main__":
#       # Hide the root window

#      # Wait for the login window to close

#     if login_window.is_logged_in():
#         open_main_window()
