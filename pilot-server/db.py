import pymysql
import pymssql
import postgresql
import os

# mysql
def get_db_connection():
    # 根据配置返回数据库连接
    return pymysql.connect(host=os.getenv('NET_IP'), 
                           port=int(os.getenv('MYSQL_PORT')), 
                           user=os.getenv('MYSQL_USER'), 
                           password=os.getenv('MYSQL_PASSWORD'), 
                           db=os.getenv('MYSQL_DATABASE'), 
                           charset="utf8mb4",
                           cursorclass=pymysql.cursors.DictCursor)
            
def query_db(query, args=()):
    # 执行 SELECT 查询
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, args)
        result = cursor.fetchall()
    conn.close()
    return result

def modify_db(query, args=()):
    # 执行 INSERT, UPDATE, DELETE 操作
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, args)
        conn.commit()
    conn.close()

# mssql
def get_sqli_mssql():
    return pymssql.connect(host=os.getenv('NET_IP'), 
                           port=int(os.getenv('MSSQL_PORT')), 
                           user=os.getenv('MSSQL_USER'), 
                           password=os.getenv('MSSQL_PASSWORD'), 
                           database=os.getenv('MSSQL_DATABASE'))

def query_mssql(query, args=()):
    # 执行 SELECT 查询
    conn = get_sqli_mssql()
    with conn.cursor() as cursor:
        cursor.execute(query, args)
        result = cursor.fetchall()
    conn.close()
    return result

# pgsql
def get_sqli_pgsql():
    postgresql.versionstring.split = _monkey_split
    pgsql = "pq://" + os.getenv('POSTGRES_USER') + ":" + os.getenv('POSTGRES_PASSWORD') + "@" + os.getenv('NET_IP') + ":" + os.getenv('POSTGRES_PORT') + "/" + os.getenv('POSTGRES_DB')
    return postgresql.open(pgsql)

def query_pgsql(query):
    # 执行 SELECT 查询
    conn = get_sqli_pgsql()
    result = conn.prepare(query)
    return result()

# pgsql补丁
import re
import postgresql.versionstring

_orig_split = postgresql.versionstring.split

def _monkey_split(vstr):
    m = re.match("^([0-9]+\.[0-9]+[^\s]*)\s+\(.+\)$", vstr)
    if m is not None:
        vstr = m.group(1)
    return _orig_split(vstr)
