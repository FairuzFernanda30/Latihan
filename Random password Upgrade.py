import random
import string
import tkinter as tk
import tkinter.messagebox as msgbox


def generate_password(length, use_symbols):
    # Menggabungkan karakter alfabet kecil, huruf besar, dan angka
    characters = string.ascii_letters + string.digits
    if use_symbols:
        # Menambahkan karakter simbol jika opsi "Use Symbols" diaktifkan
        characters += string.punctuation
    # Membuat password secara acak dengan menggunakan karakter-karakter yang sudah ditentukan
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def generate_button_clicked():
    # Mendapatkan nilai panjang password yang diinginkan dan opsi "Use Symbols" dari widget input
    password_length = int(length_entry.get())
    use_symbols = symbols_var.get()
    # Memanggil fungsi generate_password() dan menampilkan password yang dihasilkan
    password = generate_password(password_length, use_symbols)
    password_label.config(text=password)


def clear_button_clicked():
    # Menghapus password yang dihasilkan dari label
    password_label.config(text="")


def copy_button_clicked():
    # Menyalin password ke clipboard
    password = password_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        msgbox.showinfo("Password Generator", "Password copied to clipboard!")
    else:
        msgbox.showwarning("Password Generator", "No password to copy!")


# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Password Generator")

# Membuat widget untuk memasukkan panjang password yang diinginkan
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Membuat widget untuk memilih apakah akan menggunakan karakter simbol
symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Use Symbols", variable=symbols_var)
symbols_checkbox.pack()

# Membuat tombol untuk menghasilkan password baru
generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

# Membuat tombol untuk menghapus password yang dihasilkan
clear_button = tk.Button(root, text="Clear", command=clear_button_clicked)
clear_button.pack()

# Membuat tombol untuk menyalin password ke clipboard
copy_button = tk.Button(root, text="Copy", command=copy_button_clicked)
copy_button.pack()

# Membuat label untuk menampilkan password yang dihasilkan
password_label = tk.Label(root, text="")
password_label.pack()

# Menjalankan jendela utama aplikasi
root.mainloop()
