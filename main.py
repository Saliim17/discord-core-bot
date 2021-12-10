import os
from dotenv import load_dotenv

from client.own_client import Own_client

if __name__ == '__main__':
    load_dotenv()

    client = Own_client()

    client.run(os.getenv("BOT_TOKEN"))
