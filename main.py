import getpass
from fabric import Connection, Config
from dotenv import load_dotenv
import os, re

load_dotenv()
pass_phrase = os.getenv("SSH_PASSPHRASE")
password = getpass.getpass("Enter your root password")
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

conn = Connection("172.17.59.186", user="<USERNAME>", config=config)
result = conn.run("ls -la", hide=True)
#print(result.stdout)
conn.run("pwd")
with conn.cd("/mnt/c/users/<USERNAME>/Desktop"):
    conn.run("touch test_file.txt")
    conn.run("pwd")
#conn.sudo("apt install vim")
#conn.run("neofetch")

result = conn.run("ifconfig")
lines = result.stdout.split("\n")
inet_lines = [l for l in lines if "inet " in l and "127.0.0.1" not in l]
span = re.search("inet ([0-9]+\.){3}[0-9]+", inet_lines[0]).span()
ip_address = inet_lines[0][span[0]+5:span[1]]
print(ip_address)
