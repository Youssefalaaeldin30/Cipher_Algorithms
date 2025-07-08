import math
import tkinter as tk
from tkinter import ttk
import customtkinter

# Numerical Methods Imports
from Caesar_Cipher import Caesar_Cipher
from Monoalphabetic_Cipher import Monoalphabetic_Cipher 
from RailFence_Cipher import RailFence_Cipher
from ployalphabetic_Cipher import Polyalphabetic_Cipher
from Playfair_Cipher import Playfair_Cipher

# App Configuration
customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Cipher Techniques")
app.geometry("1400x1050")

tabview = customtkinter.CTkTabview(app, width=1400, height=750)
methods = [
   "Caesar Cipher", "Monoalphabetic Cipher", "RailFence Cipher", "Polyalphabetic Cipher", "Playfair Cipher"
]
for method in methods:
    tabview.add(method)
tabview.set("Caesar Cipher")
tabview.pack()

# Helper Functions
def create_input(tab_name, rely=0.15):
    entries = {}
    label = customtkinter.CTkLabel(tabview.tab(tab_name), text="Input")
    label.place(relx=0.17, rely=rely-0.04, anchor=tk.CENTER)
    entry = customtkinter.CTkEntry(tabview.tab(tab_name), placeholder_text="Text", width=350, height=150)
    entry.place(relx=0.18, rely=rely+ .09, anchor=tk.CENTER)
    entries["Equation"] = entry
    return entries

def create_mode_selector(tab_name, rely=.07):
    var = tk.StringVar(value="encode")
    customtkinter.CTkRadioButton(tabview.tab(tab_name), text="Encode", variable=var, value="encode").place(relx=0.45, rely=rely, anchor=tk.CENTER)
    customtkinter.CTkRadioButton(tabview.tab(tab_name), text="Decode", variable=var, value="decode").place(relx=0.55, rely=rely, anchor=tk.CENTER)
    return var

def create_key(tab_name, rely=0.1):
    key_label = customtkinter.CTkLabel(tabview.tab(tab_name), text="Enter Key (Our Compass)")
    key_label.place(relx=0.5, rely=rely -0.03, anchor=tk.CENTER)
    key_entry = customtkinter.CTkEntry(tabview.tab(tab_name), placeholder_text="Key", width=250, height=30)
    key_entry.place(relx=0.5, rely=rely+0.01, anchor=tk.CENTER)
    return key_entry

# Special Function for Caesar Cipher Alphabet
def create_alphabet(tab_name, rely=0.08):
    alphabet_label = customtkinter.CTkLabel(tabview.tab(tab_name), text="Enter Alphabet")
    alphabet_label.place(relx=0.5, rely=rely + 0.04, anchor=tk.CENTER)
    alphabet_entry = customtkinter.CTkEntry(tabview.tab(tab_name), placeholder_text="EX:A-Z", width=350, height=30)
    alphabet_entry.place(relx=0.5, rely=rely + 0.08, anchor=tk.CENTER)
    return alphabet_entry

# Modify the Output Field to Look Like Input (CTkEntry)
def create_output_field(tab_name, rely=0.15):
    output_label = customtkinter.CTkLabel(tabview.tab(tab_name), text="Output")
    output_label.place(relx=0.82, rely=rely-0.04, anchor=tk.CENTER)
    output_field = customtkinter.CTkEntry(tabview.tab(tab_name), placeholder_text="Output", width=350, height=150, state="readonly")
    output_field.place(relx=0.82, rely=rely+ .09, anchor=tk.CENTER)
    return output_field

def add_solver_button(tab_name, command, rely=0.32):
    customtkinter.CTkButton(
        tabview.tab(tab_name), text="Solve", fg_color="green", command=command
    ).place(relx=0.5, rely=rely, anchor=tk.CENTER)

# Caesar Cipher
mode_caesar = create_mode_selector("Caesar Cipher")
caesar_entries = create_input("Caesar Cipher")
key_entry_caesar = create_key("Caesar Cipher", rely=0.25)
alphabet_entry_caesar = create_alphabet("Caesar Cipher", rely=0.1)  # Alphabet only for Caesar
output_field_caesar = create_output_field("Caesar Cipher")

def solve_Caesar_Cipher():
    func = caesar_entries["Equation"].get()
    key = key_entry_caesar.get()
    alphabet = alphabet_entry_caesar.get()
    mode = mode_caesar.get()
    result = Caesar_Cipher(func, key, alphabet, mode)
    output_field_caesar.configure(state="normal")
    output_field_caesar.delete(0, tk.END)
    output_field_caesar.insert(0, result)
    output_field_caesar.configure(state="readonly")
add_solver_button("Caesar Cipher", solve_Caesar_Cipher)

# Monoalphabetic Cipher
mode_mono = create_mode_selector("Monoalphabetic Cipher")
mono_entries = create_input("Monoalphabetic Cipher")
key_entry_mono = create_key("Monoalphabetic Cipher", rely=0.25)
output_field_mono = create_output_field("Monoalphabetic Cipher")

def solve_Monoalphabetic_Cipher():
    func = mono_entries["Equation"].get()
    key = key_entry_mono.get()
    mode = mode_mono.get()
    result = Monoalphabetic_Cipher(func, key, mode)
    output_field_mono.configure(state="normal")
    output_field_mono.delete(0, tk.END)
    output_field_mono.insert(0, result)
    output_field_mono.configure(state="readonly")

add_solver_button("Monoalphabetic Cipher", solve_Monoalphabetic_Cipher)

# RailFence Cipher
mode_rail = create_mode_selector("RailFence Cipher")
rail_entries = create_input("RailFence Cipher")
key_entry_rail = create_key("RailFence Cipher", rely=0.25)
output_field_rail = create_output_field("RailFence Cipher")

def solve_RailFence_Cipher():
    func = rail_entries["Equation"].get()
    key = key_entry_rail.get()
    mode = mode_rail.get()
    result = RailFence_Cipher(func, key, mode)
    output_field_rail.configure(state="normal")
    output_field_rail.delete(0, tk.END)
    output_field_rail.insert(0, result)
    output_field_rail.configure(state="readonly")

add_solver_button("RailFence Cipher", solve_RailFence_Cipher)

# Polyalphabetic Cipher
mode_ploy = create_mode_selector("Polyalphabetic Cipher")
ploy_entries = create_input("Polyalphabetic Cipher")
key_entry_ploy = create_key("Polyalphabetic Cipher", rely=0.25)
output_field_ploy = create_output_field("Polyalphabetic Cipher")

def solve_ployalphabetic_Cipher():
    func = ploy_entries["Equation"].get()
    key = key_entry_ploy.get()
    mode = mode_ploy.get()
    result = Polyalphabetic_Cipher(func, key, mode)
    output_field_ploy.configure(state="normal")
    output_field_ploy.delete(0, tk.END)
    output_field_ploy.insert(0, result)
    output_field_ploy.configure(state="readonly")

add_solver_button("Polyalphabetic Cipher", solve_ployalphabetic_Cipher)

# Playfair Cipher
mode_fair = create_mode_selector("Playfair Cipher")
playfair_entries = create_input("Playfair Cipher")
key_entry_fair = create_key("Playfair Cipher", rely=0.25)
output_field_fair = create_output_field("Playfair Cipher")

def solve_Playfair_Cipher():
    func = playfair_entries["Equation"].get()
    key = key_entry_fair.get()
    mode = mode_fair.get()
    result = Playfair_Cipher(func, key, mode)
    output_field_fair.configure(state="normal")
    output_field_fair.delete(0, tk.END)
    output_field_fair.insert(0, result)
    output_field_fair.configure(state="readonly")

add_solver_button("Playfair Cipher", solve_Playfair_Cipher)

app.mainloop()