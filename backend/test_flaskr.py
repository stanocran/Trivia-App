import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
        DB_USER = os.getenv('DB_USER', 'postgres')  
        DB_PASSWORD = os.getenv('DB_PASSWORD', '1Bromptoncourt')  
        DB_NAME = os.getenv('DB_NAME', 'trivia_test') 
        self.database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            
            
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # test get paginated questions
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))
        self.assertTrue(len(data['questions']))

    # test get paginated questions with non existing page number
    def test_404_get_paginated_questions(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page not found!')

    # test get categories
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

 # test getting questions by category
    def test_get_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['current_category'], 'Science')
        self.assertEqual(data['success'], True)

    # test getting questions by non existing category 
    def test_get_404_questions_by_category(self):
        res = self.client().get('/categories/1000/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'Page not found!')
        self.assertEqual(data['success'], False)

    # test delete a question with specified id 
    def test_delete_question(self):
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)
        question =Question.query.filter(Question.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(question,None)

    # test detele a question with an id that does not exist
    def test_delete_question_404(self):
        res = self.client().delete('/questions/5000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page not found!')

    # test adding a new question 
    def test_add_question(self):
        new_question = {
            'question': 'what is your name?',
            'answer': 'Stanley',
            'difficulty': 1,
            'category': 1
        }
        res = self.client().post('/questions', json=new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question_created'])
        self.assertTrue(len(data['questions']))
        

    # test search found function
    def test_search(self):
        search = {'searchTerm': 'title', }
        res = self.client().post('/search', json=search)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    # test search not found function
    def test_search_not_found(self):
        search = {
            'searchTerm': '',
        }
        res = self.client().post('/search', json=search)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page not found!')


    # test quiz functionality
    def test_quiz(self):
        quiz = {
            'previous_questions': [13],
            'quiz_category': {
                'type': 'Entertainment',
                'id': '3'
            }
        }
        res = self.client().post('/quizzes', json=quiz)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['question']['category'], 3)

    # test quiz functionality failure
    def test_quiz_category_not_found(self):
        quiz = {
            'previous_questions': [6],
            'quiz_category': {
                'type': 'games',
                'id': ''
            }
        }
        res = self.client().post('/quizzes', json=quiz)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


    
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()