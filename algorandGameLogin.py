import tkinter as tk
from tkinter import messagebox, filedialog


class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Login with Basile Keller Wallet")
        self.logged_in = False  # Flag to indicate if the user is logged in
        self.public_key = ""
        self.private_key = ""

        welcome_label = tk.Label(self, text="Welcome! Please enter your public key.")
        welcome_label.pack(pady=10)

        keys_frame = tk.Frame(self)
        keys_frame.pack(pady=10)

        public_label = tk.Label(keys_frame, text="Public Key:")
        public_label.grid(row=0, column=0, padx=10, pady=5)
        self.public_entry = tk.Entry(keys_frame, width=40)
        self.public_entry.grid(row=0, column=1, padx=10, pady=5)

        private_label = tk.Label(keys_frame, text="Private Key:")
        private_label.grid(row=1, column=0, padx=10, pady=5)
        self.private_entry = tk.Label(keys_frame, width=40)
        self.private_entry.grid(row=1, column=1, padx=10, pady=5)

        browse_button = tk.Button(self, text="Browse", command=self.browse_files)
        browse_button.pack(pady=10)

        login_button = tk.Button(self, text="Login to Basile Keller Wallet", command=self.login)
        login_button.pack(pady=10)

    def browse_files(self):
        file_path = filedialog.askopenfilename(title="Select Private Key File")
        if file_path:
            try:
                with open(file_path, "r") as file:
                    keys = file.readlines()
                    self.public_entry.insert(tk.END, keys[1].strip())
                    self.private_entry = keys[0].strip()
                    #self.private_entry.insert(tk.END, keys[1].strip())
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def login(self):
        self.public_key = self.public_entry.get()
        self.private_key = self.private_entry    
        # print(private_key)
        
        if len(self.public_key) == 58:
            messagebox.showinfo("Login", f"Public Key: {self.public_key}\n")
            self.logged_in = True
        self.destroy()
        #return public_key, private_key

    def is_logged_in(self):
        return self.logged_in
