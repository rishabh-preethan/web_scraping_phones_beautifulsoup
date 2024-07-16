from bs4 import BeautifulSoup
import requests
import csv


html_text = requests.get('https://www.devicespecifications.com/en/model/91dc5db0').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
blue_div = soup.select_one('div[style"overflow: hidden; margin-top: 40px; position:relative;"]')
print(blue_div)
# specs_div = blue_div.find('div', id= 'model-brief-specifications')
# print('VALUE:',specs_div)

# device_specs = {}

# for spec in specs_div.find_all('b'):
#     key = spec.text.replace(':', '').strip()
#     value = spec.next_sibling.strip()
#     device_specs[key] = value

# csv_file_path = 'device_specifications.csv'

# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in device_specs.items():
#         writer.writerow([key, value])

# print(f'Device specifications saved to {csv_file_path}')