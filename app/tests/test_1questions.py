import json

#local imports
from .base_test import Settings

question_url = "api/v2/meetups/1/questions"
meetups_url = "api/v2/meetups/upcoming"

class TestUser(Settings):
    quiz =   {

          "title": "Python",
          "body": "This is the body of this question"
    } 
    meetup =   {
          "happeningOn": "14/4/2019",
          "images": "image.jpg",
          "tags": "me, you",
          "title": "Python",
          "location": "PAC"
    } 
    upvote =   {

          "title": "Python",
          "body": "This is the body of this question"
    }

    def test_post_question(self):
        """Test API can post a question to a meetup"""
        token = self.give_token()
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        res = self.app.post(question_url,
                            data=json.dumps(self.quiz),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['Message'], 'Question posted successfully')
        self.assertEqual(res.status_code, 201)

    def test_get_all_questions(self):
        token = self.give_token()
        res = self.app.post(question_url,
                            data=json.dumps(self.quiz),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        res1 = self.app.get('api/v2/meetups/1/questions')
        data = json.loads(res1.get_data().decode())
        self.assertEqual(res1.status_code, 200)
        self.assertIn('Python', str(res1.data))

    def test_get_single_question(self):
        """Test API can get a single question by using it's id."""
        token = self.give_token()
        res = self.app.post(question_url,
                            data=json.dumps(self.quiz),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        rv1 = self.app.get('api/v2/meetups/questions/1')
        data = json.loads(rv1.data.decode())
        self.assertEqual(rv1.status_code, 200)
        self.assertIn('This is the body of this question', str(rv1.data))

    def test_get_meetup_id_that_doesnt_exist(self):
        token = self.give_token()
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        res = self.app.post('api/v2/meetups/1000/questions',
                            data=json.dumps(self.quiz),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res1['Message'], 'Meetup with that id does not exist')
        self.assertEqual(res.status_code, 404)


    def test_upvote_a_question(self):
        token = self.give_token()
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        res = self.app.post(question_url,
                            data=json.dumps(self.quiz),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        res = self.app.patch('api/v2/meetups/questions/1/upvote',
                            data=json.dumps(self.upvote),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)

    def test_downvote_a_question(self):
        token = self.give_token()
        res = self.app.post(meetups_url,
                            data=json.dumps(self.meetup),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        res = self.app.post(question_url,
                            data=json.dumps(self.quiz),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        res = self.app.patch('api/v2/meetups/questions/1/downvote',
                            data=json.dumps(self.upvote),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        res1 = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
