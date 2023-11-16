VideoOmeo is a versatile Python-based tool designed to simplify the process of downloading videos from the internet. With an intuitive command-line interface, it allows users to easily download videos by providing a link. Additionally, users can download multiple videos at once by separating the links with commas.

## Getting Started

To run VideoOmeo, follow these simple steps:

1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

2. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/VideoOmeo.git
   ```

3. Navigate to the project directory.

   ```bash
   cd VideoOmeo
   ```

4. Run the program by executing the `VideoOmeo.bat` file.

   ```bash
   VideoOmeo.bat
   ```

5. Choose an option from the menu to start using VideoOmeo.

## Dependencies Installation

To install the required dependencies, run the following commands sequentially:

```bash
pip install termcolor==1.1.0
pip install requests==2.26.0
pip install tqdm==4.62.3
pip install googletrans==4.0.0-rc1
pip install pyttsx3==2.90
pip install pytube==11.0.0
```

## Updating Python and Additional Dependency

Ensure you have Python version 3.8 or later installed. You can update Python using the following command:

```bash
pip install --upgrade python
```

To update the `colorama` library to version 0.4.4, run:

```bash
pip install --upgrade colorama==0.4.4
```

## Description

VideoOmeo is a powerful video downloader that streamlines the process of acquiring videos from the internet. It is built using Python and utilizes various libraries for enhanced functionality.

### Features:
- **Simple Usage:** Download videos effortlessly by providing a single link.
- **Batch Download:** Download multiple videos simultaneously by separating links with commas.
- **Multilingual Support:** VideoOmeo supports multiple languages, ensuring a global user base can benefit from its capabilities.
- **Text-to-Speech:** Integrated with pyttsx3 for a speech synthesis feature, enabling users to receive auditory feedback on their actions.
- **Interactive Progress Bar:** The tqdm library provides users with a dynamic and visually appealing progress bar during the download process.

### Usage Example:

```bash
VideoOmeo.bat

1. Video Donwloader
2. Github
3. License
4. QUIT

Enter your choice: 1

Downloading...

Video successfully downloaded to 'Downloads' folder.
```

Enhance your video downloading experience with VideoOmeo! Feel free to contribute and make the tool even more robust.

## License

MIT License with No Modification for Personal Use. See [LICENSE.md](LICENSE.md) for details.
