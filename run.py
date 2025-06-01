#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入flask模块
from flask import Blueprint, Flask, request, session, redirect, url_for, render_template,send_from_directory
from flask_socketio import SocketIO, join_room, leave_room, send
from os import urandom
import json
# 导入自定义模块
from Utils.utils import *
# 导入user
from api.user import user
from api.create import create
from api.view import view
from api.setting import setting
from Utils.view import *

# 获取当前文件所在目录的绝对路径
current_directory = os.path.dirname(os.path.abspath(__file__))
# 用相对路径补充到当前目录，获取模板文件夹的绝对路径
template_folder = os.path.join(current_directory, 'templates')
static_folder = os.path.join(current_directory, 'static')
# 在 Flask 中使用绝对路径作为模板文件夹的路径
app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)
app.secret_key = urandom(50)
socketio = SocketIO(app)

# 导入接口
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(create, url_prefix='/create')
app.register_blueprint(view, url_prefix='/view')
app.register_blueprint(setting, url_prefix='/setting')

# 定义首页路由
@app.route('/')
def goto_index():
    return render_template('index.html')

# 重定向错误400
@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"400"))
    resp = Response_headers(content)
    return resp

# 重定向错误403
@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"403"))
    resp = Response_headers(content)
    return resp

# 重定向错误404
@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"404"))
    resp = Response_headers(content)
    return resp

# 重定向错误405
@app.errorhandler(405)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"405"))
    resp = Response_headers(content)
    return resp

# 重定向错误410
@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"410"))
    resp = Response_headers(content)
    return resp

# 重定向错误500
@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"500"))
    resp = Response_headers(content)
    return resp

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('index'))

@app.route('/create')
def create():
    if 'username' in session:
        return render_template('create.html', username=session['username'])
    else:
        return redirect(url_for('index'))

@app.route('/setting')
def setting():
    if 'username' in session:
        return render_template('setting.html', username=session['username'])
    else:
        return redirect(url_for('index'))

@socketio.on('message')
def handle_message(msg):
    username = session.get('username')
    if username:
        send(f"{username}: {msg}", broadcast=True)

@socketio.on('join')
def handle_join(room):
    join_room(room)
    username = session.get('username')
    send(f"{username} has joined the room.", to=room)


if __name__ == '__main__':
    # app.run(debug=True, threaded=True, host='0.0.0.0')
    socketio.run(app, debug=True, host='0.0.0.0')