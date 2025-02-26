import requests
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("heartbeat.log"),
        logging.StreamHandler()
    ]
)

def send_heartbeat():
    """Send a heartbeat request to the specified API endpoint."""
    url = "https://api.kmt.ltd/api/Auth/heartbeat"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Heartbeat successful: Status {response.status_code}")
        else:
            logging.warning(f"Heartbeat failed: Status {response.status_code}")
    except Exception as e:
        logging.error(f"Heartbeat error: {str(e)}")

def main():
    """Main function to run the heartbeat service."""
    interval_seconds = 120  # 2 minutes
    
    logging.info("Starting heartbeat service")
    logging.info(f"Sending heartbeat to https://api.kmt.ltd/api/Auth/heartbeat every {interval_seconds} seconds")
    
    try:
        while True:
            send_heartbeat()
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        logging.info("Heartbeat service stopped by user")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
