import tkinter as tk
from crypto import symCrypt

# Function to toggle between encryption and decryption frames
def toggle_frame():
    if encryption_frame.winfo_ismapped():  # If the encryption frame is currently displayed
        decryption_frame.grid(row=0, column=0, sticky='nsew')  # Show the decryption frame
        encryption_frame.grid_forget()  # Hide the encryption frame
        toggle_button.config(text="Switch to Encryption")  # Update button text
    else:  # If the decryption frame is displayed
        encryption_frame.grid(row=0, column=0, sticky='nsew')  # Show the encryption frame
        decryption_frame.grid_forget()  # Hide the decryption frame
        toggle_button.config(text="Switch to Decryption")  # Update button text

sc = symCrypt()

# Function triggered when the Encrypt button is pressed
def encrypt_button_pressed():
    password = recipient_public_key_entry.get()  # Get the password from the input field
    data = encryption_entry.get()  # Get the text to encrypt from the input field
    encrypted_text = sc.encrypt(data, password)  # Encrypt the data using the password
    encrypted_text_entry.delete(0, tk.END)  # Clear the output field
    encrypted_text_entry.insert(0, encrypted_text)  # Display the encrypted text in the output field

# Function triggered when the Decrypt button is pressed
def decrypt_button_pressed():
    password = private_key_entry.get()  # Get the password from the input field
    token = decryption_entry.get()  # Get the encrypted message from the input field
    decrypted_text = sc.decrypt(token, password)  # Decrypt the message using the password
    decrypted_text_entry.delete(0, tk.END)  # Clear the output field
    decrypted_text_entry.insert(0, decrypted_text)  # Display the decrypted text in the output field

# Create the main application window
window = tk.Tk()
window.title('Encryption Tool')  # Set the title of the application
window.geometry("500x400")  # Set the dimensions of the application window

# Create separate frames for encryption and decryption
encryption_frame = tk.Frame(window)  # Frame for encryption operations
decryption_frame = tk.Frame(window)  # Frame for decryption operations

# Toggle button to switch between encryption and decryption modes
toggle_button = tk.Button(window, text="Switch to Decryption", command=toggle_frame)
toggle_button.grid(row=1, column=0, columnspan=2)  # Position the button

# Configure the Encryption Frame
tk.Label(encryption_frame, text="Password: ").grid(row=1, column=0)  # Label for password input
recipient_public_key_entry = tk.Entry(encryption_frame, width=30)  # Entry field for password
recipient_public_key_entry.grid(row=1, column=1)

tk.Label(encryption_frame, text="Message to Encrypt: ").grid(row=2, column=0)  # Label for message input
encryption_entry = tk.Entry(encryption_frame, width=30)  # Entry field for message
encryption_entry.grid(row=2, column=1)

encrypt_button = tk.Button(encryption_frame, text="Encrypt", command=encrypt_button_pressed)  # Encrypt button
encrypt_button.grid(row=3, column=0, columnspan=2)  # Position the button
encryption_result_label = tk.Label(encryption_frame, text="Encrypted Text:")  # Label for encrypted text
encryption_result_label.grid(row=4, column=0, sticky='e')
encrypted_text_entry = tk.Entry(encryption_frame, width=30)  # Output field for encrypted text
encrypted_text_entry.grid(row=4, column=1, sticky='w')

# Configure the Decryption Frame
tk.Label(decryption_frame, text="Password: ").grid(row=0, column=0)  # Label for password input
private_key_entry = tk.Entry(decryption_frame, width=30)  # Entry field for password
private_key_entry.grid(row=0, column=1)

tk.Label(decryption_frame, text="Encrypted Message: ").grid(row=1, column=0)  # Label for encrypted message input
decryption_entry = tk.Entry(decryption_frame, width=30)  # Entry field for encrypted message
decryption_entry.grid(row=1, column=1)

decrypt_button = tk.Button(decryption_frame, text="Decrypt", command=decrypt_button_pressed)  # Decrypt button
decrypt_button.grid(row=2, column=0, columnspan=2)  # Position the button
decryption_result_label = tk.Label(decryption_frame, text="Decrypted Text: ")  # Label for decrypted text
decryption_result_label.grid(row=4, column=0, sticky='e')
decrypted_text_entry = tk.Entry(decryption_frame, width=30)  # Output field for decrypted text
decrypted_text_entry.grid(row=4, column=1, sticky='w')

# Initially display the encryption frame
encryption_frame.grid(row=0, column=0, sticky='nsew')
