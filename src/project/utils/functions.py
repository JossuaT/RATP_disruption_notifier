from dotenv import load_dotenv
import os

def get_secret (secret : str) -> str:
    """
    Load secrets.txt file and collect the secret wanted.
    """
    load_dotenv("secrets.txt")
    
    return(os.getenv(secret))