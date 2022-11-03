import getpass
from fabric import Connection, Config
from dotenv import load_dotenv
import os

load_dotenv()
pass_phrase = os.getenv("SSH_PASSPHRASE")
password = getpass.getpass("Enter your password")
config = Config(overrides={
    "sudo": {
        "password": password
        },
    "connect_kwargs": {
                "passphrase": pass_phrase  
    }
    })

connect_kwargs = {
    "passphrase": pass_phrase  
    }

conn = Connection("172.17.59.186", user="segovelo", config=config)
conn.run("ls -la")
