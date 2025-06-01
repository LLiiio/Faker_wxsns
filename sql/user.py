import os,re
import sys

now_dir = os.getcwd()
# 获取项目根目录
project_root = os.path.abspath(os.path.join(now_dir, ".."))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)

from mySQL_config import func


class UserTB:
    ''' 用户增加、查询 '''
    def __init__(self,user,pwd,mail,code):
        self.user = user
        self.pwd = pwd
        self.mail = mail
        self.code =code
    
    # 查询用户名
    def selectUser(self):
        sql = "select * from user where USERNAME = '%s'"%self.user
        result = func(sql)
        return result
    
    # 查询用户名密码
    def selectUserPwd(self):
        sql = "select * from user where USERNAME = '%s' and PASSWORD = '%s' limit 1"%(self.user,self.pwd)
        result = func(sql)
        return result
    # 插入
    def insetinto(self):
        sql = "INSERT INTO user (USERNAME,PASSWORD,MAIL) VALUES ('%s','%s','%s')"%(self.user,self.pwd,self.mail)
        result = func(sql)
        return result

    # 查询用户名邮箱
    def selectUserMail(self):
        sql = "select * from user where MAIL = '%s'" % self.mail
        result = func(sql)
        return result

    # 查询邮箱密码
    def selectMailPwd(self):
        sql = "select * from user where MAIL = '%s' and PASSWORD = '%s' limit 1" % (self.mail, self.pwd)
        result = func(sql)
        return result

    # 创建code
    def insetinto_code(self):
        sql = "INSERT INTO user (USERNAME,PASSWORD,MAIL,CODE) VALUES ('%s','%s','%s','%s')" % (self.user,self.pwd,self.mail,self.code)
        result = func(sql)
        return result

    # 查询邮箱验证码
    def selectMailCode(self):
        sql = "select * from user where MAIL = '%s' and CODE = '%s' limit 1" % (self.mail, self.code)
        result = func(sql)
        return result

    # 修改密码
    def update_pwd(self):
        sql = "UPDATE user SET PASSWORD = '%s' WHERE MAIL = '%s'" % (self.pwd, self.mail)
        result = func(sql)
        return result

    # 修改code
    def update_code(self):
        sql = "UPDATE user SET CODE = '%s' WHERE MAIL = '%s'" % (self.code, self.mail)
        result = func(sql)
        return result