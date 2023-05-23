import requests
import json
import os
import git
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

print("Station status extraction completed. File saved in:", file_path)

# Define the local path to your GitHub repository and clone it if not present
repo_path = "C:/Users/Admin/bicicoru"  # Ruta local de tu repositorio de GitHub

# Clonar el repositorio si aún no está presente en la ruta local
if not os.path.exists(repo_path):
    git.Repo.clone_from("https://github.com/Gabriel44200/bicicor.git", repo_path)

# Inicializar el repositorio
repo = git.Repo(repo_path)

# Agregar el archivo JSON al índice
repo.index.add([file_path])

# Realizar un commit con un mensaje descriptivo
commit_message = f"Actualizar datos de estación: {current_date} {current_time}"
repo.index.commit(commit_message)

# Hacer push de los cambios al repositorio remoto
origin = repo.remote(name='origin')
origin.push()

