from django.test import TestCase
from portfolio.threadly.models import Comment

# Create your tests here.
class CommentTest(TestCase):

    def create_comment(self, pageName="sports", name="John Doe", email="john_doe@aol.com", body="Sports keeps you healthy."):
        return Comment.objects.create(pageName=pageName, name=name, email=email, body=body)
    
    def test_comment_creation(self):
        comment = self.create_comment()
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(str(comment), comment.body)