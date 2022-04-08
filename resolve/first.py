from data.PythonAPI.setting import *
from data.PythonAPI.data_Config import readJsons_author,readJsons_poet
from data.PythonAPI.one_hot_Code import encode_And_wordFrequency
from data.PythonAPI.frequency import analysisTool,writeJson

if __name__ == "__main__":
    poetSong = readJsons_poet("song")
    poetTang = readJsons_poet("tang")
    # 编码 以及 各个朝代字频分析
    encode_And_wordFrequency(["song","tang"],poetSong,poetTang)
    # 词频分析
    fre_song = analysisTool(poetSong,"song")
    fre_tang = analysisTool(poetTang,"tang")
    fre_dict_song = fre_song.analysisFrequency()
    fre_dict_tang = fre_tang.analysisFrequency()
    writeJson(fre_dict_song,"song")
    writeJson(fre_dict_tang,"tang")