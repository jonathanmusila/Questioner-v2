from datetime import datetime


#Local imports
from app.api.v2.db_config import conn

cur = conn.cursor()

class Comment:
    """ Comments constructor """
    def __init__(self, user_id, question_id, comment):
        self.user_id = user_id
        self.question_id = question_id
        self.comment = comment
        self.time_added = str(datetime.now())

    """ Method creating a comment """
    def add_comment(self):
        commen = """ INSERT INTO comments (user_id, question_id, comment, time_added) 
        VALUES ('{}','{}','{}','{}') """\
        .format(self.user_id, self.question_id, self.comment, self.time_added)
        cur.execute(commen)
        conn.commit()

    def comment_data(self):
        return dict(user_id =self.user_id, 
                    question_id = self.question_id,
                    comment = self.comment,
                    time_added = self.time_added)
                    