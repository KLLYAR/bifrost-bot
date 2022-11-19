from group import *
from broadcaster import Broadcaster
from receiver import Receiver
from client import Custom2Client
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    
    client = Custom2Client()
    client.run(os.getenv('TOKEN'))