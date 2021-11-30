$(document).ready(function(){

 $("#predict").click(function(){
    txt=$("#news_content").val(); //获取新闻内容
    typ=$("#type").val();//获取预测方式
    $.post("/predict",{news:txt,type:typ},function(result){//调用后端的接口  传递
        $("#newsclass").html(result);
    });
  });
});