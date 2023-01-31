""" Make HTML page with data from database """
import logging
from flask import Flask
import MySQLdb
 
app = Flask(__name__)
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
 
@app.route("/")
def root():
    """ Root page """
 
    db_setting = {
        "host": "database",
        "user": "root",
        "passwd": "my-secret-pw",
        "db": "test_database",
        "charset": "utf8mb4"
        }
 
    data = []
    try:
        db_conn = MySQLdb.connect(**db_setting)
        try:
            cursor = db_conn.cursor()
            query = "SELECT name, english, mathematics FROM test_table"
            cursor.execute(query)
            data = cursor.fetchall()
        finally:
            db_conn.close()
    except Exception as err:
        logger.error("%s %s", type(err), err)
 
    body = "<table><tr><th>name</th><th>english</th><th>mathmatics</th></tr>{}</table>".format(
        "".join([
            "<tr><td>{}</td><td>{}</td><td>{}</td>".format(name, english, mathematics)
            for name, english, mathematics
            in data
        ])
        )
 
    page = "<html><head><title>Test Page</title></head><body>{body}</body></html>\n"
 
    return page.format(body=body)