import requests

def download_url_content(url, output_file):
    """
    Downloads content from a given URL and saves it to a specified file.
    """
    try:
        response = requests.get(url)  
        response.raise_for_status()  

        with open(output_file, 'wb') as file:
            file.write(response.content)  

        print(f"Content successfully downloaded and saved to: {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading content: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("URL Content Downloader")
    
    url = input("Enter the URL to download content from: ").strip()
    output_file = input("Enter the path to save the content: ").strip()
    
    download_url_content(url, output_file)
