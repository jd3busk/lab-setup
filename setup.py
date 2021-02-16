#!/usr/bin/env python
import os

### FUNCTIONS

def aptupdate():
    os.system('sudo apt-get update')

def aptinstall(package):
    os.system('sudo apt-get install -y {}'.format(package))

def aptremove(package):
    os.system('sudo apt-get remove -y {}'.format(package))

def aptrepo(repo_location):
    os.system('sudo add-apt-repository -y {}'.format(repo_location))

def user2grp(group):
    os.system('sudo usermod -aG {} $USER'.format(group))

def snapinstall(package):
    os.system('sudo snap install --classic {}'.format(package))

def getcookie(fileId):
    os.system('curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id={}" > /dev/null'.format(fileId))

def getfiles(fileName, fileId, filePath):
    getcookie(fileId)
    code = os.popen("awk '/_warning_/ {print $NF}' /tmp/cookie").read().strip()
    os.system('curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm={}&id={}" -o {}'.format(code, fileId, fileName))
    os.system('mkdir -p {} && unzip {} -d {}'.format(filePath, fileName, filePath))

def addgpgkey(gpg_url):
    os.system('curl -fsSL {} | sudo apt-key add -'.format(gpg_url))

### VARIABLES

add_prereqs = [
    'curl',
    'tree',
    'vim'
]

add_gpg_keys = {
    'Docker':'https://download.docker.com/linux/ubuntu/gpg'
}

add_apt_repos = {
    'gns3':'ppa:gns3/ppa',
    'docker':'deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable'
}

remove_apt_packages = [
    'docker',
    'docker-engine',
    'docker.io',
]

add_apt_packages = [
    'gns3-gui',
    'gns3-server',
    'xtightvncviewer',
    'curl',
    'vim',
    'konsole',
    'apt-transport-https',
    'ca-certificates',
    'docker-ce',
    'python3-venv',
    'nodejs'
]

add_snap_packages = [
    'atom',
    'code',
    'postman',
    'ngrok'
]

files = [
    {
        'name':'GNS3.zip',
        'id':'1M4c3GUJq9_APJs2Q6wymdW1_pLfikt80',
        'path':'~'
    },
    {
        'name':'gns3_controller.conf.zip',
        'id':'1D-G7_iIrfSs9JaK7SQadqtwRMu3P3iwY',
        'path':'~/.config/GNS3/2.2/'
    },
    {
        'name':'nso.zip',
        'id':'1sFZtdJuiGSeGnOmnJTyIMZa8HHoV6ILj',
        'path':'~/GNS3/images/DOCKER'
    }
]

groups = [
    'ubridge',
    'libvirt',
    'kvm',
    'wireshark',
    'docker',
]

### MAGIC

for package in add_prereqs:
    print("\n### Installing {} apt Package\n".format(package))
    aptinstall(package)

for gpg_name, gpg_url in add_gpg_keys.items():
    print("\n### Adding {} GPG Key from {}".format(gpg_name, gpg_url))
    addgpgkey(gpg_url)

for repo_name, repo_location in add_apt_repos.items():
    print("\n### Adding the {} Repository\n".format(repo_name))
    aptrepo(repo_location)

for package in remove_apt_packages:
    print("\n### Removing {} Package\n".format(package))
    aptremove(package)

aptupdate()

for package in add_apt_packages:
    print("\n### Installing {} apt Package\n".format(package))
    aptinstall(package)

for package in add_snap_packages:
    print("\n### Installing {} snap Package\n".format(package))
    snapinstall(package)

for file in files:
    print("\n### Downloading {} and Extracting to {}\n".format(file['name'], file['path']))
    getfiles(fileName=file['name'], fileId=file['id'], filePath=file['path'])

for group in groups:
    print("\n### Adding current user to the {} group\n".format(group))
    user2grp(group)
