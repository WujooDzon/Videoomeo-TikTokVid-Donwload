import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def read_readme():
    with open('readme.txt', 'r') as file:
        readme_content = file.read()
    print(readme_content)

def print_purple_text():
    purple_text = f"""
{Fore.MAGENTA}

      ▄█  ▄██████▄     ▄█    █▄    ███▄▄▄▄   ▄██   ▄           ▄████████    ▄████████     ███      ▄███████▄  
    ███ ███    ███   ███    ███   ███▀▀▀██▄ ███   ██▄        ███    ███   ███    ███ ▀█████████▄ ██▀     ▄██ 
    ███ ███    ███   ███    ███   ███   ███ ███▄▄▄███        ███    █▀    ███    ███    ▀███▀▀██       ▄███▀ 
    ███ ███    ███  ▄███▄▄▄▄███▄▄ ███   ███ ▀▀▀▀▀▀███       ▄███▄▄▄       ███    ███     ███   ▀  ▀█▀▄███▀▄▄ 
    ███ ███    ███ ▀▀███▀▀▀▀███▀  ███   ███ ▄██   ███      ▀▀███▀▀▀     ▀███████████     ███       ▄███▀   ▀ 
    ███ ███    ███   ███    ███   ███   ███ ███   ███        ███          ███    ███     ███     ▄███▀       
    ███ ███    ███   ███    ███   ███   ███ ███   ███        ███          ███    ███     ███     ███▄     ▄█ 
█▄ ▄███  ▀██████▀    ███    █▀     ▀█   █▀   ▀█████▀         ███          ███    █▀     ▄████▀    ▀████████▀ 
▀▀▀▀▀▀                                                                                                        """
                                                                                                   
{Style.RESET_ALL}
"""
    print(purple_text)

def main_menu():
    print_purple_text()
    print("1. Read README")
    print("2. Back to menu")
    print("3. Quit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            read_readme()
        elif choice == '2':
            # Uruchomienie menu.py za pomocą subprocess
            print("Going back to menu...")
            subprocess.run(["python", "menu.py"], shell=True)  # Zmodyfikuj, jeśli używasz innego polecenia uruchamiającego Pythona
        elif choice == '3':
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
