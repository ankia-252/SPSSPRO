from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
"paragraphs"

def words2Set(*poet_lists,**category):
    wordDomain = []
    for poet_list in poet_lists:
        # 分开进行字频统计
        frequency = {}
        for poet in poet_list:
            # 统计字频以及进行编码
            for words in poet["paragraphs"]:
                # 每个字进行去重统计
                for word in words:
                    if word != '，' and word != '。' and word != '！':
                        frequency[word] = frequency.get(word,0) + 1
        # 文件记录
