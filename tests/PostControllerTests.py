
import unittest
from controllers.PostController import Posts

class MockEmptyPostProvider():
    def get_posts(self):
        return []

class MockFullPostProvider():
    def get_posts(self):
        return ['valid','values']

class TestPostController(unittest.TestCase):

    def test_PostsGetReturns404_whenPostProviderReturnsEmptyList(self):
        post_controller = Posts(MockEmptyPostProvider())
        actual = post_controller.get()
        print(actual)

if __name__ == '__main__':
    unittest.main()