import unittest
import requests

class TestApp(unittest.TestCase):

    def test_index(self):
        response = requests.get("http://54.164.167.80:5000/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
