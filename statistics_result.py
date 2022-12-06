from train_fastText import classifier

labels_right = []
texts = []
with open("news_fasttext_train.txt", encoding="utf-8") as fr:
    for line in fr:
        line = str(line.encode("utf-8"), 'utf-8').rstrip()
        labels_right.append(line.split("\t")[1].replace("__label__", ""))
        texts.append(line.split("\t")[0])
    #     print labels
    #     print texts
#     break
labels_predict = [term[0] for term in classifier.predict(texts)[0]]  # 預測輸出結果為二維形式
# print labels_predict

text_labels = list(set(labels_right))
text_predict_labels = list(set(labels_predict))
print(text_predict_labels)
print(text_labels)
print()

A = dict.fromkeys(text_labels, 0)  # 預測正確的各類別的數量
B = dict.fromkeys(text_labels, 0)  # 測試數據集中各個類別的數量
C = dict.fromkeys(text_predict_labels, 0)  # 預測結果中各類別的數量
for i in range(0, len(labels_right)):
    B[labels_right[i]] += 1
    C[labels_predict[i]] += 1
    if labels_right[i] == labels_predict[i].replace('__label__', ''):
        A[labels_right[i]] += 1

print('預測正確的各個類別數量:', A)
print()
print('測試數據集中各個類別的數量:', B)
print()
print('預測結果中各個類的數量:', C)
print()
# 計算P、R以及F-score
for key in B:
    try:
        r = float(A[Key]) / float(B[key])
        p = float(A[key]) / float(C['__label__' + key])
        f = p * r * 2 / (p + r)
        print(r)
    except:
        print("error:", key, "right:", A.get(key, 0), "real:", B.get(key, 0), "predict:", C.get(key, 0))
