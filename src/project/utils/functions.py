from dotenv import load_dotenv
import os, json


def get_secret (secret : str) -> str:
    """
    Load secrets.txt file and collect the secret wanted.
    """
    load_dotenv("secrets.txt")
    
    return(os.getenv(secret))


def save_as_json (data : str, path="outputs/data.json") -> None:
    """
    Save data in a json file following the path.
    """

    with open(path, 'w', encoding="utf-8") as file:
        json.dump(data.json(), file, indent=4, ensure_ascii=False, sort_keys=False)
