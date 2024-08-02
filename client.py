import requests

class Detectron2APIClientScene:
    INVOKE_URL = "http://localhost:5000/detect"

    def __init__(self, image_path):
        self.image_path = image_path
        self.payload = self._create_payload()

    def _create_payload(self):
        with open(self.image_path, "rb") as image_file:
            image_data = image_file.read()
        return image_data

    def send_request(self):
        print("Sending request to Detectron2 API")
        files = {'image': self.payload}
        try:
            response = requests.post(self.INVOKE_URL, files=files)
            response.raise_for_status()  # Raise an error for bad status codes
            result = response.text
        except requests.exceptions.RequestException as e:
            result = f"Error: {e}"
        
        print(result)
        return result
