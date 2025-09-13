# bitgo_test

# BitGo Assessment Setup with BitGo Express

## Installation

### 1. Install Docker Desktop
Docker is required to run the BitGo Express container. Follow these steps to install it:

- **Download Docker Desktop**:
  - Visit [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
  - Click "Download for Windows" and save the installer (e.g., `DockerDesktopInstaller.exe`).

- **Run the Installer**:
  - Open PowerShell as Administrator:
    - Press `Win + S`, type `PowerShell`, right-click, and select "Run as Administrator".
  - Navigate to the download directory:
    ```powershell
    cd C:\Users\<YourUsername>\Downloads
    ```
  - Execute the installer:
    ```powershell
    .\DockerDesktopInstaller.exe
    ```
  - Follow the installation wizard, enabling WSL 2 if prompted (requires Windows 10 version 2004 or later).

- **Verify Installation**:
  - In PowerShell, run:
    ```powershell
    docker --version
    ```
  - Expected output: `Docker version XX.XX.X, build XXXXXX` (version may vary).

- **Start Docker Desktop**:
  - Launch Docker Desktop from the Start menu. Ensure it’s running (look for the Docker whale icon in the system tray).

### 2. Pull the BitGo Express Docker Image
Pull the latest BitGo Express image from Docker Hub.

- **Command**:
  - In PowerShell, run:
    ```powershell
    docker pull bitgo/express:latest
    ```
- **Expected Output**:
  ```
  latest: Pulling from bitgo/express
  Digest: sha256:40d6ac...
  Status: Image is up to date for bitgo/express:latest
  docker.io/bitgo/express:latest
  ```
- **Verify**:
  - Check available images:
    ```powershell
    docker images
    ```
  - Ensure `bitgo/express:latest` is listed.

### 3. Install Virtual Environment
Set up a virtual environment to manage Python dependencies.

- **Command**:
  - In PowerShell, run:
    ```powershell
    python -m pip install --user virtualenv
    ```

### 4. Create Virtual Environment
Create a virtual environment named `env`.

- **Command**:
  - In PowerShell, run:
    ```powershell
    python -m venv env
    ```

### 5. Activate Virtual Environment
Activate the virtual environment to isolate dependencies.

- **Command**:
  - On Windows (PowerShell), run:
    ```powershell
    env\Scripts\activate
    ```
  - Note: The `source env/bin/activate` command is for Unix-based systems (e.g., Linux/Mac). Use the Windows command above.

### 6. Install Dependencies
Install the required Python packages listed in `requirements.txt`.

- **Command**:
  - In PowerShell (with the virtual environment activated), run:
    ```powershell
    pip install -r requirements.txt
    ```
  - Note: Ensure `requirements.txt` exists in the project directory with at least `requests` (e.g., `requests`).

## Running the BitGo Express Docker Image

### 1. Run the Container
Start the BitGo Express container, mapping port 3080 on your machine to port 3080 in the container.

- **Command**:
  - In PowerShell, run:
    ```powershell
    docker run -it -p 3080:3080 bitgo/express:latest
    ```
- **Expected Output**:
  ```
  ...
  BitGo-Express running
  Environment: test
  Base URI: http://0.0.0.0:3080
  ```
- **Notes**:
  - Keep this PowerShell window open to keep the container running.
  - If port 3080 is in use, try a different port (e.g., 4000):
    ```powershell
    docker run -it -p 4000:4000 bitgo/express:latest
    ```
    Then update the Python script’s `BASE_URL` to `http://localhost:4000/api/v2`.

### 2. Test the Connection
Verify the BitGo Express server is running.

- **Command**:
  - In PowerShell, run:
    ```powershell
    curl http://localhost:3080/api/v2/ping
    ```
- **Expected Output**:
  ```
  {"status":"service is ok!","environment":"BitGo Testnet","configEnv":"testnet","configVersion":79}
  ```


### Configure Environment Variables

Create a .env file in the project directory to store environment-specific configurations.

Steps:

Create a file named .env in the root of your project directory.

Add the following fields to the .env file (leave the values blank or insert your specific values as needed):

BITGO_ACCESS_TOKEN=<insert your access token here>
BITGO_ENTERPRISE_ID=<insert your enterprise ID here>
BITGO_WALLET_PASSPHRASE=<insert your wallet passphrase here>
WEBHOOK_URL=<insert your webhook URL here>
WALLET_ID=<insert your wallet ID here>