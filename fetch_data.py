import requests
import dotenv
import os

dotenv.load_dotenv()

api_key = os.getenv("DOG_API_KEY")

def fetch_dogs(breed):
    url = "https://api.thedogapi.com/v1/breeds/search"
    params = {
        "q": breed
    }
    headers = {
        "x-api-key": api_key
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
    

if __name__ == "__main__":
    breed_type = input("Enter dog breed type (e.g., 'Terrier'): ")
    
    try:
        dogs_data = fetch_dogs(breed_type)
        
        print(f"##List of {breed_type} dogs##")
        for index in range(len(dogs_data)):
            print(f"Name #{index+1}: {dogs_data[index]["name"]}")
    except Exception as e:
        print(f"Error: {e}")

