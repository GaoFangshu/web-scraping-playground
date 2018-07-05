import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "download"
baseUrl = "http://test.ubiquant.com/"

def getAbsoluteURL(baseUrl, source):
    url = baseUrl+source;
    return url

def getDownloadPath(filePath, basePath="./ubiquant/saved/"):
    path = basePath + filePath
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html = urlopen(baseUrl)
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll('a', href=True)[1:]


for i in range(len(downloadList)):
    filePath = downloadList[i]['href']
    downloadUrl = baseUrl + filePath
    downloadPath = getDownloadPath(filePath)
    # print(downloadUrl)
    # print(downloadPath)
    urlretrieve(downloadUrl, downloadPath)
    print(str(i+1)+" out of "+str(len(downloadList))+ " files downloaded.")
