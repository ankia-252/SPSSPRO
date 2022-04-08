from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import json
from data.PythonAPI.setting import save_frequecncyDocument_path,save_EncodeDocument_path,frequecncyDocument,oneHotEncode,Tag,suffix,oneHotEncode_I
import data.PythonAPI.data_Config

def encode_And_wordFrequency(tag,*poet_lists):
    """Encode and frequency analysis

    :param tag: Identify the dynasties
    :param poet_lists: Poets of every dynasties
    :return: Null
    """
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
    integer_encoded = integer_encoded.reshape(-1, 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    print(onehot_encoded)
    print("oneHot 编码完成")
    # 保存编码
    save_onehot = {}
    save_onehot_asInteger = {}
    j = 0
    for i in onehot_encoded:
        save_onehot[wordDomain[j][0]] = ','.join(str(t) for t in i)
        save_onehot_asInteger[wordDomain[j][0]] = str(integer_encoded[j][0])
        j += 1
    print("编码键值对转化完成")
    with open(save_EncodeDocument_path+oneHotEncode,'w',encoding='UTF-8') as f:
        f.write(json.dumps(save_onehot,indent=2,ensure_ascii=False))
        f.close()
    print("oneHot 编码文件已经保存")
    with open(save_EncodeDocument_path+oneHotEncode_I,'w',encoding='UTF-8') as f:
        f.write(json.dumps(save_onehot_asInteger,indent=2,ensure_ascii=False))
        f.close()
    print("oneHot 整数文件已经保存")
    print("所有数据已经保存")



if __name__ == "__main__":
    encode_And_wordFrequency(["song","tang"],data_Config.readJsons_poet("song"),data_Config.readJsons_poet("tang"))