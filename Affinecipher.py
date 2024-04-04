import tkinter as tk

def affine_encipher(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                ciphertext += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def affine_decipher(ciphertext, a, b):
    plaintext = ""
    a_inv = pow(a, -1, 26)  # Modular multiplicative inverse of 'a' modulo 26
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))
            else:
                plaintext += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
        else:
            plaintext += char
    return plaintext

def encrypt_decrypt():
    text = text_entry.get("1.0", "end-1c")
    choice = choice_var.get()
    a = int(a_entry.get())
    b = int(b_entry.get())

    if choice == 'Encrypt':
        ciphertext = affine_encipher(text, a, b)
        result_label.config(text="Enciphered Text: " + ciphertext)
    elif choice == 'Decrypt':
        plaintext = affine_decipher(text, a, b)
        result_label.config(text="Deciphered Text: " + plaintext)
    else:
        result_label.config(text="Invalid choice. Please select Encrypt or Decrypt.")

root = tk.Tk()
root.title("Affine Cipher")
root.configure(background='#f0f0f0')

# Text Entry
text_label = tk.Label(root, text="Enter Text:", bg='#f0f0f0')
text_label.grid(row=0, column=0, padx=5, pady=5)
text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Choose Encrypt or Decrypt
choice_var = tk.StringVar()
choice_var.set("Encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=choice_var, value="Encrypt", bg='#f0f0f0')
encrypt_radio.grid(row=1, column=0, padx=5, pady=5)
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=choice_var, value="Decrypt", bg='#f0f0f0')
decrypt_radio.grid(row=1, column=1, padx=5, pady=5)

# 'a' and 'b' values Entry
a_label = tk.Label(root, text="Enter 'a' value:", bg='#f0f0f0')
a_label.grid(row=2, column=0, padx=5, pady=5)
a_entry = tk.Entry(root)
a_entry.grid(row=2, column=1, padx=5, pady=5)
b_label = tk.Label(root, text="Enter 'b' value:", bg='#f0f0f0')
b_label.grid(row=2, column=2, padx=5, pady=5)
b_entry = tk.Entry(root)
b_entry.grid(row=2, column=3, padx=5, pady=5)

# Button to encrypt/decrypt
encrypt_button = tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt, bg='#008CBA', fg='white', padx=10, pady=5)
encrypt_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Result Label
result_label = tk.Label(root, text="", bg='#f0f0f0')
result_label.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()