import pymysql

# 要执行的 SQL 文件列表
sql_files = ['user.sql', 'article.sql', 'comment.sql']

# 连接到 MySQL 数据库
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    port=3306,
    password='123456',
    database='wxsns',
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        # 遍历每个 SQL 文件
        for sql_file in sql_files:
            # 读取 SQL 文件内容
            with open(sql_file, 'r', encoding='utf-8') as file:
                sql_commands = file.read()

            # 执行 SQL 命令
            for command in sql_commands.split(';'):
                command = command.strip()
                if command:
                    try:
                        cursor.execute(command)
                    except pymysql.MySQLError as e:
                        print(f"Error executing command in {sql_file}: {command}")
                        print(f"MySQL Error: {e}")
        connection.commit()
finally:
    connection.close()
