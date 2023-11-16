# Tu importuj moduły lub dodaj inne potrzebne instrukcje
import os

# Tekst do wyświetlenia
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

# Tekst z licencją
license_text = """
MIT License

Copyright (c) [year] [author]

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

# Opcje pod licencją
print(big_text)

print("\n1. QUIT To Menu")
print("2. Wyświetl Licencję")

user_choice = input("Wybierz opcję: ")

if user_choice == "1":
    # Powrót do menu
    os.system("python menu.py")
elif user_choice == "2":
    # Wyświetlanie licencji
    print(license_text)
    
    # Dodatkowa opcja dla wyświetlonej licencji
    print("\n1. Powrót do Menu")
    print("2. QUIT")

    user_choice_license = input("Wybierz opcję: ")

    if user_choice_license == "1":
        os.system("python menu.py")
    elif user_choice_license == "2":
        exit()  # Wyjście z programu
    else:
        print("Nieprawidłowa opcja. Wybierz 1 lub 2.")
else:
    print("Nieprawidłowa opcja. Wybierz 1 lub 2.")
