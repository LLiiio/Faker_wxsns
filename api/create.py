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
from sql.create import User_CreateTB
# 创建类的实例
create = Blueprint('create',__name__)


# 上传图文
# @param：{string}     user         用户名
# @param：{string}     content      内容
# @param：{string}     pic          图片
# @returns：{json}
@create.route('/send_content', methods=['POST'])
def send_content():
    if request.method == 'POST':
        user = session.get("username")
        files = request.files.getlist('image')  # 获取所有文件
        print(str(files))
        filenames = []
        if str(files) !="[<FileStorage: '' ('application/octet-stream')>]":
            for file in files:
                ranstr = ''.join(random.sample(string.ascii_letters + string.digits, 6))+'.jpg'
                filename = os.path.join(os.getcwd(), 'static/uploaded_images',ranstr)  # 拼接文件绝对路径
                image = Image.open(file)
                # Resize the image to 200x200
                resized_image = image.resize((200, 200))
                # Save the resized image to a new file
                resized_image.save(filename)
                filenames.append(ranstr)
        pic = ','.join(filenames)
        param = request.form.to_dict()
        content = param.get("content")
        if content:
            send = User_CreateTB(user, content, pic)
            send = send.insetinto()
            if send == ():
                content = json.dumps(formatres(False, {}, "上传失败"), ensure_ascii=False)
            else:
                content = json.dumps(formatres(False, {}, "上传成功"), ensure_ascii=False)
        else:
            content = json.dumps(formatres(False, {}, "内容不能为空"), ensure_ascii=False)
    else:
        content = json.dumps(formatres(False, {}, "101"))

    resp = Response_headers(content)
    return resp