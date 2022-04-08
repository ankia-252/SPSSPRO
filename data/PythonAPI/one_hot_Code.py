from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
import json
from setting import save_frequecncyDocument_path,save_EncodeDocument_path,frequecncyDocument,oneHotEncode,Tag,suffix
import data_Config
from numpy import array

def words2Set(tag,*poet_lists):
    wordDomain = {}
    i = 0
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
                        wordDomain[word] = wordDomain.get(word,0) + 1
        # 文件记录
        save_dict = dict(sorted(frequency.items(),key=lambda x:x[1],reverse=True))
        with open(save_frequecncyDocument_path+frequecncyDocument+Tag[tag[i]]+suffix,'w',encoding='UTF-8') as f:
            f.write(json.dumps(save_dict,indent=2,ensure_ascii=False))
            f.close()
            print(Tag[tag[i]]+" 词频率统计完成")
        i += 1
    # 编码
    wordDomain = sorted(wordDomain.items(),key=lambda x:x[1],reverse=True)
    wordDomain_encode = [i[0].encode(encoding = "utf-8") for i in wordDomain]
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(wordDomain_encode)
    print(integer_encoded)
    print("整数编码完成")
    onehot_encoder = OneHotEncoder(sparse=False)
    wordDomain_encode = array(wordDomain_encode).reshape(-1,1)
    #integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(wordDomain_encode)
    print("oneHot 编码完成")
    # 保存编码
    save_onehot = {}
    j = 0
    for i in onehot_encoded:
        save_onehot[wordDomain[j][0]] = ','.join(str(t) for t in i)
        j += 1
    with open(save_EncodeDocument_path+oneHotEncode,'w',encoding='UTF-8') as f:
        f.write(json.dumps(save_onehot,indent=2,ensure_ascii=False))
        f.close()
    print("所有数据已经保存")



if __name__ == "__main__":
    words2Set(["song","tang"],data_Config.readJsons_poet("song"),data_Config.readJsons_poet("tang"))