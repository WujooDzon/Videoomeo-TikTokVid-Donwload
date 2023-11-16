import requests
import os
import re
import time
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

large_text = f"""{Fore.BLUE}
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

def download_video(tiktok_url):
    api_endpoint = 'https://www.tikwm.com/api/'
    params = {
        'url': tiktok_url,
        'hd': 1
    }

    response = requests.get(api_endpoint, params=params)

    if response.status_code == 200:
        response_data = response.json()
        if response_data['code'] == 0:
            username = re.search(r'@(\w+)', tiktok_url).group(1)
            video_id = re.search(r'/video/(\d+)', tiktok_url).group(1)

            if not os.path.exists("downloads"):
                os.makedirs("downloads")

            filename = os.path.join("downloads", f"{username}_{video_id}.mp4")

            if not os.path.exists(filename):
                video_url_without_watermark = response_data['data']['play']
                video_data = requests.get(video_url_without_watermark, stream=True)

                total_size = int(video_data.headers.get('content-length', 0))

                with open(filename, 'wb') as video_file, tqdm(
                        desc=filename,
                        total=total_size,
                        unit='B',
                        unit_scale=True,
                        unit_divisor=1024,
                        ) as bar:
                    for data in video_data.iter_content(chunk_size=1024):
                        bar.update(len(data))
                        video_file.write(data)

                print(f"Video downloaded and saved as: {filename}")
            else:
                print(f"Video already exists: {filename}")
        else:
            print(f"Error: {response_data['msg']}")
    else:
        print("Error: Unable to obtain the video URL without watermark")

def main():
    print(large_text)

    user_input = input("Paste the TikTok link: ")

    if user_input:
        if user_input.endswith(".txt"):
            if os.path.isfile(user_input):
                with open(user_input, 'r') as file:
                    for line in file:
                        tiktok_url = line.strip()
                        download_video(tiktok_url)
                        time.sleep(1)
            else:
                print("Error: The provided file path does not exist.")
        else:
            tiktok_urls = [url.strip() for url in user_input.split(',')]
            for tiktok_url in tiktok_urls:
                download_video(tiktok_url)
                time.sleep(1)

    while True:
        download_again = input("Do you want to download another video? (y/n): ").lower()
        if download_again != 'y':
            break

        tiktok_url = input("Enter TikTok video URL: ")
        download_video(tiktok_url)
        time.sleep(1)

if __name__ == '__main__':
    main()
