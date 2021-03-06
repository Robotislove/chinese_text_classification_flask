# -*- coding: utf-8 -*-

"""

"""

import tensorflow.keras as keras
import numpy as np
from sklearn import metrics
import os
from preprocess import preprocesser
from config import Config
from model import TextCNN
from model import LSTM
class test(object):
    def __init__(self):
        self.config = Config()
        self.pre = preprocesser()
    def test(self, stance, seq_length):
        model_save_path = self.config.get("result", "LSTM_model_path")
        seq_length = self.config.get("LSTM", "seq_length")
        categories = ["体育", "财经", "房产", "家居", "教育", "科技", "时尚", "时政", "游戏", "娱乐"]
        if os.path.exists(model_save_path):
            model = keras.models.load_model(model_save_path)
            print("-----model loaded-----")
            # model.summary()
        x_test = self.pre.word2idx_for_sample(stance, max_length=seq_length)
        # print(x_test.shape)
        # print(type(x_test))
        # print(y_test.shape)
        # print(type(y_test))
        pre_test = model.predict(x_test)
        # print(pre_test.shape)
        # metrics.classification_report(np.argmax(pre_test, axis=1), np.argmax(y_test, axis=1), digits=4, output_dict=True)

        return (categories[np.argmax(pre_test)])


if __name__ == '__main__':
    test = test()

    # test.test("马晓旭意外受伤让国奥警惕 无奈大雨格外青睐殷家军记者傅亚雨沈阳报道 来到沈阳，国奥队依然没有摆脱雨水的困扰。7月31日下午6点，国奥队的日常训练再度受到大雨的干扰，无奈之下队员们只慢跑了25分钟就草草收场。31日上午10点，国奥队在奥体中心外场训练的时候，天就是阴沉沉的，气象预报显示当天下午沈阳就有大雨，但幸好队伍上午的训练并没有受到任何干扰。下午6点，当球队抵达训练场时，大雨已经下了几个小时，而且丝毫没有停下来的意思。抱着试一试的态度，球队开始了当天下午的例行训练，25分钟过去了，天气没有任何转好的迹象，为了保护球员们，国奥队决定中止当天的训练，全队立即返回酒店。在雨中训练对足球队来说并不是什么稀罕事，但在奥运会即将开始之前，全队变得“娇贵”了。在沈阳最后一周的训练，国奥队首先要保证现有的球员不再出现意外的伤病情况以免影响正式比赛，因此这一阶段控制训练受伤、控制感冒等疾病的出现被队伍放在了相当重要的位置。而抵达沈阳之后，中后卫冯萧霆就一直没有训练，冯萧霆是7月27日在长春患上了感冒，因此也没有参加29日跟塞尔维亚的热身赛。队伍介绍说，冯萧霆并没有出现发烧症状，但为了安全起见，这两天还是让他静养休息，等感冒彻底好了之后再恢复训练。由于有了冯萧霆这个例子，因此国奥队对雨中训练就显得特别谨慎，主要是担心球员们受凉而引发感冒，造成非战斗减员。而女足队员马晓旭在热身赛中受伤导致无缘奥运的前科，也让在沈阳的国奥队现在格外警惕，“训练中不断嘱咐队员们要注意动作，我们可不能再出这样的事情了。”一位工作人员表示。从长春到沈阳，雨水一路伴随着国奥队，“也邪了，我们走到哪儿雨就下到哪儿，在长春几次训练都被大雨给搅和了，没想到来沈阳又碰到这种事情。”一位国奥球员也对雨水的“青睐”有些不解。", 600)
    heii = test.test("该知情人随后给记者转来宜章县人民法院的判决结果。红星新闻记者注意到，2020年12月4日23时，宜章县人民法院在其官网——宜章法院网刊发对此案件的宣判结果显示：2020年12月4日，湖南省宜章县人民法院对被告人楚挺征犯强奸罪一案进行公开宣判，以强奸罪判处被告人楚挺征有期徒刑三年。", 600)
    print(heii)


    #LSTM= LSTM()
    # CNN_model.train(3)
    #LSTM.test()
