import os
from dotenv import load_dotenv

from client import CustomClient
from sender import *
from group import *
from broadcaster import *

if __name__ == "__main__":
    load_dotenv()
    
    client = CustomClient(Sender())
    client.run(os.getenv('TOKEN'))