#!/bin/bash

### INSTALL GNS3
sudo add-apt-repository ppa:gns3/ppa -y
sudo apt-get update -y                              
sudo apt-get install -y gns3-gui gns3-server xtightvncviewer curl vim konsole

### INSTALL DOCKER
sudo apt-get remove docker docker-engine docker.io -y
sudo apt autoremove -y
sudo apt-get install -y apt-transport-https ca-certificates curl 
sudo apt-get install -y software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) stable"

sudo apt-get update -y
sudo apt-get install -y docker-ce

### SET PERMISSIONS
sudo usermod -aG ubridge $USER
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
sudo usermod -aG wireshark $USER
sudo usermod -aG docker $USER

### DOWNLOAD DEVICE IMAGES
fileId=1d0DljVAst6yKcnile6hahopSgyRBOXfb
fileName=images.zip

cd /tmp/
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName}

unzip images.zip -d ~/GNS3/

### LOAD DEVICE IMAGES
fileId=1SovGnWWL43k0_oVjrayMCE-XQplzkMBO
fileName=gns3_controller.conf

cd /tmp/
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName}

mkdir -p ~/.config/GNS3/2.2/
cp ./gns3_controller.conf ~/.config/GNS3/2.2/


### DOWNLOAD DEVNET TOOLS
sudo apt-get install -y git python3-venv nodejs 
sudo snap install --classic atom
sudo snap install --classic code
sudo snap install --classic postman
sudo snap install --classic ngrok
sudo apt-get install -y vim
sudo rm /usr/bin/vi
sudo ln -s /usr/bin/vim /usr/bin/vi

reboot
