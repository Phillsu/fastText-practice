import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import fasttext
#訓練模型
classifier = fasttext.train_supervised("news_fasttext_train.txt",label_prefix="__label__")

#load訓練好的模型
#classifier = fasttext.load_model('news_fasttext.model.bin', label_prefix='__label__')
print('訓練完成！')