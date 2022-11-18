import os
from dotenv import load_dotenv

from client import *

if __name__ == "__main__":
    load_dotenv()
    client = CustomClient()
    client.run(os.getenv('TOKEN'))