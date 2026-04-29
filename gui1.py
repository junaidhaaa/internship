import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My App")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

#Add a button that closes the app
button=tk.Button(root, text="Exit", command=root.destroy)
button.pack()

# Start the application
root.mainloop()