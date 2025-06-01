import os,re
import sys

now_dir = os.getcwd()
# 获取项目根目录
project_root = os.path.abspath(os.path.join(now_dir, ".."))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)

from mySQL_config import func


class User_HeadImgTB:
    ''' 更换头像 '''

    def __init__(self, user, headimg):
        self.user = user
        self.headimg = headimg

    # 更换头像
    def updata_headimg(self):
        sql = "UPDATE user SET HEADIMG = '%s' WHERE USERNAME = '%s'" % (self.headimg, self.user)
        result = func(sql)
        return result
