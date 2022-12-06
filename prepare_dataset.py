import jieba
import os

basedir = "THUCNews/"
dir_list = ['affairs', 'constellation', 'economic', 'edu', 'ent', 'fashion', 'game', 'home', 'house', 'lottery',
            'science', 'sports', 'society', 'stock']
##生成fastext的訓練和測試集

ftrain = open("news_fasttext_train.txt", "w", encoding="utf-8")
ftest = open("news_fasttext_test.txt", "w", encoding="utf-8")

num = -1
for e in dir_list:
    num += 1
    indir = basedir + e + '/'
    files = os.listdir(indir)
    count = 0
    for fileName in files:
        count += 1
        filepath = indir + fileName
        with open(filepath, 'r', encoding="utf-8") as fr:
            text = fr.read().encode("utf-8")
        text = str(text, 'utf-8')
        seg_text = jieba.cut(text.replace("\t", " ").replace("\n", " "))
        outline = " ".join(seg_text)
        outline = outline + "\t__label__" + e + "\n"
        #         print outline
        #         break

        if count < 10000:
            ftrain.write(outline)
            ftrain.flush()
            continue
        elif count < 20000:
            ftest.write(outline)
            ftest.flush()
            continue
        else:
            break

ftrain.close()
ftest.close()
print('完成輸出！')
