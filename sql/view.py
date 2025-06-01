import os,re
import sys

now_dir = os.getcwd()
# 获取项目根目录
project_root = os.path.abspath(os.path.join(now_dir, ".."))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)

from mySQL_config import func


class User_CommentTB:
    ''' 评论 '''
    def __init__(self,user,ID,content):
        self.user = user
        self.ID = ID
        self.content =content
    def selectAllArticles(self):
        sql = "SELECT * FROM article ORDER BY ADDTIME DESC"
        result = func(sql)
        return result

    def selectAllComment(self):
        sql = f"SELECT CONTENT, FROMUSERNAME FROM comment WHERE ID = '%s'" % (self.ID)
        result = func(sql)
        return result

    def insertlike(self):
        sql = "INSERT INTO comment (FROMUSERNAME,ID,CONTENT) VALUES ('%s','%s','%s')"%(self.user,self.ID,self.content)
        result = func(sql)
        return result