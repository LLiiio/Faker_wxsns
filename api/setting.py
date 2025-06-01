from flask import Blueprint, Flask, request, session, redirect, url_for, render_template
import json
import os
import random
import string
from PIL import Image
from datetime import datetime
# 导入自定义模块
from Utils.utils import *
from Utils.check_mail import *
# 导入mySQL_config
from sql.setting import User_HeadImgTB
# 创建类的实例
setting = Blueprint('setting',__name__)


# 上传头像
# @param：{string}     user         用户名
# @param：{string}     image          图片
# @returns：{json}
@setting.route('/send_headimg', methods=['POST'])
def send_headimg():
    if request.method == 'POST':
        user = session.get("username")
        files = request.files.getlist('image')  # 获取所有文件
        print(str(files))
        filenames = []
        if str(files) !="[<FileStorage: '' ('application/octet-stream')>]":
            for file in files:
                ranstr = f'{user}'+'.jpg'
                filename = os.path.join(os.getcwd(), 'static/uploaded_images',ranstr)  # 拼接文件绝对路径
                image = Image.open(file)
                resized_image = image.resize((50, 50))
                resized_image.save(filename)
                filenames.append(ranstr)
        headimg = ','.join(filenames)
        if headimg:
            send = User_HeadImgTB(user, headimg)
            send.updata_headimg()
            content = json.dumps(formatres(False, {}, "上传成功"), ensure_ascii=False)
    else:
        content = json.dumps(formatres(False, {}, "101"))

    resp = Response_headers(content)
    return resp