#!/usr/bin/env python3

import os

def main():
    
    ### Install GNS3
    os.system('ansible-playbook setup.yml -K')

    ### Import Device Images
    files = [
        {
            'name':'images.zip',
            'id':'15g07V1Bcou3IlgL6TUyx4JDqbH1R2b9b',
            'path':'~/GNS3/'
        },
        {
            'name':'gns3_controller.conf.zip',
            'id':'1ALfYSCLKWv6NmbouUOAiYFMExn7kz3O1',
            'path':'~/.config/GNS3/2.2/'
        },
    ]

    for file in files:
        fileName=file['name']
        fileId=file['id']
        filePath=file['path']

        os.system('curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id={}" > /dev/null'.format(fileId))
        code = os.popen("awk '/_warning_/ {print $NF}' /tmp/cookie").read().strip()
        os.system('curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm={}&id={}" -o {}'.format(code, fileId, fileName))
        os.system('mkdir -p {} && unzip {} -d {}'.format(filePath, fileName, filePath))
        os.system('rm {}'.format(fileName))

if __name__ == "__main__":
	main()
