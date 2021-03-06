#文件读取模块，用于提供读取Json文件的函数
#readJson_poet: 用于读取诗词文件
#readJson_author: 用于读取作者

import json

# 读取json文件

# setting
from data.PythonAPI.setting import *


def __readJson(fileName:str)->list:
    '''Load json as list

    :param fileName: file name
    :return: A list of dictionary elements
    '''
    try:
        with open(fileName,'r',encoding='UTF-8') as f:
            returnList = json.load(f) # return a list(dict)
            f.close()
            return returnList
    except:
        raise OSError("File Open Error")

def readJsons_poet(songOrtang,filePath:str = path):
    '''Open thr poet's json

    :param songOrtang: Identify dynasty
    :param filePath: File path, the default path is relative
    :return: File path, the default path is relative
    '''
    assert songOrtang == "song" or songOrtang == 'tang',"ValueError"
    returnList = []
    maxRnge = tang_nums if songOrtang == "tang" else song_nums
    path_open = path_tang if songOrtang == "tang" else path_song
    for i in range(0,maxRnge,step):
        returnList = returnList + __readJson(path+path_open+str(i)+".json")
    return returnList

def readJsons_author(songOrtang,filePath:str = path):
    '''Open the author's json

    :param songOrtang: Identify dynasty
    :param filePath: File path, the default path is relative
    :return: File path, the default path is relative
    '''
    assert songOrtang == "song" or songOrtang == 'tang', "ValueError"
    return __readJson(path+"authors."+songOrtang+".json")

if __name__ == "__main__":
    f = readJsons_poet("tang")
    print(f[0]["paragraphs"])
    print(sorted(f[0]["paragraphs"][0]))
