
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
        expected = {'message': 'No posts found'}, 404
        actual = post_controller.get()
        self.assertEqual(expected, actual)

    def test_PostsGetReturns200AndValidValue_whenPostProviderReturnsValidValues(self):
        post_controller = Posts(MockFullPostProvider())
        expected = {'all_posts': ['valid', 'values']}, 200
        actual = post_controller.get()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()