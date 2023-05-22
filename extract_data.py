import requests
import json
import os
from datetime import datetime

# Fetch the JSON data from the URL
station_status_url = "https://acoruna.publicbikesystem.net/customer/ube/gbfs/v1/en/station_status"

station_status_response = requests.get(station_status_url)
station_status_data = station_status_response.json()

# Get the current date and time
current_date = datetime.now().strftime("%d-%m-%Y")
current_time = datetime.now().strftime("%H-%M-%S")

# Create the "capturas" folder if it doesn't exist
capturas_folder = "capturas"
os.makedirs(capturas_folder, exist_ok=True)

# Create a folder with the current date if it doesn't exist
date_folder = os.path.join(capturas_folder, current_date)
os.makedirs(date_folder, exist_ok=True)

# Save station status to a file with the timestamp
file_name = f"station_status_{current_date}_{current_time}.json"
file_path = os.path.join(date_folder, file_name)
with open(file_path, "w") as status_file:
    json.dump(station_status_data, status_file)

# Commit and push changes to GitHub
commit_message = f"Auto-commit: Add dataset {current_date} {current_time}"
os.system("git add .")
os.system(f"git commit -m \"{commit_message}\"")
os.system("git push origin main")

print("Station status extraction completed. Dataset saved and pushed to GitHub.")
