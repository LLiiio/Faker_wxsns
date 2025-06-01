from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
import random
import string
import re


def send_email(receiver, ecode):
    """发送邮件"""
    sender = '319046270@qq.com'  # 邮箱账号和发件者签名

    # 定义发送邮件的内容，支持HTML和CSS样式
    content = f"您的邮箱验证码为：<span style='color: red; font-size: 20px;'>{ecode}</span>"
    message = MIMEText(content, 'html', 'utf-8')  # 实例化邮件对象，并指定邮件的关键信息
    # 指定邮件的标题，同样使用utf-8编码
    message['Subject'] = Header('验证码', 'utf-8')
    message['From'] = sender
    message['To'] = receiver

    smtpObj = SMTP_SSL("smtp.qq.com", 465)  # QQ邮件服务器的链接
    smtpObj.login(user='319046270@qq.com', password='vxrztvrptxdacabj')  # 通过自己的邮箱账号和获取到的授权码登录QQ邮箱

    # 指定发件人、收件人和邮件内容
    smtpObj.sendmail(sender, receiver, str(message))
    smtpObj.quit()


def gen_email_code():
    str = random.sample(string.ascii_letters + string.digits, 6)
    return ''.join(str)

# 校验某个字符串是否是合格的email地址
def IsValidEmail(email):
    REGEX_PATTERN = "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$"
    if (re.search(REGEX_PATTERN, email)):
        return 1
    else:
        return 0