import pymysql.cursors


con = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    port = 3306,
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
