import tkinter as tk

# Function to collect and print data
def submit():
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    
    print("Name:", name)
    print("Email:", email)
    print("Mobile:", mobile)

# Create the main window
root = tk.Tk()
root.title("My App")
root.geometry("300x250")

# Labels and Entry fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Mobile").pack()
mobile_entry = tk.Entry(root)
mobile_entry.pack()

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=10)

# Exit button
exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack()

# Start the application
root.mainloop()