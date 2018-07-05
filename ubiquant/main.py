import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

basePath = "./ubiquant/saved/"
baseUrl = "http://test.ubiquant.com/"

def getAbsoluteURL(baseUrl, source):
    url = baseUrl+source;
    return url

def getDownloadPath(filePath, basePath):
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
    downloadPath = getDownloadPath(filePath=filePath, basePath=basePath)
    # print(downloadUrl)
    # print(downloadPath)
    urlretrieve(downloadUrl, downloadPath)
    print("{0} out of {1} files downloaded.".format(i+1, len(downloadList)))
