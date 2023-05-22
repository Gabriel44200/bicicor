import requests
import json
import os
from datetime import datetime

# Fetch the JSON data from the URL
station_status_url = "https://acoruna.publicbikesystem.net/customer/ube/gbfs/v1/en/station_status"

station_status_response = requests.get(station_status_url)
station_status_data = station_status_response.json()

# Get the current date and time
current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H-%M-%S")

# Create a folder with the current date if it doesn't exist
folder_name = f"status_data_{current_date}"
os.makedirs(folder_name, exist_ok=True)

# Save station status to a file with a timestamp
file_name = f"station_status_{current_time}.json"
file_path = os.path.join(folder_name, file_name)
with open(file_path, "w") as status_file:
    json.dump(station_status_data, status_file)

print("Station status extraction completed. File saved in:", folder_name)
