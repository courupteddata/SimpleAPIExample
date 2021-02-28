from unittest import TestCase

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class MainTest(TestCase):
    def test_hello_world(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200, "Should always be successful")
        self.assertEqual(response.json(), {"message": "Hello World"}, "Return message should be Hello World with key "
                                                                      "message")

    def test_echo_message(self):
        message = "Test_message"
        query = "query_value"
        response = client.get(f"/echo/{message}?query={query}")

        self.assertEqual(response.status_code, 200, "Echo should be successful")
        self.assertEqual(response.json(), {"message": message, "query": query}, "Message and query should match "
                                                                                "expected values")
