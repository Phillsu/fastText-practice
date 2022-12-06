from train_fastText import classifier
result = classifier.test("news_fasttext_test.txt")
print('precision：', result[1])
