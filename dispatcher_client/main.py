from client import DispatcherClient

import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    
    client = DispatcherClient()
    client.run(os.getenv('TOKEN'))