# Import necessary libraries
from tkinter import *
import pyperclip
import random

# Create tkinter object
root = Tk()

# Set the width and height of the output window
root.geometry("800x600")

# Initializing parameters
input_pass = StringVar()
pass_len = IntVar()
pass_len.set(0)


# A function to generate the password
def generate():
    # The password will be a combination of these keys/elements
    combinations = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                    '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password = ""

    # Create password of desired length
    for i in range(pass_len.get()):
        password = password + random.choice(combinations)

    # Set the password to the entry widget
    input_pass.set(password)


# A function to copy the password to the clipboard
def CopyToClipboard():
    input_password = input_pass.get()
    pyperclip.copy(input_password)


# Heading of our application
Label(root, text="Password Generator Application", font="jost 30 bold").pack()

# Create a text label widget
Label(root, text="Enter password length", font="jost 20").pack(pady=7)

# Create a entry widget to take password length entered by the user
Entry(root, textvariable=pass_len, font='20').pack(pady=3)

# Button to call the generate function
Button(root, text="Generate Password", command=generate).pack(pady=7)

# Entry widget to show the generated password
Entry(root, textvariable=input_pass, font='20').pack(pady=3)

# Button to call the CopyToClipboard function
Button(root, text="Copy", command=CopyToClipboard).pack()

# mainloop() is an infinite loop which doesn't exit the application unless the user demands so.
root.mainloop()
