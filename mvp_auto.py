# import pptx
import sys
import argparse
from jinja2 import Template, Environment, FileSystemLoader
import json

# 初期設定する 
month = "2021年12月度"
number = 8 # MVP件数
pioneer = 3
professional = 4
teamPlayer = 1

category = ""

f = open('速報.html', 'w')
nav_str = "<div class=\"radioBox\">\n"

for i in range(number):
    if i<pioneer:
        category = "Pioneer部門"
    elif i<(pioneer+professional):
        category="Professional部門"
    else:
        category="TeamPlayer部門"
    nav_str += f"<input type=\"radio\" name=\"slider\" title=\"slide{i+1}\" id=\"slide{i+1}\" onclick=\"slideLeft('{-i*100}%')\">\n<label for=\"slide{i+1}\" class=\"radio slide{i+1}\"><span class=\"abbreviation\">{category}</span></label>\n\n"
nav_str += "</div>\n"




slider_inner = "<div class=\"slider__inner\">\n"

title = "タイトル"
name = "〇〇さん、〇〇さん、〇〇さん"
text = "理由は。。"
for i in range(number):
    if i<pioneer:
        slider_inner += f"<div class=\"slider__contents\">\n<h4 class=\"department\">Pionner部門 {month}MVP</h4>\n<div class=\"slider__caption\">{title}</div>\n<div id=\"winner_list\">\n<p class=\"content_title\"><b><i class=\"fa fa-user\" aria-hidden=\"true\"></i>&nbsp;受賞者</b></p>\n<p class=\"name\">\n{name}</p>\n</div>\n<br>\n<div class=\"value\">\n<p class=\"content_title\"><b><i class=\"fa fa-star\" aria-hidden=\"true\"></i>&nbsp;該当バリュー</b></p>\n<span class=\"applicableBtn\">挑戦</span><span class=\"applicableBtn\">期待超え</span><span class=\"applicableBtn\">変化を楽しむ</span>\n</div>\n<br>\n<p class=\"content_title\"><b><i class=\"fa fa-trophy\" aria-hidden=\"true\"></i>&nbsp;受賞理由</b></p>\n<p class=\"slider__txt\">{text}</p>\n</div>\n\n"
    elif i<(pioneer+professional):
        slider_inner += f"<div class=\"slider__contents\">\n<h4 class=\"department\">Pionner部門 {month}MVP</h4>\n<div class=\"slider__caption\">{title}</div>\n<div id=\"winner_list\">\n<p class=\"content_title\"><b><i class=\"fa fa-user\" aria-hidden=\"true\"></i>&nbsp;受賞者</b></p>\n<p class=\"name\">\n{name}</p>\n</div>\n<br>\n<div class=\"value\">\n<p class=\"content_title\"><b><i class=\"fa fa-star\" aria-hidden=\"true\"></i>&nbsp;該当バリュー</b></p>\n<span class=\"applicableBtn\">スピード</span><span class=\"applicableBtn\">創意工夫</span><span class=\"applicableBtn\">数字で語る</span><span class=\"applicableBtn\">自由と責任</span>\n</div>\n<br>\n<p class=\"content_title\"><b><i class=\"fa fa-trophy\" aria-hidden=\"true\"></i>&nbsp;受賞理由</b></p>\n<p class=\"slider__txt\">{text}</p>\n</div>\n\n"
    else:
        slider_inner += f"<div class=\"slider__contents\">\n<h4 class=\"department\">Pionner部門 {month}MVP</h4>\n<div class=\"slider__caption\">{title}</div>\n<div id=\"winner_list\">\n<p class=\"content_title\"><b><i class=\"fa fa-user\" aria-hidden=\"true\"></i>&nbsp;受賞者</b></p>\n<p class=\"name\">\n{name}</p>\n</div>\n<br>\n<div class=\"value\">\n<p class=\"content_title\"><b><i class=\"fa fa-star\" aria-hidden=\"true\"></i>&nbsp;該当バリュー</b></p>\n<span class=\"applicableBtn\">自分事</span><span class=\"applicableBtn\">本音の議論</span><span class=\"applicableBtn\">引っ張る</span><span class=\"applicableBtn\">協調</span>\n</div>\n<br>\n<p class=\"content_title\"><b><i class=\"fa fa-trophy\" aria-hidden=\"true\"></i>&nbsp;受賞理由</b></p>\n<p class=\"slider__txt\">{text}</p>\n</div>\n\n"
slider_inner += "</div>\n"
main = nav_str+slider_inner
width = number*100
                
data = {'main': main, 'width': width}

env = Environment(loader=FileSystemLoader('.', encoding='utf8'))
template = env.get_template('temp.html')

disp_text = template.render(data)         
            
f.write(disp_text)    

f.close()