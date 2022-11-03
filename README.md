# automated-ssh
python script to run shell command in WSL-2

Upgrade from WSL to WSL-2 in Windows 10
https://winaero.com/update-from-wsl-to-wsl-2-in-windows-10/
segovelo@LAPTOP-T0H2E05J:~$wsl --set-version Ubuntu-20.04 2
segovelo@LAPTOP-T0H2E05J:~$wsl -l -v

OpenSSH server setup in  WSL-2
https://www.youtube.com/watch?v=TJ1buhbhgDQ
segovelo@LAPTOP-T0H2E05J:~$sudo ssh-keygen -A
segovelo@LAPTOP-T0H2E05J:~$sudo apt install net-tools
segovelo@LAPTOP-T0H2E05J:~$ sudo service ssh start
segovelo@LAPTOP-T0H2E05J:~$sudo ufw allow ssh
segovelo@LAPTOP-T0H2E05J:~$ sudo service ssh stop

Automated ssh comands in python
https://www.youtube.com/watch?v=DYYxLSrJdW8&list=RDCMUC8wZnXYK_CGKlBcZp-GxYPA&index=8

Dependecies:
pip install fabric
pip install python-dotenv
