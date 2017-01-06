from . import *

from application import app as client
from application import SMOKE_URL


class TestSmoke(flask_testing.TestCase):

    def create_app(self):
        app = client
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.client = client.test_client()
        self.response = self.client.get(SMOKE_URL)

    def tearDown(self):
        pass

    def test_200_ok(self):
        """Assert that the request to the specified URL returns a successful response"""
        self.assert200(self.response)

    def test_json_variables(self):
        """Assert that the request to the specified URL returns the expected json"""
        assert_that(self.response.json['foo'], is_(equal_to('bar')))
