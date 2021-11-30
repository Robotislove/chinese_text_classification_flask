from flask import Flask
from flask import render_template
from flask import request
from predicter import TfidfPredicter,Word2vecPredictor


#模型路径


app = Flask(__name__)

@app.route('/')
def newsclass():
    """
    显示文章预测页面
    :return:
    """
    return  render_template('newsclass.html')

@app.route('/predict',methods=["GET", "POST"])
def predict():
    """
    接受前端传递来的文章内容和预测方式,并用对应的预测方式对文章类型进行预测
    :return:
    """

    tfidf_predicter = TfidfPredicter()  # 加载tfidf模型
    word2vec_predicter = Word2vecPredictor()  # 加载word2vec模型
    #接受前端传过来的新闻内容
    if request.method == "POST":
        news = request.form.get("news")
        model_type=request.form.get("type")
    else:
        news = request.args.get("news")
        model_type = request.args.get("type")

    #判断用户选择的预测方式并采用对应的方式进行预测
    if model_type=='tfidf':
        labels=tfidf_predicter.predict([news])
    else:
        labels=word2vec_predicter.predict([news])

    return labels#由于每次只传递了一个新闻


if __name__  ==  '__main__':
    app.run(host='127.0.0.1',  debug=True)