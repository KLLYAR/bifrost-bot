import os
from dotenv import load_dotenv

from client import ListenerClient
from sender import *

if __name__ == "__main__":
    load_dotenv()
    
    client = ListenerClient(Sender())
    client.run(os.getenv('TOKEN'))