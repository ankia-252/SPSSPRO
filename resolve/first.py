from data.PythonAPI.data_Config import readJsons_author,readJsons_poet

if __name__ == "__main__":
    authorSong = readJsons_author("song")
    authorTang = readJsons_author("tang")
    poetSong = readJsons_poet("song")
    poetTang = readJsons_poet("tang")

    #首先对唐诗整体词频进行统计