import logging
import os

# Define log directory and file
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "simulation.log")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_info(message):
    """Log an informational message."""
    logging.info(message)
    print(f"[INFO] {message}")

def log_warning(message):
    """Log a warning message."""
    logging.warning(message)
    print(f"[WARNING] {message}")

def log_error(message):
    """Log an error message."""
    logging.error(message)
    print(f"[ERROR] {message}")

def log_debug(message):
    """Log a debug message."""
    logging.debug(message)
    print(f"[DEBUG] {message}")
