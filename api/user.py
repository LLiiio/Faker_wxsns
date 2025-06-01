from flask import Blueprint,Flask,request,session
import json
# 导入自定义模块
from Utils.utils import *
from Utils.check_mail import *
# 导入mySQL_config
from sql.user import UserTB
# 创建类的实例
user = Blueprint('user',__name__)

 
# 登录
# @param：{string}     user         用户名
# @param：{string}     pwd          密码
# @returns：{json}
@user.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # POST、GET:
        # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.form.to_dict().get("xxx","")获得
        param = request.form.to_dict()
        if (param.get("user") != None or param.get("mail") != None) and param.get("pwd") != None:
            if (param.get("user") != "" or param.get("mail")!= "") and param.get("pwd") != "" and len(param.get("pwd")) < 20:
                user = UserTB(param.get("user"),param.get("pwd"),param.get("mail"),param.get("code"))
                user = user.selectUser()
                if user == ():
                    mail = param.get("user")
                    checkmail = UserTB(param.get("user"),param.get("pwd"),mail,param.get("code"))
                    checkmail = checkmail.selectUserMail()
                    if checkmail == ():
                        content = json.dumps(formatres(False, {}, "该邮箱未注册"), ensure_ascii=False)
                    else:
                        userPwd = UserTB(param.get("user"),param.get("pwd"),mail,param.get("code"))
                        userPwd = userPwd.selectMailPwd()
                        if userPwd == ():
                            content = json.dumps(formatres(False, {}, "用户名密码不正确"), ensure_ascii=False)
                        else:
                            username = checkmail[0][0]
                            session["username"] = username
                            content = json.dumps(formatres(True, {}, "登录成功"), ensure_ascii=False)
                else:
                    userPwd = UserTB(param.get("user"),param.get("pwd"),param.get("mail"),param.get("code"))
                    userPwd = userPwd.selectUserPwd()
                    if userPwd == ():
                        content = json.dumps(formatres(False,{},"用户名密码不正确"),ensure_ascii=False)
                    else:
                        session["username"] = param.get("user")
                        content = json.dumps(formatres(True,{},"登录成功"),ensure_ascii=False)
            else:
                content = json.dumps(formatres(False,{},"用户名密码为空或者过长"),ensure_ascii=False)
        else:
             content = json.dumps(formatres(False,{},"请检查参数"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    resp = Response_headers(content)
    return resp

# 注册
# @param：{string}     user         用户名
# @param：{string}     pwd          密码
# @returns：{json}
@user.route('/reg',methods=['post'])
def reg():
    if request.method == 'POST':
        param = request.form.to_dict()
        if param.get("user") != None and param.get("pwd") != None and param.get("mail") != None:
            if IsValidEmail(param.get("mail")):
                if param.get("user") != "" and len(param.get("user")) < 8 and param.get("pwd") != "" and len(param.get("pwd")) < 20:
                    user = UserTB(param.get("user"),param.get("pwd"),param.get("mail"),param.get("code"))
                    user = user.selectUser()
                    if user != ():
                        content = json.dumps(formatres(False,{},"用户名已存在"),ensure_ascii=False)
                    else:
                        mail = UserTB(param.get("user"),param.get("pwd"),param.get("mail"),param.get("code"))
                        mail = mail.selectUserMail()
                        if mail != ():
                            content = json.dumps(formatres(False, {}, "该邮箱已注册"), ensure_ascii=False)
                        else:
                            code = gen_email_code()
                            send_email(param.get("mail"), code)
                            insert_code = UserTB(param.get("user"),code,param.get("mail"),code)
                            insert_code.insetinto_code()
                            content = json.dumps(formatres(True, {}, "邮箱验证码已发送"), ensure_ascii=False)
                else:
                    content = json.dumps(formatres(False,{},"用户名密码为空或者过长"),ensure_ascii=False)
            else:
                content = json.dumps(formatres(False, {}, "邮箱格式错误"), ensure_ascii=False)
        else:
             content = json.dumps(formatres(False,{},"请检查参数"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    resp = Response_headers(content)
    return resp

# 邮箱验证
# @param：{string}     mail         邮箱
# @param：{string}     code         邮箱验证码
# @returns：{json}
@user.route('/mail_check',methods=['post'])
def mail_check():
    if request.method == 'POST':
        param = request.form.to_dict()
        if param.get("code") != None and param.get("mail") != None:
            check = UserTB(param.get("user"),param.get("pwd"),param.get("mail"),param.get("code"))
            check = check.selectMailCode()
            if check == ():
                content = json.dumps(formatres(False, {}, "邮箱验证码不正确"), ensure_ascii=False)
            else:
                insetintouser = UserTB(param.get("user"),param.get("pwd"), param.get("mail"),param.get("code"))
                insetintouser.update_pwd()
                content = json.dumps(formatres(True, {}, "注册成功"), ensure_ascii=False)
        else:
            content = json.dumps(formatres(False, {}, "请检查参数"), ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    resp = Response_headers(content)
    return resp

# 发送邮箱验证码
# @param：{string}     mail         邮箱
# @param：{string}     code         邮箱验证码
# @returns：{json}
@user.route('/send_mailcode', methods=['POST'])
def send_mailcode():
    if request.method == 'POST':
        param = request.form.to_dict()
        mail = param.get("mail")
        if mail != None:
            if IsValidEmail(mail):
                mail_exist = UserTB(None,None,mail,None)
                mail_exist = mail_exist.selectUserMail()
                if mail_exist == () :
                    content = json.dumps(formatres(False, {}, "邮箱尚未注册"), ensure_ascii=False)
                else:
                    code = gen_email_code()
                    send_email(mail, code)
                    update = UserTB(None,None,mail,code)
                    update.update_code()
                    content = json.dumps(formatres(True, {}, "邮箱验证码已发送"), ensure_ascii=False)
            else:
                content = json.dumps(formatres(False, {}, "邮箱格式错误"), ensure_ascii=False)
        else:
            content = json.dumps(formatres(False, {}, "请检查参数"), ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    resp = Response_headers(content)
    return resp

# 修改密码
# @param：{string}     mail         邮箱
# @param：{string}     code         邮箱验证码
# @param：{string}     new_pwd      新密码
# @returns：{json}
@user.route('/update_password', methods=['POST'])
def update_password():
    if request.method == 'POST':
        param = request.form.to_dict()
        mail = param.get("mail")
        code = param.get("code")
        new_pwd = param.get("new_pwd")

        if mail and code and new_pwd:
            if len(new_pwd) < 20:
                # 检查验证码是否正确
                check = UserTB(None, None, mail, code)
                check = check.selectMailCode()
                if check == ():
                    content = json.dumps(formatres(False, {}, "邮箱验证码不正确"), ensure_ascii=False)
                else:
                    # 更新密码
                    update_user = UserTB(None, new_pwd, mail, None)
                    update_user.update_pwd()
                    content = json.dumps(formatres(True, {}, "密码修改成功"), ensure_ascii=False)
            else:
                content = json.dumps(formatres(False, {}, "新密码长度不能超过20个字符"), ensure_ascii=False)
        else:
            content = json.dumps(formatres(False, {}, "请检查参数"), ensure_ascii=False)
    else:
        content = json.dumps(formatres(False, {}, "101"))

    resp = Response_headers(content)
    return resp

# 登录校验
@user.route("/session", methods=["POST"])
def check_session():
    if request.method == 'POST':
        username = session.get("username")
        if username:
            content = json.dumps(formatres(True, {}, "登录成功"), ensure_ascii=False)
        else:
            content = json.dumps(formatres(False, {}, "登录失败"), ensure_ascii=False)
    else:
        content = json.dumps(formatres(False, {}, "101"))

    resp = Response_headers(content)
    return resp

# 退出登录
@user.route("/logout", methods=["DELETE"])
def logout():
    if request.method == 'DELETE':
        # 清除session数据
        session.clear()
        content = json.dumps(formatres(True, {}, "退出登录成功"), ensure_ascii=False)
    else:
        content = json.dumps(formatres(False, {}, "101"))

    resp = Response_headers(content)
    return resp

