import unittest
from flask import current_app
from app import create_app,db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('production')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exits(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertFalse(current_app.config['WTF_CSRF_ENABLED'])