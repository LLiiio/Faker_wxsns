import os,re
import sys

now_dir = os.getcwd()
# 获取项目根目录
project_root = os.path.abspath(os.path.join(now_dir, ".."))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)

from mySQL_config import func


class User_CreateTB:
    ''' 图文发表 '''

    def __init__(self, user, content, pic):
        self.user = user
        self.content = content
        self.pic = pic

    # 插入
    def insetinto(self):
        sql = "INSERT INTO article (USERNAME,CONTENT,PIC) VALUES ('%s','%s','%s')" % (self.user, self.content, self.pic)
        result = func(sql)
        return result
