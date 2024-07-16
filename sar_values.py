import csv
from bs4 import BeautifulSoup
import requests

# The provided HTML data
# html_data = requests.get('https://www.devicespecifications.com/en/model-sar/91dc5db0').text
html_data = requests.get('https://www.devicespecifications.com/en/model-sar/91dc5db0').text

print(html_data)

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

def extract_sar_values(table):
    sar_values = []
    if table:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['td', 'th'])
            cols = [col.text.strip() for col in cols]
            sar_values.append(cols)
    return sar_values

head_sar_eu_other_apple_models = soup.find('header', {'class': 'section-header'}).find_next('table')
body_sar_eu_other_apple_models = head_sar_eu_other_apple_models.find_next('header', {'class': 'section-header'}).find_next('table')
head_sar_usa_other_apple_models = body_sar_eu_other_apple_models.find_next('header', {'class': 'section-header'}).find_next('table')
body_sar_usa_other_apple_models = head_sar_usa_other_apple_models.find_next('header', {'class': 'section-header'}).find_next('table')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

head_sar_eu_other_brands = body_sar_usa_other_apple_models.find_next('header', {'class': 'section-header'}).find_next('table')
body_sar_eu_other_brands = head_sar_eu_other_brands.find_next('header', {'class': 'section-header'}).find_next('table')
head_sar_usa_other_brands = body_sar_eu_other_brands.find_next('header', {'class': 'section-header'}).find_next('table')
body_sar_usa_other_brands = head_sar_usa_other_brands.find_next('header', {'class': 'section-header'}).find_next('table')


with open('sar_values.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(['Model', 'SAR Value'])
    csv_writer.writerow([])
    
    csv_writer.writerow(['Head SAR (EU), other apple models'])
    csv_writer.writerows(extract_sar_values(head_sar_eu_other_apple_models))
    csv_writer.writerow([])

    csv_writer.writerow(['Body SAR (EU), other apple models'])
    csv_writer.writerows(extract_sar_values(body_sar_eu_other_apple_models))
    csv_writer.writerow([])

    csv_writer.writerow(['Head SAR (USA), other apple models'])
    csv_writer.writerows(extract_sar_values(head_sar_usa_other_apple_models))
    csv_writer.writerow([])

    csv_writer.writerow(['Body SAR (USA), other apple models'])
    csv_writer.writerows(extract_sar_values(body_sar_usa_other_apple_models))
    csv_writer.writerow([])

    csv_writer.writerow(['Head SAR (EU), models by other brands'])
    csv_writer.writerows(extract_sar_values(head_sar_eu_other_brands))
    csv_writer.writerow([])

    csv_writer.writerow(['Body SAR (EU), models by other brands'])
    csv_writer.writerows(extract_sar_values(body_sar_eu_other_brands))
    csv_writer.writerow([])

    csv_writer.writerow(['Head SAR (USA), models by other brands'])
    csv_writer.writerows(extract_sar_values(head_sar_usa_other_brands))
    csv_writer.writerow([])

    csv_writer.writerow(['Body SAR (USA), models by other brands'])
    csv_writer.writerows(extract_sar_values(body_sar_usa_other_brands))