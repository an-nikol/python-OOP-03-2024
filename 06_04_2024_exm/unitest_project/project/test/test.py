from project.social_media import SocialMedia
import unittest


class TestSocialMedia(unittest.TestCase):
    def setUp(self) -> None:
        self.social_media = SocialMedia("ani123", "Instagram", 500, "entertaining")

    def test_init_constructor(self):
        self.assertEqual(self.social_media._username, "ani123")
        self.assertEqual(self.social_media._platform, "Instagram")
        self.assertEqual(self.social_media.followers, 500)
        self.assertEqual(self.social_media._content_type, "entertaining")
        self.assertEqual(self.social_media._posts, [])

        self.social_media._posts = ["dog", "cat"]
        self.assertEqual(self.social_media._posts, ["dog", "cat"])

    def test_invalid_platform_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            test_social_media = SocialMedia("ani123", "Pinterest", 500, "entertaining")

        self.assertEqual(str(ex.exception), f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']")

    def test_invalid_followers_raises_exception(self):
        test_social_media = SocialMedia("ani123", "Instagram", 100, "entertaining")

        with self.assertRaises(ValueError) as ex:
            test_social_media.followers = -1

        self.assertEqual(str(ex.exception), "Followers cannot be negative.")

    def test_create_new_post(self):
        self.assertEqual(self.social_media._posts, [])

        result = self.social_media.create_post("dog")
        self.assertEqual(result, f"New entertaining post created by ani123 on Instagram.")
        self.assertEqual(self.social_media._posts, [{'content': "dog", 'likes': 0, 'comments': []}])

        result_2 = self.social_media.create_post("cat")
        self.assertEqual(result_2, f"New entertaining post created by ani123 on Instagram.")
        self.assertEqual(self.social_media._posts, [{'content': "dog", 'likes': 0, 'comments': []}, {'content': "cat", 'likes': 0, 'comments': []}])

    def test_like_post_returns_invalid_idx_longer_than_list(self):
        self.social_media._posts = [{'content': "dog", 'likes': 0, 'comments': []},
                                    {'content': "cat", 'likes': 0, 'comments': []},
                                    {'content': "gorilla", 'likes': 0, 'comments': []}]

        result = self.social_media.like_post(3)

        self.assertEqual(result, "Invalid post index.")

    def test_like_post_returns_invalid_idx_less_than_list(self):
        self.social_media._posts = [{'content': "dog", 'likes': 0, 'comments': []},
                                    {'content': "cat", 'likes': 0, 'comments': []},
                                    {'content': "gorilla", 'likes': 0, 'comments': []}]

        result = self.social_media.like_post(-1)

        self.assertEqual(result, "Invalid post index.")

    def test_like_post_when_reached_max_number_of_likes(self):
        self.social_media._posts = [{'content': "dog", 'likes': 10, 'comments': []},
                                    {'content': "cat", 'likes': 10, 'comments': []},
                                    {'content': "gorilla", 'likes': 0, 'comments': []}]

        result = self.social_media.like_post(0)
        self.assertEqual(result, "Post has reached the maximum number of likes.")

    def test_like_post_successful(self):

        self.social_media._posts = [{'content': "dog", 'likes': 9, 'comments': []},
                                    {'content': "cat", 'likes': 5, 'comments': []},
                                    {'content': "gorilla", 'likes': 0, 'comments': []}]

        result = self.social_media.like_post(0)
        self.assertEqual(result, "Post liked by ani123.")

        result_2 = self.social_media.like_post(1)
        self.assertEqual(result_2, "Post liked by ani123.")

        result_3 = self.social_media.like_post(2)
        self.assertEqual(result_3, "Post liked by ani123.")

        self.assertEqual(self.social_media._posts, [{'content': "dog", 'likes': 10, 'comments': []},
                                    {'content': "cat", 'likes': 6, 'comments': []},
                                    {'content': "gorilla", 'likes': 1, 'comments': []}])

    def test_comment_on_post_less_than_10_chars(self):
        self.social_media._posts = [{'content': "dog", 'likes': 9, 'comments': []},
                                    {'content': "cat", 'likes': 5, 'comments': []},
                                    {'content': "gorilla", 'likes': 8, 'comments': []}]

        result = self.social_media.comment_on_post(0, "Cute!")

        self.assertEqual(result, "Comment should be more than 10 characters.")

    def test_comment_on_post_successful(self):
        self.social_media._posts = [{'content': "dog", 'likes': 9, 'comments': []},
                                    {'content': "cat", 'likes': 5, 'comments': []},
                                    {'content': "gorilla", 'likes': 8, 'comments': []}]

        result = self.social_media.comment_on_post(0, "012345678910")

        self.assertEqual(result, "Comment added by ani123 on the post.")
        self.assertEqual(self.social_media._posts, [
            {'content': "dog", 'likes': 9, 'comments': [{"user": "ani123", "comment": "012345678910"}]},
            {'content': "cat", 'likes': 5, 'comments': []},
            {'content': "gorilla", 'likes': 8, 'comments': []}
        ])

        result_2 = self.social_media.comment_on_post(1, "That is the most scary gorilla I have seen in my life!")
        self.assertEqual(result_2, "Comment added by ani123 on the post.")
        self.assertEqual(self.social_media._posts, [
            {'content': "dog", 'likes': 9, 'comments': [{"user": "ani123", "comment": "012345678910"}]},
            {'content': "cat", 'likes': 5, 'comments': [{"user": "ani123", "comment": "That is the most scary gorilla I have seen in my life!"}]},
            {'content': "gorilla", 'likes': 8, 'comments': []}
        ])

if __name__ == "__main__":
    unittest.main()