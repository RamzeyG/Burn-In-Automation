# Burn-In-Automation
This project will be one script used to burn in and complete an assessment document to present to customers

# Installation
Use the following commands to be able to run my script:

Please use Git.
First Install git and clone the repository. Accessing the script from git
ensures you always have the most updated version. Use "git pull" when in the
project directory to get the latest updates.

This has been tested on WSL (Windows Subsystem for Linux), Arch Linux, Ubuntu Linux:
```
sudo apt install git -y
cd <your_location_you_want_the_project_to_download_to>
git clone git@github.com:RamzeyG/Burn-In-Automation.git
sudo apt install python
sudo apt install python-pip
sudo pip install paramiko
sudo pip install argparse
sudo pip install pexpect
sudo pip install numpy
sudo pip install tqdm
sudo apt install texlive-full -y
```
NOTE: texlive-full will take a long time to install. Its best to install over night. 

Arch Users: use "pacman -S" instead of "apt"

# Usage
