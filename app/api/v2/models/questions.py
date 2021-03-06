"""
A model class for question related operations
"""

from datetime import datetime

#Local imports
from app.api.v2.db_config import conn


# cursor to perform database operations
cur = conn.cursor()

class Question:
    """ Questions constructor """
    def __init__(self, username, meetup_id, votes, title, body ):
        self.username = username
        self.meetup_id = meetup_id
        self.votes = 0
        self.title = title
        self.body = body
        self.time_added = str(datetime.now())

    """ Method for inserting a question to db """
    def add_question(self):
        question = """ INSERT INTO questions (username, meetup_id, votes, title, body, time_added) 
        VALUES ('{}','{}','{}','{}','{}', '{}') """\
        .format(self.username, self.meetup_id, self.votes, self.title, self.body, self.time_added)
        cur.execute(question)
        conn.commit()

    def question_data(self):
        return dict(username =self.username, 
                    meetup_id = self.meetup_id,
                    votes = self.votes,
                    title = self.title,
                    body = self.body,
                    time_added = self.time_added)
