import getpass
from fabric import Connection, Config

#password = getpass.getpass("Enter your password")
#config = Config(overrides={"sudo":{"password": password}})
conn = Connection("172.17.60.62", user="segovelo")#, config=config)
conn.run("ls -la")
