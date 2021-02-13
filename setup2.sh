#!/bin/bash

### SET PERMISSIONS
sudo usermod -aG docker $USER

### DOWNLOAD NSO IMAGE FILES
fileId=1sFZtdJuiGSeGnOmnJTyIMZa8HHoV6ILj
fileName=nso.zip

cd /tmp/
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName}

mkdir -p ~/GNS3/images/DOCKER
unzip nso.zip -d ~/GNS3/images/DOCKER

cd ~/GNS3/images/DOCKER/nso/

docker build -t gns3/nso-base .
