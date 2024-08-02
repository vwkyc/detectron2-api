# Setup Instructions

1. Update package lists:
    ```sh
    sudo apt-get update
    ```

2. Install dependencies:
    ```sh
    sudo apt-get install -y libgl1-mesa-glx python3.8-venv
    ```

3. Create and activate a virtual environment:
    ```sh
    python3.8 -m venv detectron2_env
    source detectron2_env/bin/activate
    ```

4. Install Python dependencies:
    ```sh
    pip install -r temp_requirements.txt
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
    python app.py
    ```

havent tested ^