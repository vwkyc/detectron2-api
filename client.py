import requests
import json

# The URL of your Detectron2 API
url = "https://example.com/detect"

# Path to the image file you want to analyze
image_path = "image.png"

# Open the image file
with open(image_path, "rb") as image_file:
    # Create a dictionary with the file to send
    files = {"image": image_file}
    
    # Send the POST request to the API
    try:
        response = requests.post(url, files=files)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        exit(1)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    results = response.json()
    
    # Print the detections
    for detection in results["detections"]:
        print(f"Class: {detection['class']}")
        print(f"Score: {detection['score']}")
        print(f"Bounding Box: {detection['box']}")
        print("---")
else:
    print(f"Error: {response.status_code}")
    print(response.text)