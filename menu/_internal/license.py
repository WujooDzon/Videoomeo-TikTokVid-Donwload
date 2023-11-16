# Import modules or add other necessary instructions
import os

# Text to display
big_text = """
      ▄█  ▄██████▄     ▄█    █▄    ███▄▄▄▄   ▄██   ▄           ▄████████    ▄████████     ███      ▄███████▄  
    ███ ███    ███   ███    ███   ███▀▀▀██▄ ███   ██▄        ███    ███   ███    ███ ▀█████████▄ ██▀     ▄██ 
    ███ ███    ███   ███    ███   ███   ███ ███▄▄▄███        ███    █▀    ███    ███    ▀███▀▀██       ▄███▀ 
    ███ ███    ███  ▄███▄▄▄▄███▄▄ ███   ███ ▀▀▀▀▀▀███       ▄███▄▄▄       ███    ███     ███   ▀  ▀█▀▄███▀▄▄ 
    ███ ███    ███ ▀▀███▀▀▀▀███▀  ███   ███ ▄██   ███      ▀▀███▀▀▀     ▀███████████     ███       ▄███▀   ▀ 
    ███ ███    ███   ███    ███   ███   ███ ███   ███        ███          ███    ███     ███     ▄███▀       
    ███ ███    ███   ███    ███   ███   ███ ███   ███        ███          ███    ███     ███     ███▄     ▄█ 
█▄ ▄███  ▀██████▀    ███    █▀     ▀█   █▀   ▀█████▀         ███          ███    █▀     ▄████▀    ▀████████▀ 
▀▀▀▀▀▀                                                                                                        
"""

# Text with license
license_text = """
MIT License

Copyright (c) 2023 WujooDzon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Options under the license
print(big_text)

print("\n1. QUIT To Menu")
print("2. Display License")

user_choice = input("Choose an option: ")

if user_choice == "1":
    # Return to the menu
    os.system("python menu.py")
elif user_choice == "2":
    # Display the license
    print(license_text)
    
    # Additional option for the displayed license
    print("\n1. Back to Menu")
    print("2. QUIT")

    user_choice_license = input("Choose an option: ")

    if user_choice_license == "1":
        os.system("python menu.py")
    elif user_choice_license == "2":
        exit()  # Exit the program
    else:
        print("Invalid option. Choose 1 or 2.")
else:
    print("Invalid option. Choose 1 or 2.")
