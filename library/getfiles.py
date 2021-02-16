#!/usr/bin/python

import os

def getcookie(fileId):
    os.system('curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id={}" > /dev/null'.format(fileId))

def getfiles(fileName, fileId, filePath):
    getcookie(fileId)
    code = os.popen("awk '/_warning_/ {print $NF}' /tmp/cookie").read().strip()
    os.system('curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm={}&id={}" -o {}'.format(code, fileId, fileName))
    os.system('mkdir -p {} && unzip {} -d {}'.format(filePath, fileName, filePath))

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

for file in files:
    getfiles(fileName=file['name'], fileId=file['id'], filePath=file['path'])
