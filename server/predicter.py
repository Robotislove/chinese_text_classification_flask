
import jieba
import numpy as np
import os
import tensorflow as tf
import tensorflow.keras as keras
from model import LSTM
from model import TextCNN
from config import Config
from preprocess import preprocesser
class test1():
    def __init__(self):
        self.config = Config()
        self.pre = preprocesser()
    def test(self, articles):
        model_save_path1 = self.config.get("result", "CNN_model_path")
        seq_length = self.config.get("CNN_training_rule", "seq_length")
        categories = ["体育", "财经", "房产", "家居", "教育", "科技", "时尚", "时政", "游戏", "娱乐"]
        if os.path.exists(model_save_path1):
            model = keras.models.load_model(model_save_path1)
            # model.summary()
        articles1= "".join(articles)
        print(type(articles))
        x_test = self.pre.word2idx_for_sample(articles1, max_length=seq_length)
        print(x_test)
        # print(x_test.shape)
        # print(type(x_test))
        # print(y_test.shape)
        # print(type(y_test))
        pre_test = model.predict(x_test)
        # print(pre_test.shape)
        # metrics.classification_report(np.argmax(pre_test, axis=1), np.argmax(y_test, axis=1), digits=4, output_dict=True)
        print(categories[np.argmax(pre_test)])
        return (categories[np.argmax(pre_test)])


class test2():
    def __init__(self):
        self.config = Config()
        self.pre = preprocesser()
    def test(self, articles):
        model_save_path2 = self.config.get("result", "LSTM_model_path")
        seq_length = self.config.get("LSTM", "seq_length")
        categories = ["体育", "财经", "房产", "家居", "教育", "科技", "时尚", "时政", "游戏", "娱乐"]
        if os.path.exists(model_save_path2):
            model = keras.models.load_model(model_save_path2)
            # model.summary()
        articles1 = "".join(articles)
        x_test = self.pre.word2idx_for_sample(articles1, max_length=seq_length)
        print(x_test)
        # print(x_test.shape)
        # print(type(x_test))
        # print(y_test.shape)
        # print(type(y_test))
        pre_test = model.predict(x_test)
        # print(pre_test.shape)
        # metrics.classification_report(np.argmax(pre_test, axis=1), np.argmax(y_test, axis=1), digits=4, output_dict=True)
        print(categories[np.argmax(pre_test)])
        return (categories[np.argmax(pre_test)])
class TfidfPredicter():
    def __init__(self):
        """
        实例化并加载模型
        :param model_file: 模型路径
        """
        self.test0 =test1()
    def predict(self, articles):
        """
        实现文章预测
        :param articles: 文章列表
        :return: 文章预测的结果列表
        """
        y_label = self.test0.test(articles)
        return  y_label
        #将y的结果转换为字符串形式

# class Word2vecPredictor(object):
#     def __init__(self):
#         """
#         实例化并加载模型
#         :param model_file: 模型路径
#         """
#         self.model = keras.models.load_model('LSTM_model.h5')

#或者采用jieba来进行输入的问题预处理
class Word2vecPredictor():
    def __init__(self):
        """
        实例化并加载模型
        :param model_file: 模型路径
        """
        self.test1 = test2()

    def predict(self, articles):
        """
        实现文章预测
        :param articles: 文章列表
        :return: 文章预测的结果列表
        """
        y_label = self.test1.test(articles)
        print(y_label)
        return  y_label

# if __name__ == '__main__':
#     test_2 = TfidfPredicter()
#     print(test_2)