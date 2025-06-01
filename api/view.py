from flask import Blueprint, Flask, request, session, redirect, url_for, render_template
import json
import os
import random
import string
from datetime import datetime
# 导入自定义模块
from Utils.utils import *
from Utils.check_mail import *
# 导入mySQL_config
from Utils.view import setdata1
from sql.view import User_CommentTB

# 创建类的实例
view = Blueprint('view',__name__, static_folder='../static', template_folder='../template')

@view.route('/')
def index():
    page_num = int(request.args.get('page_num', 1))  # 获取页面参数，如果没有默认为第一页
    parsed_data_list = setdata1(page_num)
    return render_template('web1.7.html', data=parsed_data_list, page_num=page_num)

@view.route('/like')
def like():
    param = request.args.to_dict()
    ID = param.get("ID")
    user = session.get("username")
    if user:
        insert = User_CommentTB(user,ID,'')
        insert.insertlike()
        return index()
    else:
        return render_template('index.html')

@view.route('/comment')
def comment():
    param = request.args.to_dict()
    ID = param.get("ID")
    user = session.get("username")
    comment = param.get("comment")
    if user:
        insert = User_CommentTB(user,ID,comment)
        insert.insertlike()
    else:
        content = json.dumps(formatres(False, {}, "请先登录"), ensure_ascii=False)
    return content