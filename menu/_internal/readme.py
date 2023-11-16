import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def read_readme():
    readme_text = """
    # VideoOmeo 🌐🎥

## Getting Started 🚀

To run VideoOmeo, follow these simple steps:

1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. Clone this repository to your local machine.

    ```bash
    git clone 
    ```

3. Navigate to the project directory.

    ```bash
    cd VideoOmeo
    ```

4. Run the VideoOmeo.exe file.

5. Choose an option from the menu to start using VideoOmeo.

## Batch Download 🔄

If you want to download multiple videos, provide the links separated by commas. Follow the tutorial below to get links from TikTok:

1. Open TikTok and copy the video link.

2. Paste the link in VideoOmeo, add a comma, and press enter. Repeat this process for each video link.

    Example:
    ```
    
    ```

## Dependencies Installation 📦

To install the required dependencies, run the following commands sequentially:

```bash
pip install termcolor==1.1.0
pip install requests==2.26.0
pip install tqdm==4.62.3
pip install googletrans==4.0.0-rc1
pip install pyttsx3==2.90
pip install pytube==11.0.0
```

## Updating Python and Additional Dependency 🔧

Ensure you have Python version 3.8 or later installed. You can update Python using the following command:

```bash
pip install --upgrade python
```

To update the colorama library to version 0.4.4, run:

```bash
pip install --upgrade colorama==0.4.4
```

## Description ℹ️

VideoOmeo is a powerful video downloader that streamlines the process of acquiring videos from the internet. It is built using Python and utilizes various libraries for enhanced functionality.

### Features:

- **Simple Usage:** Download videos effortlessly by providing a single link.
- **Batch Download:** Download multiple videos simultaneously by separating links with commas.
- **Multilingual Support:** VideoOmeo supports multiple languages, ensuring a global user base can benefit from its capabilities.
- **Text-to-Speech:** Integrated with pyttsx3 for a speech synthesis feature, enabling users to receive auditory feedback on their actions.
- **Interactive Progress Bar:** The tqdm library provides users with a dynamic and visually appealing progress bar during the download process.

## Usage Example:

```bash
VideoOmeo.exe

1. Video Downloader
2. Github
3. License
4. QUIT

Enter your choice: 1

Downloading...

Video successfully downloaded to 'Downloads' folder.


```
# Enjoy your video downloading experience with VideoOmeo! If you find the program helpful, consider giving it a ⭐️ star!

    """

    print(readme_text)

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
            # Run menu.py using subprocess
            print("Going back to menu...")
            subprocess.run(["python", "menu.py"], shell=True)  # Modify if you are using a different Python launch command
        elif choice == '3':
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
