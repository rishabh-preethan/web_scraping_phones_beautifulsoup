import requests
from bs4 import BeautifulSoup
import csv

def scrape_device_details(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Modify the following code based on the structure of the website
        device_name = soup.find('h1', {'itemprop': 'name'}).text.strip()
        release_date = soup.find('td', text='Release Date').find_next('td').text.strip()
        # Add more fields as needed

        return {'Device Name': device_name, 'Release Date': release_date}
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return None

def main():
    base_url = 'https://www.devicespecifications.com/en/model/e48a5dad'
    device_list = [
        '/en/model/',
        # Add more device URLs as needed
    ]

    data_list = []

    for device_url in device_list:
        full_url = f'{base_url}{device_url}'
        device_data = scrape_device_details(full_url)
        if device_data:
            data_list.append(device_data)

    # Save data to CSV
    headers = ['Device Name', 'Release Date']  # Add more headers as needed
    with open('device_details.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_list)

if __name__ == "__main__":
    main()
