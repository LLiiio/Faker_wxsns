from sql.view import User_CommentTB
import os


def getdata(i):
    rows = User_CommentTB(None,None,None)
    rows = rows.selectAllArticles()
    # 如果 i 超过数据总数，返回 None
    if i >= len(rows):
        return None

    username = rows[i][0]
    content_desc  = rows[i][2]
    time = rows[i][4]
    ID = rows[i][1]
    images = (rows[i][3]).split(',')
    if images[0]:
        images = ['./static/uploaded_images/' + image for image in images]
    else:
        images = []
    rows = User_CommentTB(None, ID, None)
    rows = rows.selectAllComment()
    comment, FromUserName = zip(*rows) if rows else ([], [])
    # 将 comment 和 comment_username 合并为字典列表
    comment_data_list = [{'comment_username': u, 'comment': c} for u, c in zip(FromUserName, comment)]
    like_list = []
    # 处理 comment_data_list
    comment_data_list = [data for data in comment_data_list if
                         data['comment'] or like_list.append(data['comment_username'])]
    like_list = list(set(like_list))
    return content_desc, images, username, time, like_list, comment_data_list,ID

def setdata1(page_num, per_page=10):
    start_index = (page_num - 1) * per_page
    data_list = []

    for i in range(start_index, start_index + per_page):
        result = getdata(i)
        # 如果 getdata 返回 None，说明数据不足，结束循环
        if result is None:
            break
        content_desc, images, username, time, like_list, comment_data_list,ID = result
        data = {
            'content_desc': content_desc,
            'images': images,
            'usernames': username,
            # 'headimg': headimg,
            'time': time,
            'like_list': like_list,
            'comment_data_list': comment_data_list,
            'ID': ID
        }
        data_list.append(data)

    return data_list
