import jieba
from data.PythonAPI.data_Config import readJsons_poet
import json
from data.PythonAPI.setting import save_frequecncyDocument_path,frequecncy_Document2,suffix

class analysisTool:
    """Frequency analysis

    """
    poets_key_eq_author = {}
    authors = []
    dynasty = ""
    def __init__(self,poets:list,type:str):
        self.dynasty = type
        for poet in poets:
            if self.poets_key_eq_author.get(poet["author"],False) != False:
                self.poets_key_eq_author[poet["author"]].append(poet)
            else:
                self.poets_key_eq_author[poet["author"]] = [poet]
                self.authors.append(poet["author"])
    def analysisFrequency(self):
        """

        :return: Dict of every authors's frequency
        """
        lexicon = {}
        for author in self.authors:
            lexiconOfAuthor = {}
            for poet in self.poets_key_eq_author[author]:
                temp_str = ""
                for i in poet["paragraphs"]:
                    if i[0] == "（":break
                    else:
                        temp_str += i
                for i in jieba.cut(temp_str,cut_all=True):
                    if i[0] == '，' or i[0] == '。' or i[0] == '[' or i == ']' or i == '）' or i == '（':continue
                    lexiconOfAuthor[i] = lexiconOfAuthor.get(i,0) + 1
            lexiconOfAuthor = dict(sorted(lexiconOfAuthor.items(),key=lambda x:x[1],reverse=True))
            lexicon[author] = lexiconOfAuthor
        return lexicon

def writeJson(d:dict,type:str):
    """Write to Json

    :param d: The dictionary that needs to be written
    :param type: The dynasty
    :return: Null
    """
    with open(save_frequecncyDocument_path + frequecncy_Document2 + type + '.' + suffix, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(d, indent=2, ensure_ascii=False))
        f.close()
        print(type+"朝诗人词频统计完成")

if __name__ == "__main__":
    poets = readJsons_poet("tang")
    temp = analysisTool(poets,"tang")
    l = temp.analysisFrequency()
    writeJson(l,"tang")



