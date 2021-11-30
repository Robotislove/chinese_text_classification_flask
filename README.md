# -Tensorflow-
基于Tensorflow的中文文本分类可网页展示部署，基于别人的模型https://github.com/sun830910/Text_Classification加入了网页端。

# 中文文本分类

基于tensorflow2.0中的keras进行中文的文本分类  
目前已完成：  

2020/07/18:TextCNN model  
2020/07/19:LSTM model
2020/07/20:preprocess代码优化

2021/10/1：加入网页端


## 环境

Tensorflow.keras  

Python3  



## 数据集

使用THUCNews进行训练与测试（由于数据集太大，无法上传到Github，可自行下载）  
百度网盘:链接: https://pan.baidu.com/s/1nD9ej_waIPpk_GITTbgXGA  密码: 3swf  

数据集划分如下：  
训练集cnews.train.txt 50000条  
验证集cnews.val.txt 5000条  
测试集cnews.test.txt 10000条  
共分为10个类别："体育","财经","房产","家居","教育","科技","时尚","时政","游戏","娱乐"。
cnews.vocab.txt为词汇表，字符级，大小为5000。



## 文件说明

将数据集中的四份数据存放至data资料夹中  

src中的文件为代码存放资料夹：

preprocess.py:加载数据与预处理相关函数。

model.py:模型结构主体。

config.py:配置文件，包含路径配置与各模型的相关参数。

main.py:主函数文件

## 运行方式

使用Pycharm打开项目文件夹，运行main1.py为测试，然后会提示打开网页端：http://127.0.0.1:5000/。

或者是运行main.py训练自己的模型，保存训练后的结果。

在文本框中输入新闻内容，然后会弹出输出结果。

运行结果：

![Alt text](.\img\11.png)

