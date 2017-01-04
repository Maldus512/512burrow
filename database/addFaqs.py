import MySQLdb
import uuid
import json
import os
from ..env.settings import mysqlpwd, mysqluser



def getUniqueId(curs):
        uid = str(uuid.uuid4())[0:15]
        query = "SELECT * FROM faqs WHERE id = %s"
        curs.execute(query, [uid])
        while curs.rowcount > 0:
            uid = str(uuid.uuid4())[0:23]
            curs.execute(query, [uid])
        return uid





if __name__ == "__main__":
    db = MySQLdb.connect("localhost", mysqluser, mysqlpwd, "512burrow")
    db.autocommit(True)
    cur = db.cursor()
    
    filename = os.path.dirname(os.path.realpath(__file__)) + "/faq.json"
    with open(filename, "r") as f:
        res = json.load(f) 

    cur.execute("""DELETE from faqs WHERE True""")
    i = 0 
    for faq in res:
        id = getUniqueId(cur)
        cur.execute("""INSERT INTO faqs(id, question, answer, pos)
                VALUES(%s, %s, %s, %s)""",
                [id, faq['question'], faq['answer'], i])
        i += 1

