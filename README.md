# Setup Instructions

1. Update package lists:
    ```sh
    # sudo add-apt-repository ppa:deadsnakes/ppa #if unable to install python3.8-venv
    sudo apt-get update
    ```

2. Install dependencies:
    ```sh
    sudo apt-get install -y libgl1-mesa-glx git build-essential python3.8-venv python3.8-dev
    ```

3. Create and activate a virtual environment:
    ```sh
    python3.8 -m venv detectron2_env
    source detectron2_env/bin/activate
    ```

4. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Clone and install Detectron2:
    ```sh
    git clone https://github.com/facebookresearch/detectron2.git
    cd detectron2
    python setup.py develop
    ```

served on http://localhost:5000/detect

tested working on Ubuntu jammy 22.04 x86_64 Host: Windows Subsystem for Linux - Ubuntu (2.3.14)
