# Setup Instructions

1. Update package lists:
    ```sh
    sudo apt-get update
    ```

2. Install dependencies:
    ```sh
    sudo apt-get install -y libgl1-mesa-glx git build-essential python3.8-venv python3.8-dev
    ```

3. Create and activate a virtual environment:
    ```sh
    python3.8 -m venv venv
    source venv/bin/activate
    ```

4. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Clone and install Detectron2:
    ```sh
    git clone https://github.com/facebookresearch/detectron2.git
    cd detectron2
    pip install -e .
    cd ..
    ```

6. Run the application:
    ```sh
    gunicorn -c gunicorn_config.py app:app
    ```

The application will be served on [http://localhost:5000/detect](http://localhost:5000/detect).

Tested working on Ubuntu Jammy 22.04 x86_64, Host: Windows Subsystem for Linux - Ubuntu (2.3.14).
