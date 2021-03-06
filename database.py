import pymysql

def get_connection():
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           password='1234', db='msg'
                           , charset='utf8')

    return conn


def get_thumbnail_high_views():
    conn = get_connection()
    sql = '''select * from thumbnail_tb order by views desc limit 6'''
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result


def get_hashtag(thumbnail_id):
    conn = get_connection()
    sql = '''select name from hash_tb where hash_id in (select hash_id from thumbnail_hash where thumbnail_id = %s)'''
    cursor = conn.cursor()
    cursor.execute(sql, thumbnail_id)
    result = cursor.fetchall()
    conn.close()
    return result


def get_vod_cover(arg):
    conn = get_connection()
    sql = '''select * from vod_tb where vod_title like %s'''
    cursor = conn.cursor()
    cursor.execute(sql, (f'%{arg}%'))
    result = cursor.fetchall()
    conn.close()
    return result


def get_vod(arg):
    conn = get_connection()
    sql = '''select * from vod_tb where vod_id = %s'''
    cursor = conn.cursor()
    cursor.execute(sql, arg)
    result = cursor.fetchall()
    conn.close()
    return result


def get_thumbnail_with_vodid(arg):
    conn = get_connection()
    sql = '''select * from thumbnail_tb where vod_id = %s'''
    cursor = conn.cursor()
    cursor.execute(sql, arg)
    result = cursor.fetchall()
    conn.close()
    return result


def get_thumbnail_from_hashtag(arg):
    conn = get_connection()
    sql = '''select * from thumbnail_tb where thumbnail_id in (select thumbnail_id from thumbnail_hash where hash_id in (select hash_id from hash_tb where name like %s))'''
    cursor = conn.cursor()
    cursor.execute(sql, (f'%{arg}%'))
    result = cursor.fetchall()
    conn.close()
    return result